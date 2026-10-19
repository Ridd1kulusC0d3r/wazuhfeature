# Incident Response, DFIR e SOAR

**Objetivo:** converter sinais de segurança em **casos**, evidências, decisões e melhorias, preservando auditoria e limites de automação.

| Prioridade | Projeto | Capacidade útil | Limite e critério de adoção |
|---|---|---|---|
| **A** | [Hotwash](https://github.com/lidless-labs/hotwash) | Parse de playbooks Markdown/Mermaid em fluxos visuais; execução com responsáveis, notas, evidências e integração Wazuh/MCP | WIP: ações SOAR parciais; exige revisão de permissões, fluxos e HMAC |
| **A** | [Wazuh-IRIS-integration](https://github.com/nateuribe/Wazuh-IRIS-integration) | Envio de alertas Wazuh ao DFIR-IRIS para criação de casos | Autor recomenda documentação oficial mais recente; não replicar `verify=False` como padrão |
| **A** | [shuffle-soc-automation](https://github.com/heraclescap/shuffle-soc-automation) | Workflows de ingestão de alertas, normalização, enriquecimento e ticket IRIS | Requer controle de payload, segredos, retries, aprovação e tratamento de falhas |
| **B** | [MakaraSOC](https://github.com/socarium/makarasoc) | Arquitetura modular de Wazuh, DFIR-IRIS, Shuffle, Velociraptor, MISP e OpenCTI | Integração ampla ≠ maturidade validada; revisar requisitos, código e manutenção |
| **B** | [SOC Automation Lab](https://github.com/zionsworking/soc-automation-lab) | Docker, regras e ponte Wazuh/Shuffle/TheHive | Revisar versões, autenticação, exposição de portas e compatibilidade |
| **B** | [incident-response-playbooks](https://github.com/iamahmedsalam/incident-response-playbooks) | Playbooks, exercícios e relatos de detecção/investigação | Predominantemente material didático, não automação implantável |
| **B** | [SOCFortress CoPilot](https://github.com/socfortress/CoPilot) | Frontend/backend SOC e conectores Wazuh/Velociraptor/Graylog/Grafana | Aplicação maior, deve ser avaliada separadamente por módulo e licença |
| **B** | [Enterprise Azure Wazuh SOC Lab](https://github.com/waisyrr/Enterprise-Azure-Wazuh-SIEM-SOAR-Security-Operations-Lab) | Triagem, aprovação humana, enriquecimento, evidências e relatórios | Caso de estudo em Azure, não baseline genérica de produção |
| **B** | [Velociraptor DFIR + Wazuh Lab](https://github.com/samsonejim/velociraptor-dfir-wazuh-lab) | Workflow de coleta/inspeção forense e investigação | A coleta em endpoints precisa ser autorizada e auditada |
| **A (oficial)** | [Guia Wazuh + DFIR-IRIS](https://wazuh.com/blog/enhancing-incident-response-with-wazuh-and-dfir-iris-integration/) | Referência de integração publicada pela Wazuh | Conferir data, versões e requisitos atuais |

## Contrato mínimo de caso

```yaml
case_id: "IR-DEMO-001"
origin: "alerta sintético"
alert_ids: []
owner: "analista designado"
triage_status: "new"
severity: "undetermined"
decision: "pending-human-review"
evidence_ids: []
response_actions: []
approval_required: true
audit_log: []
```

## Guardrails para automação

- **Nível 0:** coletar logs, enriquecer e sugerir classificação (read-only).
- **Nível 1:** abrir/atualizar rascunho de caso com trilha de auditoria e antideduplicação.
- **Nível 2:** propor uma ação de resposta para **aprovação humana**, com avaliação de impacto.
- **Nível 3:** executar somente ações previamente aprovadas, autorizadas, restritas em escopo, com logging e procedimento de reversão.

Nenhum repositório desta curadoria recebe autorização para executar ações em sistemas reais. Validação inicial somente com dados sintéticos.

## Ciclo de investigação

```text
Wazuh alert -> enriquecimento -> triagem -> caso
       -> hipóteses -> evidências -> decisão
       -> resposta supervisionada -> postmortem
       -> alteração versionada em detecção / runbook / teste
```

**Laboratório:** [IR guiado por runbook](../docs/trilhas.md#trilha-4--ir-guiado-por-runbook). **Relacionados:** [Hunting](threat-hunting.md) e [CTI](cti-retrohunting.md).
