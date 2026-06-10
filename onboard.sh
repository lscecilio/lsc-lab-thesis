#!/usr/bin/env bash
# onboard.sh — converte um DXF em "projeto" do Atlas Sketch.
# uso: onboard.sh <slug> <caminho_dxf> [nome_exibicao] [s_srs]
#
# Gera (em /var/www/atlas-sketch/data):
#   <slug>_cad.geojson      LineStrings WGS84 com properties.layer
#   <slug>.geojson          massas: Polygons inferidos de LineStrings fechadas de lotes/quadras
#   <slug>_muros.geojson    (se houver layers MURO*) LineStrings
#   projetos/<slug>.json     manifesto do projeto
# Reaproveita ogr2ogr (DXF->GeoJSON, reproj p/ EPSG:4326). CRS-fonte auto-detectado
# pela magnitude das coords (Chambord = UTM SIRGAS2000 22S / EPSG:31982), ou passado em s_srs.
#
# GUARD-RAILS: escreve SOMENTE nos caminhos acima. NAO toca em projetos/index.html,
# nem em index.json, nem reinicia servicos. chmod 644 nos arquivos publicados.
set -euo pipefail

SLUG="${1:?uso: onboard.sh <slug> <caminho_dxf> [nome_exibicao] [s_srs]}"
DXF="${2:?uso: onboard.sh <slug> <caminho_dxf> [nome_exibicao] [s_srs]}"
NAME="${3:-$SLUG}"
S_SRS="${4:-}"
DATA_DIR="${DATA_DIR:-/var/www/atlas-sketch/data}"

case "$SLUG" in
  chambord|chambord_cad|chambord_muros|index)
    echo "RECUSADO: slug '$SLUG' colidiria com dados protegidos do Chambord. Use outro slug (ex chambord2)." >&2
    exit 1;;
esac
if [ ! -f "$DXF" ]; then echo "DXF nao encontrado: $DXF" >&2; exit 2; fi

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ARGS=(--slug "$SLUG" --dxf "$DXF" --name "$NAME" --data-dir "$DATA_DIR")
[ -n "$S_SRS" ] && ARGS+=(--s-srs "$S_SRS")

python3 "$HERE/onboard_dxf.py" "${ARGS[@]}"

echo "ONBOARD OK | slug=$SLUG | manifesto=$DATA_DIR/projetos/$SLUG.json" >&2
echo "  (lembrete: o agente pai integra projetos/index.json; este script NAO toca nele.)" >&2
