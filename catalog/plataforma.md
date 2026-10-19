# Plataforma, arquitetura, automação e IA

**Objetivo:** dimensionar, implantar, observar e evoluir a stack Wazuh sem confundir componentes oficiais, produtos de terceiros e laboratórios comunitários.

## Referências oficiais

| Prioridade | Fonte | Principal uso |
|---|---|---|
| **A** | [wazuh/wazuh](https://github.com/wazuh/wazuh) | Código-fonte, componentes nativos, documentação de implementação |
| **A** | [wazuh/wazuh-docker](https://github.com/wazuh/wazuh-docker) | Deploy Docker Compose, ambientes reproduzíveis e topologias de nó único/múltiplos |
| **A** | [wazuh/wazuh-kubernetes](https://github.com/wazuh/wazuh-kubernetes) | Orquestração Kubernetes e arquitetura distribuída |
| **A** | [wazuh/wazuh-ansible](https://github.com/wazuh/wazuh-ansible) | Automação de provisionamento e configuração |
| **A** | [wazuh/integrations](https://github.com/wazuh/integrations) | Coleção de contribuições e referências de integração |
| **C** | [wazuh/wazuh-ruleset](https://github.com/wazuh/wazuh-ruleset) | Referência histórica **arquivada**; usar rulesets do repositório principal |

## Benchmarks comunitários

| Prioridade | Projeto | O que documenta/implementa | Uso mais indicado |
|---|---|---|---|
| **A** | [siem-docker-stack](https://github.com/ChiefGyk3D/siem-docker-stack) | Stack Docker abrangente, indexação hot/warm, Grafana/Prometheus, cache e automações n8n | Referência para operação, retenção e observabilidade; ativo e sujeito a mudanças |
| **A** | [wazuh-docker-monitoring-platform](https://github.com/GiulioSavini/wazuh-docker-monitoring-platform) | Docker, Ansible, rulesets cloud e health checks | Benchmark de configuração, onboarding e infraestrutura |
| **A** | [SOCFortress CoPilot](https://github.com/socfortress/CoPilot) | Aplicação SOC com frontend, backend e conectores Wazuh e ferramentas correlatas | UX e orquestração de serviços SOC; revisar maturidade e licenciamento |
| **A** | [SOCFortress wazuh-mcp-server](https://github.com/socfortress/wazuh-mcp-server) | Interface MCP para explorar a API Wazuh, incluindo controles de categorias de ferramentas | Benchmark para assistente **read-only**; desabilitar operações perigosas |
| **B** | [Wazuh SOC Enterprise](https://github.com/brunoflausino/wazuh-soc-enterprise) | Laboratório de engenharia de detecção e integração de múltiplos componentes | Casos, documentação, telemetria e arquitetura de referência |
| **B** | [Enterprise Azure Wazuh SOC Lab](https://github.com/waisyrr/Enterprise-Azure-Wazuh-SIEM-SOAR-Security-Operations-Lab) | Integração Azure/AD, Wazuh, automações e relatórios | Estudo de caso, não modelo pronto de produção |
| **B** | [MakaraSOC](https://github.com/socarium/makarasoc) | Stack Wazuh + DFIR-IRIS + CTI + SOAR | Comparação de arquitetura de ferramentas |
| **B** | [SOC Automation Lab](https://github.com/zionsworking/soc-automation-lab) | Compose e workflows Wazuh/Shuffle/TheHive | Referência modular de laboratório |

## Princípios arquiteturais

```text
Agentes / coletores externos / APIs
      -> Wazuh manager / regras / decoders
      -> indexer / políticas de retenção
      -> Dashboard / hunting / detecção
      -> enriquecimento / casos / automação supervisionada
      -> métricas, backups, testes, revisão humana
```

Checklist para propostas de implantação:

- Dimensionamento de ingestão/eventos, espaço em disco, indexação e retenção.
- Criptografia em trânsito, RBAC, certificados e credenciais via secret manager.
- Observabilidade da stack (saúde de agentes, manager, indexer, filas e armazenamento).
- Políticas de backup/restore **testadas** e plano de rollback.
- Fixação de versões, inventário de dependências, SBOM e revisão de licenças.
- Segregação entre ambientes de estudo e produção.
- Para IA, ferramentas **somente leitura** primeiro, lista explícita de capacidades, logs de auditoria, proteção contra prompt injection contida em eventos e revisão de evidências.

## Produto / PoC / framework

Um número elevado de conectores não torna um projeto automaticamente seguro, eficiente ou pronto para operação. Classificar cada benchmark separadamente: **diagrama**, **configuração**, **artefato executável**, **integração demonstrada** ou **validação independente**.

**Trilha:** [arquitetura e confiabilidade](../docs/trilhas.md#trilha-6--arquitetura-e-confiabilidade). **Funcionalidades nativas:** [matriz](funcionalidades.md).
