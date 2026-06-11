---
id: exemplos-calculo
titulo: Exemplos práticos de cálculo (emolumentos + tributos) — Uberlândia/MG
categoria: emolumentos
escopo: comarca-uberlandia
publico: [cliente, calculo]
vigencia: 2026
fontes:
  - https://www8.tjmg.jus.br/institucional/at/pdf/cpo86642025.pdf
  - https://eitbi.uberlandia.mg.gov.br/assets/PDF/Lei-ordinaria-4871.pdf
  - https://www.almg.gov.br/legislacao-mineira/texto/LEI/14941/2003/?cons=1
atualizado_em: 2026-06-11
---

# Exemplos práticos de cálculo (valores 2026)

> ⚠️ **Estimativas didáticas** com a tabela 2026. Confirme sempre na serventia. As faixas de
> emolumentos saem de [`emolumentos-mg.md`](emolumentos-mg.md); ITBI de [`itbi-uberlandia.md`](itbi-uberlandia.md);
> ITCD de [`itcd-mg.md`](itcd-mg.md).

## Roteiro geral de uma compra e venda de imóvel à vista

Custo total ≈ **ITBI + emolumentos da escritura (Notas) + emolumentos do registro (RI)**.

1. **ITBI (Uberlândia):** 2% × valor de mercado declarado.
2. **Escritura (Tabela 1, conteúdo financeiro):** valor final da faixa do imóvel.
3. **Registro (Tabela 4, item 5.e):** mesma grade da escritura (valor final da faixa).
4. (+ certidões, prenotação, exame e cálculo quando cobrados à parte.)

---

## Exemplo 1 — Imóvel de R$ 300.000,00 (compra à vista)

| Item | Cálculo | Valor |
|---|---|---|
| ITBI (2%) | 0,02 × 300.000 | **R$ 6.000,00** |
| Escritura de compra e venda | faixa 280.000,01–350.000,00 | **R$ 4.903,53** |
| Registro na matrícula | mesma faixa (Tabela 4, 5.e) | **R$ 4.903,53** |
| **Total aproximado** | | **≈ R$ 15.807,06** |

(≈ 5,3% do valor do imóvel.)

## Exemplo 2 — Imóvel de R$ 300.000,00 financiado pelo SFH

| Item | Cálculo | Valor |
|---|---|---|
| ITBI — parte financiada (ex.: R$ 240.000 a 0,5%) | 0,005 × 240.000 | R$ 1.200,00 |
| ITBI — parte restante (R$ 60.000 a 2%) | 0,02 × 60.000 | R$ 1.200,00 |
| **ITBI total** | | **R$ 2.400,00** |
| Escritura | em geral por **instrumento particular com força de escritura** (financiamento SFH) | dispensada/reduzida |
| Registro (com redução de 50% — Nota XV) | R$ 4.903,53 × 0,5 | **≈ R$ 2.451,77** |
| Registro da alienação fiduciária | ato de garantia (à parte) | conforme tabela |

> Financiamento SFH reduz emolumentos (Nota XV = −50%); o contrato do banco costuma dispensar a escritura
> pública (instrumento particular com força de escritura, art. 108 CC + Lei 9.514/97).

## Exemplo 3 — Imóvel de R$ 1.000.000,00 (compra à vista)

| Item | Cálculo | Valor |
|---|---|---|
| ITBI (2%) | 0,02 × 1.000.000 | **R$ 20.000,00** |
| Escritura | faixa 840.000,01–1.120.000,00 | **R$ 6.866,53** |
| Registro | mesma faixa | **R$ 6.866,53** |
| **Total aproximado** | | **≈ R$ 33.733,06** |

## Exemplo 4 — Inventário extrajudicial (espólio de R$ 500.000,00)

| Item | Cálculo | Valor |
|---|---|---|
| ITCD (5%, sem desconto) | 0,05 × 500.000 | **R$ 25.000,00** |
| ITCD (com desconto de 15% se pago em 90 dias) | 25.000 × 0,85 | **R$ 21.250,00** |
| Escritura de inventário (conteúdo financeiro, faixa 420.000,01–560.000,00) | | **R$ 5.523,14** |
| Registro do formal/partilha de imóvel na matrícula | conforme valor do imóvel | conforme tabela |
| Honorários advocatícios | obrigatório (livremente contratados) | — |

## Exemplo 5 — Doação de imóvel de R$ 200.000,00 (com reserva de usufruto)

| Item | Cálculo | Valor |
|---|---|---|
| ITCD (5%) | 0,05 × 200.000 | **R$ 10.000,00** |
| ITBI | **não incide** (doação é gratuita) | R$ 0,00 |
| Escritura de doação (faixa 175.000,01–210.000,00) | | **R$ 4.238,32** |
| Registro na matrícula | mesma faixa | **R$ 4.238,32** |

> Doação até **10.000 UFEMG** (≈ R$ 57.899 em 2026) é **isenta** de ITCD.

## Exemplo 6 — Atos avulsos de notas

| Ato | Valor final |
|---|---|
| Reconhecimento de firma (1 assinatura) | R$ 11,21 |
| Autenticação de cópia (1 folha) | R$ 11,21 |
| Procuração genérica (1 outorgante) | R$ 68,94 |
| Ata notarial (até 2 folhas) | R$ 218,42 |
| Escritura de divórcio sem partilha | R$ 655,68 |

---

## Pseudocódigo para o RAG (cálculo determinístico)

```
função calcular_compra_venda(valor_imovel, financiado_sfh=false):
    # 1) ITBI
    se financiado_sfh:
        itbi = 0.005 * valor_financiado + 0.02 * (valor_imovel - valor_financiado)
    senão:
        itbi = 0.02 * valor_imovel

    # 2) emolumentos: buscar faixa em emolumentos-mg.json -> escritura_e_registro_conteudo_financeiro
    escritura = faixa.final
    registro  = faixa.final              # mesma grade
    se financiado_sfh: registro *= 0.5   # Nota XV (-50%)

    total = itbi + escritura + registro
    retornar { itbi, escritura, registro, total }
```
