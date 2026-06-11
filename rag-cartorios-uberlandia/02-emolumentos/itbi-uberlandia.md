---
id: itbi-uberlandia
titulo: ITBI — Imposto sobre Transmissão de Bens Imóveis (Uberlândia/MG)
categoria: emolumentos
escopo: municipal-uberlandia
publico: [cliente, juridico, calculo]
vigencia: 2026
fontes:
  - https://eitbi.uberlandia.mg.gov.br/assets/PDF/Lei-ordinaria-4871.pdf
  - https://www.uberlandia.mg.gov.br/prefeitura/secretarias/financas/itbi/
  - https://eitbi.uberlandia.mg.gov.br/
  - https://www.uberlandia.mg.gov.br/2025/04/16/prefeitura-altera-regras-do-itbi-em-beneficio-ao-contribuinte/
atualizado_em: 2026-06-11
---

# ITBI — Imposto sobre Transmissão de Bens Imóveis (Uberlândia)

Imposto **municipal**, pago à Prefeitura de Uberlândia, devido na **transmissão onerosa** de imóveis
(ex.: compra e venda). **Deve ser pago ANTES da lavratura da escritura e do registro.**

> **Lei que rege:** Lei Ordinária Municipal nº **4.871/1989** (regulamentada pelo Decreto 14.502/2013),
> com alterações — a mais recente e relevante é a **Lei Complementar nº 786/2025** (vigente desde
> **25/05/2025**), que mudou a base de cálculo. Sistema de emissão de guia: **e-ITBI**
> (https://eitbi.uberlandia.mg.gov.br/). Dados estruturados: [`../data/tributos.json`](../data/tributos.json).

## 1. Alíquotas (art. 6º da Lei 4.871/1989)

| Hipótese | Alíquota |
|---|---|
| **Transmissões/cessões onerosas em geral** (compra e venda à vista) | **2%** |
| **SFH** (Sistema Financeiro de Habitação, menor renda) — parte **financiada** | **0,5%** |
| **SFH** — valor **restante** (não financiado) | **2%** |
| **Demais transmissões/cessões** | **4%** |

> ⚠️ Correção comum: o regime SFH **não** é "1%". É **0,5% sobre o valor financiado + 2% sobre o
> restante** (texto legal do art. 6º, I).

## 2. Base de cálculo (NOVA regra — LC 786/2025)

- **Desde 25/05/2025:** a base é o **valor dos bens em condições normais de mercado**, **declarado pelo
  contribuinte**, com **presunção de veracidade**. Ficou **desvinculada do valor venal do IPTU**.
- Se o Fisco discordar, instaura **Processo Administrativo Tributário (PAT)**.
- Penalidades por divergência: multa de **50% a 150%** da diferença; correção pela **SELIC**.

**Bases específicas (art. 8º):**

| Operação | Base |
|---|---|
| Domínio útil | 1/3 do valor venal |
| Usufruto / uso / habitação | 1/3 do valor |
| Nua-propriedade | 2/3 do valor |
| Arrematação/leilão | preço pago |
| Permuta | valor de cada imóvel |

## 3. Fato gerador, contribuinte e prazos

- **Fato gerador (arts. 1º-3º):** transmissão inter vivos, onerosa, da propriedade/domínio útil e
  direitos reais (exceto garantia), e cessão de direitos à aquisição. Inclui compra e venda, dação em
  pagamento, arrematação, adjudicação, partilha com excedente oneroso, permuta. Devido quando o imóvel
  está em Uberlândia (ainda que o ato seja celebrado fora).
- **Contribuinte (art. 9º):** o **comprador/adquirente** (na permuta, cada permutante). Responsabilidade
  solidária do cedente e do tabelião em caso de recolhimento insuficiente.
- **Quando paga (arts. 11-12) — sempre ANTES do registro:**
  - Escritura pública: **antes da lavratura**.
  - Documento particular: em **120 dias** da assinatura, sempre antes do registro.
  - Sentença judicial: 30 dias do trânsito em julgado.
  - Arrematação/adjudicação/usucapião: até 30 dias do trânsito em julgado.
- **Art. 14:** tabeliães/registradores **não podem** lavrar/registrar sem o comprovante de ITBI pago.

## 4. Não incidência / imunidades (art. 4º)

- **Integralização de capital** (transmissão para realização de capital de PJ);
- **Fusão, incorporação ou extinção** de PJ;
- Aquisição por **pessoa jurídica de direito público, templos, instituições de educação e assistência social**;
- Permuta/dação em **desapropriação**;
- **Promessas/compromissos** de compra e venda (Lei 12.547/2016).

> **Ressalva (imunidade de integralização/fusão):** NÃO se aplica se a PJ adquirente tiver **atividade
> preponderantemente imobiliária** (>50% da receita em compra/venda/locação de imóveis nos 2 anos
> anteriores e 2 posteriores). Multa de 100% se descumprir.

## 5. Isenções (art. 5º)

- Aquisição de moradia por **ex-combatentes**, viúvas e filhos menores/incapazes (limite em OTN — unidade
  extinta; aplicabilidade a confirmar);
- Aquisição vinculada a **programas habitacionais de promoção social** para baixa renda com participação
  do poder público.

## 6. Como emitir a guia

- Sistema **e-ITBI**: https://eitbi.uberlandia.mg.gov.br/
- Página oficial (Secretaria de Finanças): https://www.uberlandia.mg.gov.br/prefeitura/secretarias/financas/itbi/
- O contribuinte/tabelião emite a guia com a descrição completa do imóvel.

## 7. Pontos a confirmar

1. Regulamentação infralegal da apuração do "valor de mercado" pós-LC 786/2025.
2. Isenção do art. 5º, I (limite em OTN, unidade extinta) — conversão/atualização atual.
3. Incidência de **ISSQN** sobre atos cartorários em Uberlândia (não confunde com ITBI).
