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

### 5. Incidente de Segurança — EM MONITORAMENTO (incidente #101)
- Apps bound em `0.0.0.0` alcançáveis diretamente via tailnet (100.77.253.80), bypassando atlas_gate.
- Afetados: portas 3061 (atlas-ir-v3, IRPF), 3950/3951 (pollaudit), 8202 (mem0_mcp), 8300 (openclaw-mcp).
- **Ação recomendada**: rebind para `127.0.0.1` + rota via Caddy atlas_gate, ou firewall no tailnet.
- **Bloqueio**: rebind de 8202/8300 derrubaria MCPs em uso — decisão arquitetural necessária.

## Pendentes da faxina

| Item | Descrição | Localização |
|------|-----------|-------------|
| Maverik notícias alucinadas | Digest com news de 14/04/2025 | `ATLAS_FLOW/api/briefing` → `maverik-proactive.js` (hock) |
| Triage "144 falsos" | Digest 100% falso-positivo a cada 4h | Timer não localizado — verificar hock |
| INTEL UPDATES | Verificar funcionamento | `brave_research.py` semanal (domingo 18h BRT) — parece OK |
| Tenants de teste no Postgres | UPDATE status → 'archived' | `platform.tenants` — preservar Docinho Gourmet/Isadora |
| Claud memory leak | Diagnosticar store.py / load pattern | `/opt/claud/mcp/server.py` + `store.py` |

## Autonomy ratio impacto
- Antes: ~50+ notificações/dia de ruído (loop leads, digest duplicado, churn poluído, claud flapping)
- Depois: alertas ativos reduzidos, foco em sinais acionáveis

---
*Auditoria conduzida em sessão única. Todos os fixes foram aplicados diretamente nos servidores (claw/hock) via MCP claud_exec_remote.*
