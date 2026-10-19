# WAZUH FEATURE ATLAS
### Curadoria técnica de funcionalidades, projetos e integrações para Wazuh SIEM/XDR

> **Da funcionalidade ao caso de uso verificável.** Um índice independente, em português, de repositórios e materiais para estudar **threat hunting, CTI, incident response, DFIR, SOAR, detection engineering, war games defensivos, arquitetura e automação** com Wazuh.

[![Curadoria](https://img.shields.io/badge/tipo-curadoria%20t%C3%A9cnica-175CD3)](#como-usar)
[![Idioma](https://img.shields.io/badge/idioma-PT--BR-1565C0)](#índice)
[![Código externo](https://img.shields.io/badge/c%C3%B3digo%20de%20terceiros-n%C3%A3o%20incorporado-475467)](docs/metodologia.md)
[![Validação](https://img.shields.io/badge/execu%C3%A7%C3%A3o-n%C3%A3o%20atestada-F79009)](docs/metodologia.md)

## Por que este repositório existe?

Uma lista genérica de links não explica **qual funcionalidade usar, por que ela é útil, o que precisa ser validado e como ela se encaixa no ciclo SOC**. Este atlas separa projetos oficiais, bibliotecas de regras, aplicações, conectores, demonstrações e laboratórios. O objetivo é encontrar referências adequadas sem confundir uma prova de conceito com um produto pronto para produção.

**Escopo:** curadoria documental, matrizes de capacidades e trilhas de estudos. **Fora do escopo:** redistribuir código alheio, clonar stacks sem revisão, credenciais, sistemas vulneráveis públicos e instruções de exploração. Regras, exemplos e compatibilidade devem ser testados no ambiente autorizado antes da adoção.

## Índice

| Área | Pergunta respondida | Catálogo |
|---|---|---|
| **Funcionalidades Wazuh** | Quais recursos nativos existem e quais projetos os complementam? | [Matriz de funcionalidades](catalog/funcionalidades.md) |
| **Threat Hunting / DFIR** | Como transformar dados em hipóteses, pivôs e evidências? | [Hunting e forense](catalog/threat-hunting.md) |
| **CTI / Retro-Hunting** | Como enriquecer e pesquisar IOCs historicamente? | [Inteligência de ameaças](catalog/cti-retrohunting.md) |
| **Incident Response / SOAR** | Como conduzir triagem, casos, runbooks e automações supervisionadas? | [Resposta e orquestração](catalog/incident-response.md) |
| **War Games / Purple Validation** | Como medir observabilidade e resposta com eventos sintéticos? | [Exercícios e validação](catalog/war-games.md) |
| **Detection Engineering** | Como versionar e testar regras, decoders e queries? | [Detection-as-Code](catalog/detection-engineering.md) |
| **Plataforma / Automação / IA** | Como manter a infraestrutura e integrar copilotos com segurança? | [Arquitetura e operações](catalog/plataforma.md) |
| **Aprendizado guiado** | Em que ordem estudar e o que entregar? | [Trilhas e mini-labs](docs/trilhas.md) |
| **Proveniência e seleção** | Por que a referência entrou? Como interpretar as ressalvas? | [Metodologia](docs/metodologia.md) |
| **Inventário editável** | Como filtrar projetos por domínio, tipo e prioridade? | [CSV](catalog/repositorios.csv) |

## Comece pelos projetos de maior valor prático

| Referência | Tipo | Onde se destaca | Cuidado |
|---|---|---|---|
| [SOCFortress/Wazuh-Rules](https://github.com/socfortress/Wazuh-Rules) | Regras/decoders | Detection engineering | Risco de colisão de IDs; fazer backup e validar |
| [WAZUH Process Tree Viewer](https://github.com/mym0us3r/WAZUH-Process-Tree-Viewer) | Aplicação | Hunting de processos Windows | Exige telemetria e versão compatível |
| [Wazuh-TI](https://github.com/federicofantini/Wazuh-TI) | Integração CTI | OpenCTI/TAXII + retro-hunting | Limites de consulta, autenticação e licença |
| [Hotwash](https://github.com/lidless-labs/hotwash) | Aplicação | Runbooks executáveis / IR | Projeto WIP; integrações SOAR em evolução |
| [Wazuh Detection Rules Kit](https://github.com/KaanTuran28/Wazuh-Detection-Rules-Kit) | Regras/testes | Lint, simulação e queries de hunting | Simulador isolado não substitui Wazuh real |
| [Purple Team Certification Lab](https://github.com/mrjmriii/purple-team-certification-lab) | Laboratório | Scoring e exercícios defensivos | Implementação parcial; validar escopo |
| [Wazuh SOC Enterprise](https://github.com/brunoflausino/wazuh-soc-enterprise) | Laboratório/documentação | Evidência, regras e integração SOC | Diferenciar resultados documentados de testes próprios |
| [Wazuh MCP Server](https://github.com/socfortress/wazuh-mcp-server) | Conector de IA | Consulta assistida a Wazuh | Restringir ferramentas de escrita e credenciais |

## Como usar

1. Encontre a **funcionalidade nativa** em [catalog/funcionalidades.md](catalog/funcionalidades.md).
2. Entre na área correspondente e compare **o que o repositório entrega**: código, configuração, laboratório ou apenas documentação.
3. Consulte a fonte original, versão, condições de uso e licença. Links não significam endosso.
4. Estude o fluxo defensivo com dados sintéticos e valide parser, regra, alerta, investigação e evidências.
5. Registre resultados e lacunas antes de recomendar adoção.

## Princípios

- **Existir no GitHub ≠ funcionar em produção.** Os links e READMEs foram conferidos em 19/10/2026, mas os projetos externos **não foram executados nesta curadoria**.
- **Evidência antes de automação.** Respostas com efeito sobre agentes, hosts ou identidades devem exigir revisão e autorização.
- **Proveniência primeiro.** Cada ferramenta conserva o link do mantenedor. Não há código de terceiros incorporado.
- **Escopo defensivo.** War games priorizam tabletop, replay de logs, eventos sintéticos e avaliação de Blue Team.
- **Compatibilidade é específica.** Wazuh, OpenSearch, versões de plugins, formatos XML, DSL e Sigma precisam de testes próprios.
- **Curadoria ≠ repositório oficial Wazuh.** Para o código-fonte e a documentação primária, veja [wazuh/wazuh](https://github.com/wazuh/wazuh), [documentação oficial](https://documentation.wazuh.com/current/) e [wazuh/integrations](https://github.com/wazuh/integrations).

## Contribuições

Sugestões devem informar link, finalidade, artefatos efetivamente presentes, licença, versão, manutenção, testes reproduzíveis, limitações e domínio. O checklist está em [docs/metodologia.md](docs/metodologia.md). **Não enviar segredos, IOCs privados, dados pessoais ou arquivos maliciosos.**

---

*Atlas comunitário independente, sem afiliação ou endosso oficial da Wazuh ou dos mantenedores externos. Última triagem documental: 19 de outubro de 2026.*
