# War Games, Purple Team e validação defensiva

**Objetivo:** avaliar observabilidade, qualidade de investigação e processo de resposta do Blue Team com **eventos sintéticos, replay de logs autorizados e exercícios de mesa**. Nenhum exercício desta curadoria depende de exploração real.

| Prioridade | Repositório | O que pode ser aproveitado | Maturidade e ressalva |
|---|---|---|---|
| **A** | [purple-team-certification-lab](https://github.com/mrjmriii/purple-team-certification-lab) | Organização por fases, artefatos, scorecard e validação de regras Wazuh | Parcial segundo README; usar como design de rubricas, não certificação |
| **A** | [Wazuh SOC Enterprise](https://github.com/brunoflausino/wazuh-soc-enterprise) | Casos documentados com telemetria, regras, relatório e lacunas | Conferir evidências e reproduzir com datasets seguros |
| **B** | [SOC-Lab-02-Modular-Detection-Wazuh](https://github.com/Kamii-cxo/SOC-Lab-02-Modular-Detection-Wazuh) | Separação de módulos de detecção, checklist e evidências do laboratório | O README apresenta diversos cenários como **rascunhos**, não como catálogo validado |
| **B** | [tf-aws-purple-lab](https://github.com/trewwwsec/tf-aws-purple-lab) | Referência arquitetural de infraestrutura como código, telemetria e validação Wazuh | Consultar exclusivamente a arquitetura e avaliação defensiva; não executar atividades ofensivas |
| **B** | [detect-lab-ci](https://github.com/cybersagnik/detect-lab-ci) | Testes de detecções Sigma com fixtures EVTX, CI e visão ATT&CK | Pipeline direcionado a outros backends; adaptação Wazuh é trabalho próprio |
| **B** | [Wazuh Detection Rules Kit](https://github.com/KaanTuran28/Wazuh-Detection-Rules-Kit) | Lint, testes de regras e consultas de investigação | Confirmação de alerta exige Wazuh real e teste na ingestão |
| **B** | [incident-response-playbooks](https://github.com/iamahmedsalam/incident-response-playbooks) | Exemplos de decisões, investigação e retrospectiva de incidentes | Valor pedagógico; não validar ações operacionais com base apenas no relato |

## Modelo recomendado de exercício

```text
White Cell: define cenário fictício, objetivos, dados sintéticos e gabarito
  -> Preparação: parser, regra, queries e controle de versão
  -> Blue Cell: recebe evento/alerta e decide o fluxo investigativo
  -> Observação: registra timeline, evidências, lacunas e hipóteses
  -> Avaliação: compara esperado x observado, sem automatizar contenção
  -> After Action Review: converte lacunas em melhoria de detecção/runbook
```

## Template de cenário

```yaml
scenario_id: "WG-FIM-001"
name: "Investigação de alerta sintético de integridade"
mode: "tabletop-and-log-replay"
environment: "isolated-lab"
roles: ["white-cell", "blue-cell"]
telemetry_sources: ["fim", "agent-metadata"]
expected_observations:
  - "evento visível"
  - "parsing correto"
  - "evidence_id preservado"
  - "classificação justificada"
automation_policy: "no-live-containment"
success_criteria:
  - "hipótese documentada"
  - "timeline reproduzível"
  - "gap identificado ou explicitamente ausente"
```

## Escala de resultados

- **PASS:** evento observado, interpretação justificada e evidência preservada.
- **DEGRADED:** cobertura parcial, contexto ausente ou investigação inconclusiva.
- **FAIL:** evento esperado não coletado, não processado ou incorretamente interpretado.
- **NOT TESTED:** etapa não exercitada; **não** equivale a sucesso.

**Métricas de referência:** disponibilidade da telemetria, taxa de testes positivos/negativos, tempo de triagem **medido**, integridade das evidências, acurácia de decisões e problemas que viraram regressão. Não publicar porcentagem ATT&CK como se medisse probabilidade real de detecção.

Veja [mini-lab de Blue Team](../docs/trilhas.md#trilha-5--blue-team-war-game-de-mesa), [Detection-as-Code](detection-engineering.md) e [Incident Response](incident-response.md).
