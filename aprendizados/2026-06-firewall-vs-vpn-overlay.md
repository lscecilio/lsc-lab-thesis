# Aprendizado: o firewall do host pode estar mentindo pra você

> Categoria: segurança / hermeticidade · Virou regra: sim · Data: 2026-06

## O sintoma

Um alerta apontou que serviços internos — que deveriam ser acessíveis
**apenas** pelo gateway autenticado — estavam alcançáveis direto, pulando o
gate. O estranho: o firewall do host **já tinha regras de bloqueio**
para exatamente essas portas. As regras existiam, estavam "ativas", e mesmo
assim não bloqueavam nada.

## A causa-raiz (o pulo do gato)

A rede entre as máquinas é uma **VPN overlay** (malha cifrada ponto-a-ponto). Esse
tipo de VPN instala, por conta própria, uma regra no início da cadeia
`INPUT` do netfilter que **aceita incondicionalmente** todo tráfego que chega
pela interface da VPN — e essa regra roda **antes** do firewall do host.

Resultado: como o netfilter é *first-match*, todo pacote vindo da malha era
aceito pela regra da VPN antes de chegar nas regras do firewall. As regras do
do firewall para a VPN eram **letra morta** (contador de pacotes: zero). Os únicos
serviços de fato protegidos eram os que, por acaso, já escutavam só em
`loopback` — ou seja, protegidos no nível do *socket*, não do firewall.

**A lição central:** num host dentro de uma VPN overlay, as regras do
firewall comum **não governam** o tráfego da malha por padrão. Você acha que
está protegido; não está.

## A regra que ficou

1. **Hermeticidade se prova de fora, não de dentro.** Bloqueio só é real
   quando verificado a partir de **outro nó da malha** (um peer), não com
   `curl localhost`. Teste de fora ou não teste.

2. **A regra de bloqueio precisa ficar ACIMA do accept da VPN.** O controle
   tem que ser inserido no topo da cadeia, antes do ponto onde a VPN aceita
   tudo. Bloqueio colocado "depois" é decorativo.

3. **Detectar não basta — tem que auto-curar (loop fechado).** A VPN
   **reescreve** as próprias regras a cada reconfiguração/atualização, o que
   reabriria o buraco. Então a defesa não é uma regra estática: é um **guard
   idempotente em timer** que, a cada poucos minutos, (a) derruba qualquer
   serviço exposto fora de uma *allowlist* e (b) reafirma sua posição no topo
   da cadeia. App novo subiu exposto? Fechado sozinho no próximo ciclo.

4. **O guard só aperta, nunca arrisca lockout.** Ele pode adicionar bloqueio
   de porta de aplicação, mas **nunca** toca no plano de controle (acesso
   administrativo, gateway, banco). Auto-fix que pode te trancar do lado de
   fora não é auto-fix, é roleta.

5. **Allowlist > blocklist, com *grandfather* explícito.** O default é negar;
   o que é intencionalmente exposto fica numa lista versionada e auditável.
   O que já existia mas não foi verificado entra como *grandfathered* — com
   comentário — em vez de quebrar um fluxo desconhecido às cegas.

## Por que isso importa pra tese

Isto é a tese em miniatura: um detector disparou, a causa-raiz estava num
detalhe que "deveria estar resolvido", e o desfecho não foi um ticket pra
alguém olhar depois — foi **diagnóstico → correção verificada → blindagem
permanente que se mantém sozinha**, fechando o loop. Auto-fix com guard
contínuo bate "aprovar passo a passo": o passo a passo nunca teria pego a
reabertura silenciosa na próxima vez que a VPN se reconfigurasse.
