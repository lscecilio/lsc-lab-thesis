#!/usr/bin/env python3
"""
ingest_cartorios.py — Ingestão do corpus "RAG Cartórios de Uberlândia/MG"
na coleção Qdrant `juridico-knowledge` (mesma usada pelo app atlas-juridico-cidadao).

Segue o padrão de scripts/legal-collector/indexar_urbanismo_uberlandia.py:
  - embeddings via OpenAI text-embedding-3-large (3072-dim, igual à coleção)
  - IDs determinísticos (uuid5) -> re-execução é idempotente
  - cada ponto recebe source="rag-cartorios-uberlandia" -> remoção trivial por filtro

Uso (na frota, onde existem OPENAI_API_KEY + Qdrant):
  export OPENAI_API_KEY=$(cat /home/claw/.openclaw/secrets/openai_api_key)
  python3 ingest_cartorios.py --dry-run     # só chunk + estimativa de custo
  python3 ingest_cartorios.py               # embed + upsert

Env opcionais:
  QDRANT_HOST (default 127.0.0.1)  QDRANT_PORT (default 6333)
  COLLECTION  (default juridico-knowledge)  CORPUS_DIR (default ./ do próprio script)
"""
import os, re, sys, glob, time, uuid, argparse
from datetime import datetime, timezone

QDRANT_HOST = os.getenv("QDRANT_HOST", "127.0.0.1")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", "6333"))
COLLECTION  = os.getenv("COLLECTION", "juridico-knowledge")
EMBED_MODEL = os.getenv("EMBED_MODEL", "text-embedding-3-large")
SOURCE_TAG  = "rag-cartorios-uberlandia"
NAMESPACE   = uuid.UUID("00000000-0000-0000-0000-0000ca47011a")  # namespace dedicado (cartórios)
CORPUS_DIR  = os.getenv("CORPUS_DIR", os.path.dirname(os.path.abspath(__file__)))

OPENAI_KEY_FILE = "/home/claw/.openclaw/secrets/openai_api_key"


def parse_front(t):
    fm, body = {}, t
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if m:
        body = t[m.end():]
        for line in m.group(1).splitlines():
            mm = re.match(r"^(\w+):\s*(.*)$", line)
            if mm and mm.group(2).strip():
                fm[mm.group(1)] = mm.group(2).strip()
    return fm, body


def build_chunks():
    chunks = []
    for fp in sorted(glob.glob(os.path.join(CORPUS_DIR, "**", "*.md"), recursive=True)):
        if os.path.basename(fp) == "README.md":
            continue
        t = open(fp, encoding="utf-8").read()
        fm, body = parse_front(t)
        stem = os.path.splitext(os.path.basename(fp))[0]
        cat = fm.get("categoria", "cartorios")
        esc = fm.get("escopo", "comarca-uberlandia")
        vig = fm.get("vigencia", "2026")
        h1 = re.search(r"^#\s+(.+)$", body, re.M)
        titulo = h1.group(1).strip() if h1 else stem
        rel = os.path.relpath(fp, CORPUS_DIR)
        n = 0
        for part in re.split(r"\n(?=##\s)", body):
            part = part.strip()
            if len(part) < 40:
                continue
            subs = re.split(r"\n(?=###\s)", part) if len(part) > 3500 else [part]
            for s in subs:
                s = s.strip()
                if len(s) < 40:
                    continue
                n += 1
                hm = re.match(r"^#{1,3}\s+(.+)$", s, re.M)
                tema = hm.group(1).strip() if hm else titulo
                chunks.append({
                    "id_logico": f"cartorios-udi-{stem}-{n:02d}",
                    "categoria": cat, "abrangencia": esc, "tema": tema,
                    "vigencia": vig, "fonte": rel, "titulo_doc": titulo,
                    "texto": f"[{titulo}] {s}",
                })
    return chunks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    chunks = build_chunks()
    chars = sum(len(c["texto"]) for c in chunks)
    tokens = chars // 4
    custo = (tokens / 1000) * 0.00013
    print(f"[INFO] corpus={CORPUS_DIR}")
    print(f"[INFO] chunks={len(chunks)} chars={chars} tokens~{tokens} custo_embed~${custo:.4f}")
    print(f"[INFO] collection={COLLECTION}@{QDRANT_HOST}:{QDRANT_PORT} model={EMBED_MODEL} source={SOURCE_TAG}")
    if args.dry_run:
        for c in chunks[:5]:
            print(f"   - {c['id_logico']} | {c['tema'][:60]}")
        print("[DRY-RUN] nada gravado.")
        return

    from openai import OpenAI
    from qdrant_client import QdrantClient
    from qdrant_client.models import PointStruct

    key = os.getenv("OPENAI_API_KEY")
    if not key and os.path.exists(OPENAI_KEY_FILE):
        key = open(OPENAI_KEY_FILE).read().strip()
    if not key:
        print("[ERRO] OPENAI_API_KEY ausente (env ou arquivo de secrets)", file=sys.stderr)
        sys.exit(1)

    oai = OpenAI(api_key=key)
    qd = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT, check_compatibility=False)

    pontos = []
    for i, c in enumerate(chunks, 1):
        pid = str(uuid.uuid5(NAMESPACE, c["id_logico"]))
        vec = oai.embeddings.create(model=EMBED_MODEL, input=c["texto"]).data[0].embedding
        payload = dict(c)
        payload["source"] = SOURCE_TAG
        payload["indexed_at"] = datetime.now(timezone.utc).isoformat()
        pontos.append(PointStruct(id=pid, vector=vec, payload=payload))
        if i % 10 == 0 or i == len(chunks):
            print(f"   embed {i}/{len(chunks)} (dims={len(vec)})")

    qd.upsert(collection_name=COLLECTION, points=pontos, wait=True)
    info = qd.get_collection(COLLECTION)
    print(f"[OK] upsert {len(pontos)} pontos | points_count={info.points_count}")
    print(f"[CUSTO] estimado ${custo:.4f}")
    print(f"[REVERSÍVEL] remover com filtro payload.source == '{SOURCE_TAG}'")


if __name__ == "__main__":
    main()
