---
id: itcd-mg
titulo: ITCD — Imposto sobre Transmissão Causa Mortis e Doação (Minas Gerais)
categoria: emolumentos
escopo: estadual-mg
publico: [cliente, juridico, calculo]
vigencia: 2026
fontes:
  - https://www.almg.gov.br/legislacao-mineira/texto/LEI/14941/2003/?cons=1
  - https://www.fazenda.mg.gov.br/empresas/impostos/itcd/informacoes.html
  - https://www.fazenda.mg.gov.br/empresas/legislacao_tributaria/resolucoes/ufemg.html
atualizado_em: 2026-06-11
---

# ITCD — Imposto sobre Transmissão Causa Mortis e Doação (MG)

Imposto **estadual** (SEF-MG), devido em **heranças** (causa mortis) e **doações**. É pré-requisito
para a escritura de **inventário extrajudicial** e de **doação**. Em MG chama-se **ITCD** (= ITCMD).

> **Lei que rege:** Lei Estadual MG nº **14.941/2003** (regulamento: Decreto 43.981/2005 — RITCD).
> Sistemas: **e-ITCD** / SIARE. Dados estruturados: [`../data/tributos.json`](../data/tributos.json).

## 1. Alíquota (art. 10)

**Alíquota única de 5%** sobre a base de cálculo — tanto causa mortis quanto doação. MG **não** adota
progressividade.

### Desconto por pagamento antecipado (causa mortis)

- **Desconto de 15%** se o imposto for recolhido em até **90 dias** da abertura da sucessão (óbito), com
  entrega tempestiva da Declaração de Bens e Direitos (DBD).
- **Efeito prático:** 5% (sem desconto) ou **4,25%** (com desconto de 15%) na herança paga em até 90 dias.

> ⚠️ Algumas fontes dizem "4% em até 90 dias / 5% depois" — é simplificação imprecisa. O correto é
> **5% com desconto de 15%** → efetivo 4,25%.

- **Doação:** desconto de 50% do imposto para doação de até **90.000 UFEMG** se recolhido antes de ação
  fiscal (*confirmar no RITCD vigente*).

## 2. Base de cálculo (art. 4º)

**Valor venal = valor de mercado** do bem na data do óbito / avaliação / doação. Expressa em **UFEMG**.

> **UFEMG 2026 = R$ 5,7899** (Resolução SEF nº 5.969/2025). Sempre use a UFEMG do **ano do fato gerador**.

## 3. Fato gerador

- **Causa mortis:** sucessão legítima ou testamentária; imóveis em MG; bens móveis quando o inventário
  tramita em MG ou o herdeiro é domiciliado em MG.
- **Doação:** a qualquer título (inclusive adiantamento de legítima); imóveis em MG; bens móveis quando o
  doador é domiciliado em MG. Inclui **excedente de meação** em divórcio/dissolução de união estável.

## 4. Isenções (art. 3º)

- **Causa mortis:** imóvel residencial até **40.000 UFEMG** (se o monte total não passar de 48.000 UFEMG)
  (≈ R$ 231.596 em 2026); roupas, utensílios agrícolas manuais, móveis e aparelhos domésticos.
- **Doação:** valor total que **não exceda 10.000 UFEMG** (≈ R$ 57.899 em 2026); imóvel doado pelo poder
  público em programas habitacionais; doações da Cohab-MG; imóvel ao FAR (Lei 11.977/2009).

## 5. Prazos de pagamento

| Situação | Prazo |
|---|---|
| Herança | **180 dias** após o óbito (desconto de 15% exige pagamento em 90 dias) |
| Excedente de meação em divórcio | 30 dias da sentença ou antes da escritura |
| Excedente em união estável | 15 dias |
| Doação por escritura | antes da lavratura |
| Doação por escrito particular | 15 dias da assinatura |

## 6. Relação com inventário / doação extrajudicial

Para inventário (judicial ou **extrajudicial**) ou doação, preenche-se a **DBD** e obtém-se a **Certidão
de Pagamento/Desoneração de ITCD** da SEF-MG. **O tabelião exige essa certidão** para lavrar a escritura.
Além do ITCD há os emolumentos do cartório.

- Informações: https://www.fazenda.mg.gov.br/empresas/impostos/itcd/informacoes.html
- Validação da certidão: https://www.fazenda.mg.gov.br/empresas/impostos/itcd/validacao-da-certidao-de-itcd/

## 7. Laudêmio

**NÃO se aplica em Uberlândia.** Laudêmio incide só sobre terrenos de marinha / imóveis foreiros da União
no litoral. Uberlândia é interior, sem orla. Desconsiderar em cálculos padrão.

## 8. Pontos a confirmar

1. Desconto de 50% para doação até 90.000 UFEMG (fonte secundária — confirmar no RITCD).
2. UFEMG de anos anteriores (use sempre a do ano do fato gerador).
