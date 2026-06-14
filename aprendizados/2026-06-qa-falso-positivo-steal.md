---
categoria: aprendizado
escopo: qa / observabilidade / loop-fechado
publico: true
vigencia: 2026-06
fontes: [incidente operacional sanitizado]
---

# QA "tudo vermelho" por causa-raiz compartilhada — o loop fechado precisa de auto-heal de *infra*, não de patch por app

Nota de aprendizado **sanitizada** (Evidence Gate), destilada de um incidente real.
Sem IPs, hostnames, portas, nomes de app/cliente ou tokens — só o padrão e as regras que ficaram.

## O que aconteceu

Um gate de QA disparou alerta: vários apps "falhando" de uma vez, score derrubado. Olhando de
perto, **todas** as falhas tinham a **mesma** assinatura genérica (estouro do mesmo timeout, por
uma fração de segundo) e os serviços estavam todos no ar. No mesmo run, os apps que "passaram"
responderam centenas de vezes mais devagar que o normal.

A causa-raiz não era código: era **contenção de CPU no hypervisor** (CPU *steal* alto — vizinho
barulhento na máquina física). A caixa estava sendo estrangulada de fora; os apps estavam lentos,
não quebrados. Os poucos que cruzaram o teto do probe foram marcados como erro.

E, pior que o alarme: o **loop fechado não resolveu sozinho**. Por quatro motivos compostos:

1. **O loop morria no primeiro hop.** O orquestrador aguardava o run com um timeout **menor que a
   duração real** do run. Resultado: ele expirava em todo ciclo e **nunca chegava** nos passos a
   jusante (classificar, abrir incidente, remediar). Nada downstream rodava.
2. O testador era **read-only** por design — só detecta, nunca conserta.
3. O cérebro de remediação estava em **modo sem-LLM** (cap de custo) — não sintetizava correção.
4. **Auto-fix de código era a ferramenta errada.** Não havia código quebrado. Um healer de código
   tentaria "consertar" apps sãos, falharia o verify e daria revert — o clássico
   *"detecta pra sempre, conserta nunca"*.

## As regras que ficaram

1. **Falha simultânea com assinatura idêntica = causa compartilhada, não N bugs.** "Tudo vermelho com
   o mesmo erro" é sinal de **infra/dependência comum** até prova em contrário. Não abra N tarefas de
   correção por app.

2. **Probe de saúde tem que ser *steal-aware*.** Meça a contenção do host (CPU steal/iowait) no início
   do run; sob saturação, **escale o timeout** e **classifique como transitório de infra**.
   *Lento ≠ quebrado.* Um teto de timeout fixo transforma blip de hypervisor em falso "app caído".

3. **Não pague humano por transitório de infra.** Alerta ruidoso treina o operador a ignorar alerta.
   Page só em falha *real* (BUG_REAL); transitório vira nota silenciosa. **Auto-resolver = recuperar
   sozinho quando a contenção cai** — e não acordar ninguém nesse meio-tempo.

4. **O timeout do orquestrador tem que ser maior que a duração real do passo que ele aguarda.** Senão o
   loop morre no 1º hop e tudo a jusante (judge, incidente, remediação) nunca executa. Esse é o bug
   mais traiçoeiro: o sistema *parece* vivo (detecta e alerta) mas o circuito está aberto no início.

5. **Auto-fix de código e auto-heal de infra são pistas diferentes.** Detectar não basta: o desfecho
   certo é **classificar a camada da causa** (código? config? infra/host?) e remediar **naquela
   camada**. Aplicar o remediador errado é pior que não remediar — ele mascara o sintoma e reverte em
   loop.

6. **Mudança em produção viva: staging + dead-man switch + backup versionado.** Valide num clone, faça
   cutover com revert automático armado por tempo, e só desarme depois de provar saúde. Vale ainda mais
   quando a própria caixa está degradada.

## Alinhamento com a tese

Loop fechado de verdade é **detectar → classificar a camada da causa → remediar nela → manter-se
sozinho**. O elo que faltava aqui não era "mais auto-fix": era o sistema **reconhecer que a causa era
infra**, parar de tratar lentidão como bug, e se recuperar quando a contenção passasse — escalando ao
humano só a parte que é genuinamente decisão humana (trocar a máquina contém o vizinho barulhento).

---

🔒 Evidence Gate: self-check rodado — sem IPs/portas/hosts/apps/clientes/tokens; só terminologia
genérica de operação (CPU steal, probe de saúde, loop fechado, dead-man switch).
