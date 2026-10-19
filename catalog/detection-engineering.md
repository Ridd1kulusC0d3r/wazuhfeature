# Detection Engineering, regras, decoders e queries

**Objetivo:** construir detecções Wazuh reproduzíveis e identificar o que pertence ao parser, à regra nativa XML, ao indexador e à camada de hunting.

| Prioridade | Repositório | Componentes / referência | Ressalva |
|---|---|---|---|
| **A** | [SOCFortress/Wazuh-Rules](https://github.com/socfortress/Wazuh-Rules) | Regras, decoders e integrações para múltiplas fontes de telemetria | Verificar IDs existentes: a importação sem validação pode impedir inicialização do manager |
| **A** | [wazuh/integrations](https://github.com/wazuh/integrations) | Referências comunitárias para rules, decoders, active response, dashboards e outros | Repositório da organização Wazuh, mas contribuições não significam suporte garantido |
| **A** | [Wazuh Detection Rules Kit](https://github.com/KaanTuran28/Wazuh-Detection-Rules-Kit) | Regras XML, linter/simulador e queries OpenSearch DSL | Testes isolados não substituem `wazuh-logtest` e ingestão |
| **B** | [sigma-wazuh-converter](https://github.com/jeamf/sigma-wazuh-converter) | Pipeline de conversão Sigma → XML Wazuh e testes | Revisar mapeamento, condições complexas e unicidade de IDs |
| **B** | [detect-lab-ci](https://github.com/cybersagnik/detect-lab-ci) | Benchmark adjacente de CI com Sigma e eventos EVTX | Focado em outros destinos de query; portar lógica e fixtures, não a saída pronta |
| **B** | [Wazuh SOC Enterprise](https://github.com/brunoflausino/wazuh-soc-enterprise) | Regras customizadas, integrações e documentação de testes/casos | Garantir contrato e testes para cada regra selecionada |
| **B** | [Advanced_Wazuh_Queries](https://github.com/nwclasantha/Advanced_Wazuh_Queries) | Consultas e documentação para hunting em Wazuh 4.11.2 | Sintaxe depende da interface de pesquisa |
| **C** | [sigma-rules (Hatchepsoute)](https://github.com/Hatchepsoute/sigma-rules) | Material adjacente sobre Sigma e consultas OpenSearch | Não é implementação direta de regras Wazuh XML |
| **A (oficial)** | [wazuh/wazuh](https://github.com/wazuh/wazuh) | Código da plataforma e árvore atual de rulesets | Fonte primária, conferir branch/tag |
| **C (histórico)** | [wazuh/wazuh-ruleset](https://github.com/wazuh/wazuh-ruleset) | Repositório de rulesets antigo | **Arquivado**: não escolher como baseline de conteúdo atual |

## Distinguir as quatro superfícies

| Camada | Tipo | Responsabilidade |
|---|---|---|
| **Decoder** | XML do Wazuh | Extrair/normalizar campos dos eventos |
| **Regra nativa** | XML do Wazuh | Classificar e correlacionar eventos no motor de análise |
| **Query de hunting** | DQL, OpenSearch Query DSL ou outra interface documentada | Explorar dados indexados retrospectivamente |
| **Sigma** | Formato portável de detecção | Especificar comportamento de modo independente de backend; requer tradução/validação |

**Não confundir** teste de regex, regra Wazuh, consulta de indexador e tradução Sigma. Resultados podem divergir mesmo quando a intenção analítica é semelhante.

## Contrato de detecção recomendado

```yaml
id: DET-DEMO-001
title: "Alteração de arquivo em laboratório"
category: "fim"
owner: "blue-team-lab"
telemetry:
  source: "Wazuh FIM"
  fields: ["agent.name", "rule.id"]
detection:
  implementation: "Wazuh XML"
  rule_id: "a-definir-sem-conflitos"
tests:
  positive_fixture: "fixture sintética A"
  negative_fixture: "fixture sintética B"
  wazuh_logtest: "pending"
decision:
  runbook: "../incident-response.md"
  production_approved: false
```

Campos e nomes são ilustrativos: validar todos os IDs e campos na revisão de Wazuh usada.

## Critérios de aceitação

- [ ] Definir comportamento observável e fonte que realmente o coleta.
- [ ] Provar parsing e correspondência positiva e negativa.
- [ ] Validar ID de regra único e sem sobreposição não intencional.
- [ ] Conferir dependências, precedência, `if_sid` e efeitos de correlação.
- [ ] Testar a detecção no `wazuh-logtest` e, se aplicável, na cadeia de ingestão real de laboratório.
- [ ] Registrar falsos positivos, limitações, proprietário e plano de rollback.
- [ ] Vincular a regra a um hunt, caso de uso, runbook e regressão.

Para exercícios práticos, veja [trilha Detection Engineering](../docs/trilhas.md#trilha-1--detection-engineering) e [War Games](war-games.md).
