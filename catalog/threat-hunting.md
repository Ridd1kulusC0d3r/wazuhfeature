# Threat Hunting e DFIR

**Objetivo:** gerar hipóteses, formular consultas reprodutíveis, investigar relações entre eventos e documentar lacunas de telemetria. O Wazuh fornece dados e capacidades de consulta; ferramentas externas ampliam visualizações e procedimentos.

| Prioridade | Projeto / fonte | Artefato e valor específico | Limite ou cuidado |
|---|---|---|---|
| **A** | [WAZUH Process Tree Viewer (WPTV)](https://github.com/mym0us3r/WAZUH-Process-Tree-Viewer) | Aplicação que reconstrói árvores de processos Windows a partir de eventos Security/Sysmon; inclui camada opcional de análise assistida | Exige eventos de processo, agente Windows e compatibilidade de plugin/OpenSearch explicitada no README |
| **A** | [Advanced_Wazuh_Queries](https://github.com/nwclasantha/Advanced_Wazuh_Queries) | Guia de consultas Wazuh 4.11.2; exploração de filtros, tempo, agentes e severidade | Diferenciar consulta de Dashboard/Discover das APIs DSL; conferir campos na versão de uso |
| **A** | [Wazuh Detection Rules Kit](https://github.com/KaanTuran28/Wazuh-Detection-Rules-Kit) | Regras XML, validador e consultas OpenSearch Query DSL para hunting | Linter/simulador isolado não substitui validação real no Wazuh |
| **B** | [Threat-Hunting (Aruns-itsme)](https://github.com/Aruns-itsme/Threat-Hunting) | Guias, playbooks, queries e exemplos de evidências | Material de estudo, não pacote único compatível com Wazuh |
| **B** | [Velociraptor DFIR + Wazuh Lab](https://github.com/samsonejim/velociraptor-dfir-wazuh-lab) | Estudo de caso de coleta forense e investigação com integração Wazuh em GCP | Exige ambiente de laboratório e revisar controles de coleta e autorização |
| **B** | [Enterprise Azure Wazuh SOC Lab](https://github.com/waisyrr/Enterprise-Azure-Wazuh-SIEM-SOAR-Security-Operations-Lab) | Procedimentos de hunting, correlação, alertas e relatórios em ambiente Azure | Resultados numéricos descritos são alegações do autor, não métricas auditadas aqui |
| **C** | [Wazuh XDR, SOAR & TI Lab](https://github.com/0xcgz/threat-intelligence-threat-hunting-wazuh) | Demonstração de hunting integrado ao enriquecimento SOAR/CTI | Predominantemente demonstração e documentação, não catálogo de queries pronto |

## Referências por problema

### Reconstrução de processos

Usar [WPTV](https://github.com/mym0us3r/WAZUH-Process-Tree-Viewer) como referência de navegação por relações `parent→child`, preservando **identificador do evento, host, identidade, timestamp e origem**. Não inferir causalidade somente pela aparência da árvore. O README do projeto destaca versões específicas do Wazuh e OpenSearch Dashboards, que devem ser conferidas antes de instalar plugins.

### Biblioteca de consultas

De cada query escolhida, extrair uma **ficha técnica**, não simplesmente copiar uma expressão:

```yaml
id: HUNT-DEMO-001
hypothesis: "Sequência incomum de processos em endpoint de teste"
source: "Windows Security / Sysmon"
query_engine: "OpenSearch Query DSL"
required_fields: ["agent.name", "@timestamp"]
time_window: "definida no estudo"
expected_evidence: ["event_id", "host", "timestamp"]
limitations: ["depende do pipeline de normalização"]
```

Campos ilustrativos: validar nomes reais no índice local.

### Encerramento de hunting

Todo hunt deve resultar em **finding / benign / inconclusive / telemetry gap**, com links para consultas, evidências e proposta de melhoria. Uma lista de queries sem hipótese e sem fechamento não é uma biblioteca profissional de hunting.

**Laboratório proposto:** [trilha de hunting com logs sintéticos](../docs/trilhas.md#trilha-2--hunting-por-hipótese). Consulte também [CTI retro-hunting](cti-retrohunting.md) e [Detection Engineering](detection-engineering.md).
