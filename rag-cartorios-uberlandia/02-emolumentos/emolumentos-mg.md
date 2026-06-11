---
id: emolumentos-mg
titulo: Emolumentos Cartorários de Minas Gerais — Composição e Tabela 2026
categoria: emolumentos
escopo: estadual-mg
publico: [cliente, juridico, calculo]
vigencia: 2026
fontes:
  - https://www8.tjmg.jus.br/institucional/at/pdf/cpo86642025.pdf
  - https://www.almg.gov.br/legislacao-mineira/texto/LEI/15424/2004/?cons=1
  - https://www.tjmg.jus.br/portal-tjmg/servicos-notariais-e-de-registro/tabela-de-emolumentos.htm
  - https://recivil.com.br/tabela-de-emolumentos/
atualizado_em: 2026-06-11
---

# Emolumentos Cartorários de Minas Gerais (vigência 2026)

> **Norma vigente:** **Portaria nº 8.664/CGJ/2025** (TJMG), publicada no DJe de 18/12/2025,
> **vigência a partir de 01/01/2026**. Base legal: **Lei Estadual nº 15.424/2004**.
> Indexador: **UFEMG 2026 = R$ 5,7899** (Resolução SEF-MG nº 5.969/2025). Os valores são
> reajustados **anualmente** pela variação da UFEMG (art. 50 da Lei 15.424/2004).
> **Dados estruturados para cálculo:** ver [`../data/emolumentos-mg.csv`](../data/emolumentos-mg.csv)
> e [`../data/emolumentos-mg.json`](../data/emolumentos-mg.json).

## 1. Como se compõe o valor pago pelo cidadão

**Valor Final ao Usuário = Emolumentos + Taxa de Fiscalização Judiciária (TFJ).**

Não há terceira parcela cobrada do cidadão. Cada linha das tabelas oficiais traz **3 colunas**:
`Emolumentos | TFJ | Valor Final`. O cidadão paga a 3ª coluna (já é a soma).

| Parcela | O que é | Base legal |
|---|---|---|
| **Emolumentos** | Retribuição pelos atos do notário/registrador. Já englobam traslados, anotações, comunicações, diligências essenciais, certidões internas ao ato, uso de sistemas (art. 7º). | Lei 15.424/2004, arts. 2º e 7º |
| **TFJ** (Taxa de Fiscalização Judiciária) | Tributo pelo poder de polícia do Judiciário sobre as serventias. É **valor tabelado por ato** (coluna própria), **não** um percentual aplicado pelo usuário. | Lei 15.424/2004, art. 3º |
| **Recompe-MG** | 7% dos emolumentos recebidos pela serventia, recolhido **pela própria serventia** (não pelo cidadão), para o Fundo que compensa a gratuidade do Registro Civil. **Não entra no preço ao cidadão.** | Lei 15.424/2004, arts. 31-35 |
| **Recompe-Geral (art. 45-A)** | Nas faixas altas (acima de R$ 3,2 mi), 40% dos emolumentos brutos adicionais vão a MP/Defensoria/AGE, via DAE, **sem custo adicional ao usuário**. | Lei 15.424/2004, art. 45-A |

> ⚠️ Algumas fontes secundárias falam em "TFJ = 7%" — **incorreto** para o cálculo. A TFJ é um
> valor tabelado por ato (coluna própria). Os 7% referem-se ao Recompe (repasse interno da serventia).

> **ISSQN:** a tabela-base do TJMG **não** inclui ISSQN. Alguns municípios acrescem ISS ao valor
> final (ex.: 5% em Almenara, Arinos, Montes Claros). Para **Uberlândia**, confirmar a incidência de
> ISS sobre atos notariais/registrais na tabela municipal aplicada pela serventia.

## 2. Regras de redução mais usadas (Notas das tabelas)

| Situação | Efeito no valor final | Nota |
|---|---|---|
| Imóvel financiado por entidade financeira/governo | **−50%** | Nota XV |
| Imóvel por SFI/SFH/cooperativa/consórcio | **−80%** | Nota XXIII (Tabela 1) |
| Promessa/compromisso de compra e venda, cessão, permuta (registro) | **−50%** | Nota XV (Tabela 4) |
| Usufruto | base = **1/3** do valor do imóvel | Nota X |
| Servidão | base = **20%** do valor | Nota XIV |

## 3. Tabela 1 — Atos do Tabelião de Notas

### 3.1 Escritura pública COM conteúdo financeiro (por faixa do valor declarado)

> **Mesma grade vale para o registro de compra e venda no Registro de Imóveis** (Tabela 4, item 5.e).

