#!/usr/bin/env python3
# onboard_dxf.py — converte um DXF (qualquer projeto) em geojson consumidos pelo Atlas Sketch.
# Produz: <slug>_cad.geojson (LineStrings WGS84 c/ properties.layer),
#         <slug>.geojson (massas: Polygons a partir de LineStrings fechadas de lotes/quadras),
#         <slug>_muros.geojson (se houver layers de muro) e o manifesto <slug>.json.
# Reaproveita ogr2ogr para reprojetar; NAO toca em dados existentes (escreve so nos caminhos passados).
import argparse, json, os, subprocess, sys, tempfile, collections

# ---------- heuristicas de layers ----------
LOTE_HINTS  = ("LOTE",)
QUADRA_HINTS= ("QUADRA",)
MURO_HINTS  = ("MURO",)

def layer_matches(name, hints):
    u = (name or "").upper()
    return any(h in u for h in hints)

def ogr_to_wgs84(dxf, s_srs):
    """Converte DXF -> GeoJSON via ogr2ogr. Se s_srs dado, reprojeta p/ EPSG:4326."""
    tmp = tempfile.NamedTemporaryFile(suffix=".geojson", delete=False).name
    os.unlink(tmp)
    cmd = ["ogr2ogr","-f","GeoJSON",tmp,dxf]
    if s_srs:
        cmd += ["-s_srs",s_srs,"-t_srs","EPSG:4326"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(tmp):
        sys.stderr.write("ogr2ogr falhou: %s\n%s\n" % (r.returncode, r.stderr))
        sys.exit(3)
    d = json.load(open(tmp))
    os.unlink(tmp)
    return d

def detect_s_srs(dxf):
    """Detecta CRS-fonte por magnitude das coords nativas. UTM SIRGAS2000 22S=EPSG:31982."""
    d = ogr_to_wgs84(dxf, None)  # sem reproj -> coords nativas
    xs=[]; ys=[]
    for f in d["features"]:
        g=f.get("geometry")
        if not g: continue
        c=g["coordinates"]
        while c and isinstance(c[0],list): c=c[0]
        if c and isinstance(c[0],(int,float)):
            xs.append(c[0]); ys.append(c[1])
        if len(xs)>50: break
    if not xs:
        return None,"vazio"
    mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
    if -180<=mx<=180 and -90<=my<=90:
        return None,"ja-em-graus(WGS84?)"
    if 100000<mx<900000 and 7000000<my<8200000:
        return "EPSG:31982","UTM-SIRGAS2000-22S(EPSG:31982) por magnitude X~%.0f Y~%.0f"%(mx,my)
    return "EPSG:31982","fallback EPSG:31982 (magnitude X~%.0f Y~%.0f - VERIFICAR)"%(mx,my)

def coords_closed(coords, tol=1e-6):
    if len(coords)<4: return False
    a,b=coords[0],coords[-1]
    return abs(a[0]-b[0])<tol and abs(a[1]-b[1])<tol

def bbox_of(features):
    miX=miY=1e18; maX=maY=-1e18
    def walk(c):
        nonlocal miX,miY,maX,maY
        if c and isinstance(c[0],(int,float)):
            miX=min(miX,c[0]); maX=max(maX,c[0]); miY=min(miY,c[1]); maY=max(maY,c[1])
        else:
            for x in c: walk(x)
    for f in features:
        g=f.get("geometry")
        if g: walk(g["coordinates"])
    if miX>maX: return None
    return (miX,miY,maX,maY)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--slug",required=True)
    ap.add_argument("--dxf",required=True)
    ap.add_argument("--name",default=None)
    ap.add_argument("--data-dir",default="/var/www/atlas-sketch/data")
    ap.add_argument("--s-srs",default=None,help="CRS-fonte (ex EPSG:31982); auto se omitido")
    a=ap.parse_args()
    slug=a.slug; name=a.name or slug; dd=a.data_dir
    if not os.path.exists(a.dxf):
        sys.stderr.write("DXF nao encontrado: %s\n"%a.dxf); sys.exit(2)

    s_srs=a.s_srs; how=("forcado %s"%s_srs) if s_srs else None
    if not s_srs:
        s_srs,how=detect_s_srs(a.dxf)
    sys.stderr.write("[onboard] CRS-fonte: %s (%s)\n"%(s_srs,how))

    d=ogr_to_wgs84(a.dxf, s_srs)
    feats=d["features"]

    # ---------- CAD: todas as LineStrings, properties.layer ----------
    cad=[]
    for f in feats:
        g=f.get("geometry")
        if not g or g["type"]!="LineString": continue
        lay=(f.get("properties") or {}).get("Layer") or (f.get("properties") or {}).get("layer") or "?"
        cad.append({"type":"Feature","properties":{"layer":lay},"geometry":g})
    cad_fc={"type":"FeatureCollection","features":cad}

    # ---------- MASSAS: LineStrings fechadas em layers de lote/quadra -> Polygons ----------
    massas=[]; nlote=0; nquadra=0
    for f in feats:
        g=f.get("geometry")
        if not g or g["type"]!="LineString": continue
        lay=(f.get("properties") or {}).get("Layer") or ""
        is_lote=layer_matches(lay,LOTE_HINTS)
        is_quadra=layer_matches(lay,QUADRA_HINTS)
        if not (is_lote or is_quadra): continue
        cs=g["coordinates"]
        if not coords_closed(cs): continue
        ring=cs[:] if (cs[0]==cs[-1]) else cs+[cs[0]]
        kind="lote" if is_lote else "quadra"
        if is_lote: nlote+=1
        else: nquadra+=1
        uid="%s-%04d"%("L" if is_lote else "Q", (nlote if is_lote else nquadra))
        massas.append({"type":"Feature","properties":{"kind":kind,"use":kind,"uid":uid,"layer_src":lay,"inferido":True},"geometry":{"type":"Polygon","coordinates":[ring]}})
    massas_fc={"type":"FeatureCollection","features":massas}

    # ---------- MUROS: layers MURO* como LineStrings ----------
    muros=[]
    for f in feats:
        g=f.get("geometry")
        if not g or g["type"]!="LineString": continue
        lay=(f.get("properties") or {}).get("Layer") or ""
        if not layer_matches(lay,MURO_HINTS): continue
        kind="muro_cond" if "COND" in lay.upper() else "muro"
        muros.append({"type":"Feature","properties":{"kind":kind,"layer_src":lay},"geometry":g})
    muros_fc={"type":"FeatureCollection","features":muros}

    # ---------- centro = centroide do bbox ----------
    bb=bbox_of(cad) or bbox_of(feats)
    centro={"lat":round((bb[1]+bb[3])/2,6),"lon":round((bb[0]+bb[2])/2,6)} if bb else {"lat":0,"lon":0}

    # ---------- escrita (chmod 644) ----------
    os.makedirs(dd,exist_ok=True)
    p_cad=os.path.join(dd,"%s_cad.geojson"%slug)
    p_mass=os.path.join(dd,"%s.geojson"%slug)
    p_muros=None
    json.dump(cad_fc,open(p_cad,"w")); os.chmod(p_cad,0o644)
    json.dump(massas_fc,open(p_mass,"w")); os.chmod(p_mass,0o644)
    muros_rel=None
    if muros:
        p_muros=os.path.join(dd,"%s_muros.geojson"%slug)
        json.dump(muros_fc,open(p_muros,"w")); os.chmod(p_muros,0o644)
        muros_rel="/data/%s_muros.geojson"%slug
    terreno_path=os.path.join(dd,"%s_terreno.json"%slug)
    terreno_rel="/data/%s_terreno.json"%slug if os.path.exists(terreno_path) else None

    manifest={"slug":slug,"nome":name,"massas":"/data/%s.geojson"%slug,"cad":"/data/%s_cad.geojson"%slug,
              "muros":muros_rel,"terreno":terreno_rel,"engenharia":"/data/engenharia/%s"%slug,"centro":centro}
    proj_dir=os.path.join(dd,"projetos"); os.makedirs(proj_dir,exist_ok=True)
    p_man=os.path.join(proj_dir,"%s.json"%slug)
    json.dump(manifest,open(p_man,"w"),ensure_ascii=False,indent=2); os.chmod(p_man,0o644)

    # ---------- relatorio ----------
    laycnt=collections.Counter(f["properties"]["layer"] for f in cad)
    report={"slug":slug,"s_srs":s_srs,"s_srs_how":how,"cad_features":len(cad),
            "cad_layers":dict(laycnt.most_common()),"massas_features":len(massas),
            "massas_lote":nlote,"massas_quadra":nquadra,"muros_features":len(muros),
            "centro":centro,"manifest":manifest,
            "arquivos":{"cad":p_cad,"massas":p_mass,"muros":p_muros,"manifest":p_man}}
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
