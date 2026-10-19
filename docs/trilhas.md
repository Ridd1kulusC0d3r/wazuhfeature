# Trilhas guiadas e mini-labs defensivos

A proposta é aprender Wazuh em **etapas verificáveis**, sem instalar um ecossistema inteiro antes de compreender o caminho dos dados. Os exercícios abaixo são seguros para laboratório com telemetria **sintética** e ambiente autorizado. Evite dados reais de terceiros.

## Trilha 1 — Detection Engineering

**Meta:** de uma linha de evento fictícia até uma regra XML testada.

1. Documentar fonte, campos esperados e comportamento que se pretende identificar.
2. Criar fixture JSON/texto benigna com variações positivas e negativas.
3. Inspecionar parser e regras com `wazuh-logtest` em laboratório.
4. Conferir o ID único, mensagem, nível, falsos positivos e observáveis.
5. Registrar evidências, alterações e um teste de regressão.

**Entregáveis:** contrato de detecção, fixtures, regra comentada, resultado de teste e revisão por par. [Referências](../catalog/detection-engineering.md).

## Trilha 2 — Hunting por hipótese

**Meta:** investigar uma sequência fictícia de criação de processos e autenticação.

1. Definir hipótese e fontes (Sysmon/Windows, quando disponíveis).
2. Montar dataset sintético com timestamp, host, usuário, processo pai/filho.
3. Executar consultas documentando se são DQL, OpenSearch DSL ou outro mecanismo.
4. Construir timeline ou árvore, relacionando cada observação ao ID do evento.
5. Registrar `finding`, `benign`, `inconclusive` ou `telemetry gap`.

**Entregáveis:** hipótese, consultas, cadeia de evidências e proposta de detecção. [Referências](../catalog/threat-hunting.md).

## Trilha 3 — CTI e retro-hunting

**Meta:** verificar retrospectivamente um IOC **fictício de documentação** em logs sintéticos.

1. Criar registro de IOC com tipo, origem fictícia, confiança e validade temporal.
2. Simular coleção pequena de eventos em janela definida.
3. Consultar correspondências históricas com limites de tempo e volume.
4. Registrar coincidências, contexto, falsos positivos e expiração do IOC.
5. Não transformar coincidência em incidente automaticamente.

**Entregáveis:** schema de IOC, registro de busca, achados e critérios de descarte. [Referências](../catalog/cti-retrohunting.md).

## Trilha 4 — IR guiado por runbook

**Meta:** responder a um alerta **sintético** de integridade de arquivo.

1. Abrir um caso de treinamento; não acionar contenção.
2. Classificar severidade, impacto, contexto e nível de confiança.
3. Registrar evidências, responsáveis, decisões e checkpoints.
4. Redigir recomendação de contenção sujeita a aprovação humana.
5. Fechar o caso com relatório pós-incidente e melhoria de regra.

**Entregáveis:** ficha de caso, timeline, runbook preenchido, relatório e ação de melhoria. [Referências](../catalog/incident-response.md).

## Trilha 5 — Blue Team War Game de mesa

**Meta:** medir investigação, comunicação e lacunas sem executar técnicas ofensivas.

1. White Cell define cenário fictício, escopo, dados e critérios.
2. Blue Cell recebe alertas e logs sintéticos em rodadas.
3. A equipe registra consultas, hipóteses, decisões e justificativas.
4. Facilitador compara eventos previstos versus observados.
5. Scorecard avalia **qualidade de evidência, interpretação, comunicação, decisões e melhorias**.

**Entregáveis:** pacote de eventos, anotações, scorecard, AAR (*after-action review*) e backlog. [Referências](../catalog/war-games.md).

## Scorecard sugerido

| Dimensão | Peso | Exemplo de critério |
|---|---:|---|
| Telemetria e observabilidade | 20% | Eventos esperados realmente disponíveis |
| Interpretação contextual | 25% | Hipóteses sustentadas por IDs de evidência |
| Qualidade de investigação | 25% | Linha do tempo e explicação reproduzíveis |
| Decisão e comunicação | 15% | Priorização e justificativa claras |
| Melhoria contínua | 15% | Lacuna convertida em teste/backlog |

**Não confundir:** esse score é uma rubrica didática, não uma medição validada de taxa real de detecção (recall/precision) ou do nível de segurança organizacional.

## Trilha 6 — Arquitetura e confiabilidade

**Meta:** desenhar uma implantação sustentável, mesmo sem fazer o deploy.

- Modelar fluxo de coleta, indexação, dashboards, disponibilidade, backup e retenção.
- Documentar RBAC, segmentação, certificados e observabilidade da própria stack.
- Registrar cenários de falha e recuperação com testes **não destrutivos**.
- Verificar licenças, suporte e requisitos de recursos de cada solução externa.

**Entregável:** diagrama, ADR (decisão arquitetural), checklist de implantação e critérios de aceitação. [Referências](../catalog/plataforma.md).

---

**Definition of Done transversal:** não afirmar que uma função “funciona” sem registrar ambiente, versão, fixture, comando/procedimento, saída observada, resultado esperado e limitações.