| Faixa de valor (R$) | Emol. (R$) | TFJ (R$) | **Final (R$)** |
|---|---|---|---|
| até 1.400,00 | 159,20 | 61,35 | **220,55** |
| 1.400,01 – 2.720,00 | 259,68 | 100,08 | **359,76** |
| 2.720,01 – 5.440,00 | 376,34 | 145,01 | **521,35** |
| 5.440,01 – 7.000,00 | 520,99 | 200,76 | **721,75** |
| 7.000,01 – 14.000,00 | 694,78 | 267,69 | **962,47** |
| 14.000,01 – 28.000,00 | 897,58 | 345,89 | **1.243,47** |
| 28.000,01 – 42.000,00 | 1.129,02 | 435,05 | **1.564,07** |
| 42.000,01 – 56.000,00 | 1.389,81 | 535,50 | **1.925,31** |
| 56.000,01 – 70.000,00 | 1.679,40 | 647,11 | **2.326,51** |
| 70.000,01 – 105.000,00 | 2.113,64 | 814,42 | **2.928,06** |
| 105.000,01 – 140.000,00 | 2.540,87 | 1.180,65 | **3.721,52** |
| 140.000,01 – 175.000,00 | 2.717,08 | 1.262,61 | **3.979,69** |
| 175.000,01 – 210.000,00 | 2.893,66 | 1.344,66 | **4.238,32** |
| 210.000,01 – 280.000,00 | 3.070,72 | 1.701,35 | **4.772,07** |
| 280.000,01 – 350.000,00 | 3.155,22 | 1.748,31 | **4.903,53** |
| 350.000,01 – 420.000,00 | 3.240,20 | 1.795,39 | **5.035,59** |
| 420.000,01 – 560.000,00 | 3.325,70 | 2.197,44 | **5.523,14** |
| 560.000,01 – 700.000,00 | 3.508,36 | 2.318,34 | **5.826,70** |
| 700.000,01 – 840.000,00 | 3.691,51 | 2.439,36 | **6.130,87** |
| 840.000,01 – 1.120.000,00 | 3.875,31 | 2.991,22 | **6.866,53** |
| 1.120.000,01 – 1.400.000,00 | 4.197,56 | 3.240,08 | **7.437,64** |
| 1.400.000,01 – 1.680.000,00 | 4.520,42 | 3.489,30 | **8.009,72** |
| 1.680.000,01 – 3.200.000,00 | 4.844,02 | 3.738,95 | **8.582,97** |
| acima de 3.200.000,00 | *Nota XXV* | — | — |

*Nota XXV/XVII (faixas acima de R$ 3.200.000,00): a cada faixa de R$ 500.000,00 (ou fração, até
100 faixas) acresce R$ 3.289,90 (1ª faixa) e R$ 2.193,27 (subsequentes) sobre emolumentos brutos,
dos quais 40% vão ao art. 45-A; TFJ fixada em R$ 4.673,83.*

### 3.2 Outros atos de Notas

| Ato | Emol. | TFJ | **Final** |
|---|---|---|---|
| Escritura SEM conteúdo financeiro | 55,45 | 17,45 | **72,90** |
| Procuração genérica (por outorgante) | 52,43 | 16,51 | **68,94** |
| Procuração previdência/assistência social | 27,86 | 8,75 | **36,61** |
| Procuração com conteúdo financeiro | 166,18 | 52,23 | **218,41** |
| Substabelecimento | 34,96 | 11,00 | **45,96** |
| Reconhecimento de firma (por assinatura) | 8,55 | 2,66 | **11,21** |
| Autenticação de cópia (por folha) | 8,55 | 2,66 | **11,21** |
| Autenticação eletrônica/digital | 10,01 | 2,98 | **12,99** |
| Ata notarial (até 2 folhas) | 166,18 | 52,24 | **218,42** |
| Ata notarial (por folha acrescida) | 8,55 | 2,66 | **11,21** |
| Testamento público | 332,64 | 104,60 | **437,24** |
| Revogação de testamento | 166,29 | 52,34 | **218,63** |
| Aprovação de testamento cerrado | 498,82 | 156,88 | **655,70** |
| Pacto antenupcial / divórcio / união estável e dissolução | 498,82 | 156,86 | **655,68** |
| Convenção de condomínio | 132,88 | 41,80 | **174,68** |
| Aditamento/retificação sem conteúdo financeiro | 32,98 | 10,37 | **43,35** |

## 4. Tabela 4 — Atos do Oficial de Registro de Imóveis

