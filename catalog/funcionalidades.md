# Matriz de funcionalidades Wazuh

Uma visão orientada a **capacidades**, distinguindo recurso da plataforma, integrações adicionais e estudos de caso.

| Capacidade | Nativa no Wazuh? | O que observar | Curadoria associada |
|---|---|---|---|
| Agentes e inventário (**Syscollector**) | Sim | Estado de software, processos e ativos | [Plataforma](plataforma.md) |
| **FIM / syscheck** | Sim | Integridade, origem e enriquecimento de eventos | [Detection](detection-engineering.md) · [IR](incident-response.md) |
| **SCA** (avaliação de configuração) | Sim | Políticas, compliance e desvios | [Plataforma](plataforma.md) |
| Detecção de vulnerabilidades | Sim, depende de feeds e configuração | Qualidade de inventário, matching e escopo | [Plataforma](plataforma.md) |
| **Logcollector / Syslog** | Sim | Cobertura, perda de eventos e parsing | [Detection](detection-engineering.md) |
| **Decoders / Ruleset XML** | Sim | Normalização, regras, precedência, IDs | [Detection](detection-engineering.md) |
| **wazuh-logtest** | Sim | Testes de parser e regra | [Detection](detection-engineering.md) |
| **Active Response** | Sim | Controles, autorizações, logs e rollback | [IR](incident-response.md) |
| **Wazuh Indexer / Dashboard** | Componentes da stack | Consultas, janela temporal, índices e desempenho | [Hunting](threat-hunting.md) |
| **Threat Hunting** | Fluxos de consulta e investigação | Queries, hipóteses, timelines, evidências | [Hunting](threat-hunting.md) |
| **Cloud/identity telemetry** | Coletores/módulos e integrações | AWS/Azure/GCP/Office 365, cobertura e normalização | [Plataforma](plataforma.md) |
| **Suricata / Zeek / Sysmon** | **Ferramentas externas** integradas via telemetria | Campos, regras e correlação multi-fonte | [Detection](detection-engineering.md) |
| **MISP / OpenCTI / STIX / TAXII** | **Integrações externas** | Proveniência, confiança e validade dos IOCs | [CTI](cti-retrohunting.md) |
| **Retro-hunting de IOCs** | Workflow construído sobre dados indexados | Janela histórica, limites, deduplicação | [CTI](cti-retrohunting.md) |
| **DFIR-IRIS / TheHive / Velociraptor** | **Ferramentas externas** | Casos, coleta de evidência e cadeia investigativa | [IR](incident-response.md) |
| **Shuffle / n8n** | **SOAR externo** | Aprovação, idempotência, acesso e rollback | [IR](incident-response.md) |
| **MCP e assistentes de IA** | **Integração externa** | Somente leitura primeiro, auditoria e grounding | [Plataforma](plataforma.md) |
| **War games / BAS / Purple** | Metodologias de validação externas | Replay sintético, detecção, decisões e score | [War Games](war-games.md) |

## Da capacidade à evidência

```text
Objetivo / hipótese
  -> fonte e evento esperado
  -> agente/coletor e parser
  -> regra, query ou correlação
  -> investigação e evidências
  -> decisão supervisionada
  -> teste de regressão e lacuna documentada
```

## Referências primárias

- [Código-fonte Wazuh](https://github.com/wazuh/wazuh)
- [Integrações da comunidade](https://github.com/wazuh/integrations)
- [Documentação oficial](https://documentation.wazuh.com/current/)
- [Docker oficial](https://github.com/wazuh/wazuh-docker)
- [Kubernetes oficial](https://github.com/wazuh/wazuh-kubernetes)
- [Ansible oficial](https://github.com/wazuh/wazuh-ansible)

> “Sim” indica que a capacidade faz parte do ecossistema Wazuh, **não** que esteja habilitada, suportada por qualquer versão ou apta a funcionar sem configuração. Para implantação, confira a documentação da versão exata.
