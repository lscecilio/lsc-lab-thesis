# RAG — Cartórios, Registro de Imóveis e Notas — Comarca de Uberlândia/MG

Corpus de conhecimento estruturado para alimentar um sistema RAG (Retrieval-Augmented
Generation) especializado em serviços notariais e registrais da **comarca de Uberlândia,
Minas Gerais**. Cobre: cartórios da comarca, legislação (federal, estadual MG e municipal),
cálculo de emolumentos e tributos (ITBI/ITCD), e os procedimentos extrajudiciais mais comuns.

> ⚠️ **Aviso.** Este material é informativo e foi compilado de fontes públicas (ver
> `fontes` no rodapé de cada documento). **Valores de emolumentos e tributos mudam
> periodicamente** (a tabela de emolumentos de MG é reajustada anualmente). Sempre confirme
> na fonte oficial antes de usar para fins jurídicos ou de cobrança. Datas de vigência estão
> indicadas em cada documento.

## Estrutura

```
rag-cartorios-uberlandia/
├── 00-cartorios/      # Serventias extrajudiciais da comarca (notas, RI, RCPN, RTD/PJ, protesto)
├── 01-legislacao/     # Legislação federal, estadual (MG) e municipal (Uberlândia)
├── 02-emolumentos/    # Tabela de emolumentos MG, ITBI Uberlândia, ITCD MG, exemplos de cálculo
├── 03-processos/      # Guias passo a passo + documentos necessários por procedimento
├── 04-glossario/      # Glossário de termos notariais e registrais
└── data/              # Dados estruturados (JSON/CSV) para uso programático no RAG
```

## Convenção dos documentos (para chunking)

Cada arquivo `.md` traz um *frontmatter* YAML com metadados que facilitam o chunking,
o roteamento de consultas e a filtragem por escopo:

```yaml
---
id: emolumentos-mg
titulo: Tabela de Emolumentos de Minas Gerais
categoria: emolumentos        # cartorios | legislacao | emolumentos | processos | glossario
escopo: estadual-mg           # federal | estadual-mg | municipal-uberlandia | comarca-uberlandia
publico: [cliente, juridico]  # a quem o conteúdo se destina
vigencia: 2026                # ano/data de referência dos valores ou da norma
fontes:                       # URLs de origem (rastreabilidade)
  - https://...
atualizado_em: 2026-06-11
---
```

Recomendações de ingestão:
- **Chunk por seção** (cabeçalhos `##`/`###`); cada seção tende a ser autocontida.
- Indexe o frontmatter como metadado para filtrar por `escopo`, `categoria`, `publico` e `vigencia`.
- Os arquivos em `data/` (JSON/CSV) servem para *function calling*/cálculo determinístico
  (ex.: calcular emolumentos por faixa de valor) — não dependa do LLM para aritmética de tabela.

## Índice

### 00 — Cartórios da comarca
- [`cartorios-uberlandia.md`](00-cartorios/cartorios-uberlandia.md) — lista de serventias, atribuições, endereços, circunscrições

### 01 — Legislação
- [`legislacao-federal.md`](01-legislacao/legislacao-federal.md) — Leis 6.015/73, 8.935/94, 14.382/22, CC, CPC, CNN/CNJ
- [`legislacao-mg.md`](01-legislacao/legislacao-mg.md) — Lei 15.424/04, Código de Normas CGJ-MG
- [`legislacao-municipal.md`](01-legislacao/legislacao-municipal.md) — ITBI e normas tributárias de Uberlândia

### 02 — Emolumentos e tributos
- [`emolumentos-mg.md`](02-emolumentos/emolumentos-mg.md) — composição e tabela de emolumentos MG
- [`itbi-uberlandia.md`](02-emolumentos/itbi-uberlandia.md) — ITBI municipal
- [`itcd-mg.md`](02-emolumentos/itcd-mg.md) — ITCD estadual (heranças e doações)
- [`exemplos-calculo.md`](02-emolumentos/exemplos-calculo.md) — exemplos práticos de cálculo

### 03 — Processos e documentos
- Escritura de compra e venda, registro de imóveis, inventário/divórcio extrajudicial,
  usucapião extrajudicial, retificação, procuração, ata notarial, doação, e mais.

### 04 — Glossário
- [`glossario.md`](04-glossario/glossario.md)

### data/ — Dados estruturados
- [`cartorios.json`](data/cartorios.json) — serventias da comarca
- [`emolumentos-mg.csv`](data/emolumentos-mg.csv) / [`.json`](data/emolumentos-mg.json) — faixas de emolumentos
- [`tributos.json`](data/tributos.json) — alíquotas de ITBI/ITCD
- [`fontes.json`](data/fontes.json) — catálogo de fontes citadas

---

*Compilado por LSC-Lab. Conteúdo informativo sob [CC BY-NC 4.0](../LICENSE).*