| Ato | Emol. | TFJ | **Final** |
|---|---|---|---|
| **Registro com conteúdo financeiro** (compra e venda) | *idem Tabela 1 §3.1, mesma grade* | | de **220,55** a **8.582,97** |
| Registro SEM conteúdo financeiro | 26,16 | 8,23 | **34,39** |
| Matrícula / cancelamento de matrícula | 69,42 | 21,83 | **91,25** |
| Prenotação | 53,11 | 10,72 | **63,83** |
| Exame e cálculo | 88,93 | 17,96 | **106,89** |
| Certidão de situação jurídica atualizada | 137,70 | 21,45 | **159,15** |
| Usucapião extrajudicial — processamento | 2.571,61 | 541,95 | **3.113,56** (+ registro pelo 5.e) |
| Indicação de registro/averbação | 8,55 | 2,66 | **11,21** |
| Procedimento de intimação (fiduciante/promissário, por pessoa) | 159,19 | 61,35 | **220,54** |

### 4.1 Averbações (Tabela 4, item 1)

| Averbação | **Final** |
|---|---|
| Cédula hipotecária / alteração de cláusula / quitação / sem conteúdo financeiro | **36,27** |
| Cancelamento de ônus/direitos reais — até 1.400 | **36,27** |
| Cancelamento de ônus — 1.400,01 a 5.000 | **43,55** |
| Cancelamento de ônus — 5.000,01 a 20.000 | **87,14** |
| Cancelamento de ônus — acima de 20.000 | **145,25** |
| Cancelamento de registro/averbação | **36,27** |
| Contrato de promessa de compra e venda/cessão | **metade** do item 5.e |

### 4.2 Penhora/arresto/sequestro (item 5.f)

| Faixa | **Final** |
|---|---|
| até 1.400,00 | **24,87** |
| 1.400,01 – 5.000,00 | **29,83** |
| 5.000,01 – 20.000,00 | **59,69** |
| acima de 20.000,00 | **99,49** |

## 5. Tabela 7 — Registro Civil das Pessoas Naturais (principais)

| Ato | **Final** |
|---|---|
| Registro de nascimento e de óbito + 1ª certidão | **GRATUITO** (Lei 9.534/97) |
| Habilitação para casamento | **360,69** |
| Diligência de casamento fora da serventia | **673,40** |
| Assento de casamento | **94,16** |
| Registros no Livro "E" | **141,24** |
| Averbação para alteração/cancelamento | **113,00** |
| Certidão em resumo/negativa | **63,83** |
| Certidão de inteiro teor | **127,64** |
| Reconhecimento de paternidade/maternidade / retificação | **159,02** |
| Termo declaratório de união estável | **655,69** |

## 6. Tabela 8 — Atos comuns a registradores e notários

| Ato | **Final** |
|---|---|
| Arquivamento (por folha) | **13,43** |
| Busca (período de 5 anos) | **9,45** |
| Certidão inteiro teor/resumo | **41,08** |
| Certidão em relatório por quesitos | **63,83** |
| Levantamento de dúvida não efetivado | **36,27** |

## 7. Gratuidades e isenções (Lei 15.424/2004, arts. 20-21)

- **Registro Civil — gratuidade universal:** registro de nascimento, de óbito e **primeira certidão**
  são **gratuitos a todos** (Lei federal 9.534/97). Compensados pelo Recompe (mín. 40 UFEMGs por ato).
- **Pessoas reconhecidamente pobres (art. 21):** isenção de emolumentos para habilitação/assento de
  casamento e respectivas certidões; demais certidões de registro civil. Exige **declaração de pobreza**.
- **Habitação social (art. 20):** redução/isenção em aquisição de casa própria até 60 m² em programas
  habitacionais; financiamento por entidade financeira/governo → −50% (Nota XV); SFI/SFH/cooperativa/
  consórcio → −80% (Nota XXIII).
- **REURB-S:** atos de registro/averbação e certidões **isentos** de emolumentos no Registro de Imóveis.
- **Outras (art. 20):** atos de interesse da União/Estado/Município; penhora/arresto em execução fiscal
  (Lei 6.830/80); certidões requisitadas pela Justiça Eleitoral.

## 8. Fonte canônica para ingestão

Para o RAG, recomenda-se ingerir como fontes canônicas:
1. **PDF da Portaria 8.664/CGJ/2025** (8 tabelas completas + ~27 Notas por tabela com todas as regras
   de redução e faixas adicionais): https://www8.tjmg.jus.br/institucional/at/pdf/cpo86642025.pdf
2. **Lei 15.424/2004** (estrutura jurídica): https://www.almg.gov.br/legislacao-mineira/texto/LEI/15424/2004/?cons=1
