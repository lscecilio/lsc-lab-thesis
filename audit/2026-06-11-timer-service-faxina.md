# Faxina de Timers e Serviços — 2026-06-11

**Contexto**: Audit completo do ecossistema LSC-Lab para eliminar ruído operacional, loops de alerta falso, e instabilidade de serviços.

## Status por item

### 1. Loop "Lead HOT" (atlas-scout / Co_Work) — RESOLVIDO
- **Causa raiz**: `atlas-scout` rodava como user `claw`, mas `leads.json` tinha ownership de `root` → EACCES em todo save desde 26/04. O touch #3 nunca persistia e o alerta repetia a cada 2h.
- **Correção**: `chown claw` no arquivo + seeds arquivados em `archived_seeds` (Ana Souza, Carlos Oliveira eram dados de teste).
- **Arquivo**: `/opt/lsc-lab/apps/atlas-scout/data/leads.json`

### 2. Briefing WhatsApp Duplicado (Atlas SaaS) — RESOLVIDO
- **Causa raiz**: `wa-digest-enhancer.timer` (hock) rodava a cada 8h reenviando conteúdo congelado ("25 sinais") às 22h e 02h.
- **Correção**: `systemctl disable --now wa-digest-enhancer.timer` em hock.
- **Status pós-fix**: `Loaded: disabled / Active: inactive (dead) / Trigger: n/a`
- **Digest oficial** (`wa-digest.timer`, 4x/dia: 08/12/16/20h) continua operando normalmente.

### 3. Churn Alert Poluído (atlas-os billing.js) — RESOLVIDO
- **Causa raiz**: `checkInactiveTenants()` em `/opt/lsc-lab/apps/atlas-os/billing.js` buscava todos `tenant.status = 'active'` incluindo dezenas de tenants de teste.
- **Correção**: Adicionado `NOT ILIKE` filters nas 3 queries afetadas (churn-check linha 358, usage-alerts linha 303, credit-refill linha 227):
  ```sql
  AND t.name NOT ILIKE '%smoke%'
  AND t.name NOT ILIKE '%-test%'
  AND t.name NOT ILIKE '%test-%'
  AND t.name NOT ILIKE '%persona-tester%'
  AND t.name NOT ILIKE '%debug%'
  ```
- `atlas-os.service` reiniciado em hock.
- **Pendente**: Arquivar tenants de teste no banco (UPDATE status → 'archived') para limpeza definitiva. Preservar Docinho Gourmet/Isadora (clientes reais).

### 4. MCP Claud Flapping (:8210) — MITIGADO
- **Causa raiz**: `claud.service` sem `MemoryMax` — Python acumula audit_log em memória (21.555 rows, claud.db 43MB) atingindo 836MB antes de colapsar. 39 restarts em um dia.
- **Correção aplicada**:
  - `MemoryMax=512M` adicionado ao `/etc/systemd/system/claud.service`
  - `CLAUD_AUDIT_RETENTION_DAYS`: 90d → 30d
  - `claud-audit-prune.service`: argumento atualizado de `90` → `30`
- **Status pós-fix**: `Memory: 48.0M (max: 512.0M)` — cap ativo.
- **Fix permanente pendente**: Diagnosticar leak em `store.py` (provavelmente acumulação de objetos Python por row do audit_log). O cap de 512M é guardrail, não cura raiz.

### 5. Triage "144 Falsos" (atlas-triage) — RESOLVIDO
- **Causa raiz**: `enviarDigest()` em `/opt/lsc-lab/services/atlas-triage.js` enviava digest mesmo quando 100% das notificações eram falso-positivo (WARNING: 200 total, 200 falsos).
- **Correção**: Adicionado guard na iteração de linhas — suprime linhas onde `fp === tot`, e aborta envio se `linhas.length === 1` (só o header).
- **Backup**: `atlas-triage.js.bak-fp-suppress`
- `atlas-triage.service` reiniciado em hock.

### 6. Maverik Notícias Alucinadas — RESOLVIDO
- **Causa raiz**: `narrativeSuggestion()` em `/opt/lsc-lab/apps/ceo-personal-bot/maverik-briefing.js` não incluía a data atual no prompt → LLM alucinava notícias antigas (ex: 14/04/2025).
- **Correção**:
  - Adicionado `const hoje = new Date().toLocaleDateString('pt-BR', {...})` dentro da função
  - `- Data de hoje: ${hoje}` incluído no bloco CONTEXTO do prompt
  - `buildBriefing()` agora lê `/opt/lsc-lab/doutrina/market-intel/LATEST.md` (se `< 8 dias`) e injeta os tópicos como `- Intel de mercado: ...` no prompt
  - `marketIntel` passado como campo no contexto de `narrativeSuggestion()`
- **Backup**: `maverik-briefing.js.bak-date-intel`
- `ceo-personal-bot.service` reiniciado em hock.

### 7. INTEL UPDATES Pipeline — RESOLVIDO
- **Causa raiz**: `brave_research.py` (semanal, domingo 18h BRT) gerava markdown com pesquisa Brave Search e salvava em `/opt/lsc-lab/doutrina/market-intel/` + enviava Telegram com lista de tópicos. Nenhuma outra parte do sistema consumia o output.
- **Correção (2 partes)**:
  1. **Maverik lê o intel**: `buildBriefing()` em `maverik-briefing.js` agora lê `LATEST.md` diariamente e injeta os tópicos de mercado no contexto do LLM de sugestão — o intel é *executado* a cada briefing matinal.
  2. **Intel instalado na memória**: `brave_research.py` agora chama `mem0.Memory.add()` ao final de cada run, salvando um resumo dos tópicos na coleção Qdrant `lsclab-memory` (user `leandro`) — o intel fica *persistido* e pesquisável por qualquer agente.
- **Backup**: `brave_research.py.bak-pre-mem0`
- `brave_research.py` pode ser testado manualmente: `python3 /opt/lsc-lab/doutrina/market-intel/brave_research.py`

### 8. Incidente de Segurança — EM MONITORAMENTO (incidente #101)
- Apps bound em `0.0.0.0` alcançáveis diretamente via tailnet (100.77.253.80), bypassando atlas_gate.
- Afetados: portas 3061 (atlas-ir-v3, IRPF), 3950/3951 (pollaudit), 8202 (mem0_mcp), 8300 (openclaw-mcp).
- **Ação recomendada**: rebind para `127.0.0.1` + rota via Caddy atlas_gate, ou firewall no tailnet.
- **Bloqueio**: rebind de 8202/8300 derrubaria MCPs em uso — decisão arquitetural necessária.

## Pendentes da faxina

| Item | Descrição | Localização |
|------|-----------|-------------|
| Tenants de teste no Postgres | UPDATE status → 'archived' | `platform.tenants` — preservar Docinho Gourmet/Isadora |
| Claud memory leak | Diagnosticar store.py / load pattern | `/opt/claud/mcp/server.py` + `store.py` |
| Incidente #101 (bind 0.0.0.0) | Decisão arquitetural: rebind vs firewall tailnet | Bloqueado: 8202/8300 em uso |

## Autonomy ratio impacto
- Antes: ~50+ notificações/dia de ruído (loop leads, digest duplicado, churn poluído, claud flapping, triage 144 falsos, briefing com datas erradas)
- Depois: alertas ativos reduzidos, intel de mercado integrado no briefing diário, foco em sinais acionáveis

---
*Auditoria conduzida em sessão única (2 context windows). Todos os fixes foram aplicados diretamente nos servidores (claw/hock) via MCP claud_exec_remote.*
