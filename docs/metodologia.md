# Metodologia de curadoria

> Critérios de seleção, confiança e adoção. Triagem documental em **19/10/2026**.

## O que foi efetivamente verificado

- O repositório de destino estava vazio; esta curadoria foi criada sem sobrescrever código preexistente.
- A **existência dos links GitHub** listados no inventário foi conferida via consulta ao repositório.
- Os **READMEs dos principais projetos comunitários** e dos projetos oficiais de implantação foram examinados para identificar proposta, tipo de artefato, limites e ressalvas.
- **Não foram executadas, compiladas ou testadas as ferramentas externas**. Não foram medidas taxas de detecção, falsos positivos, latência ou estabilidade.
- A curadoria **não copia código, regras, imagens, configurações ou datasets externos**. Somente contém atribuição, síntese e links para as fontes. Antes de reutilizar código, consultar licenças e dependências do projeto em sua revisão específica.

## Critério de entrada

1. **Relevância ao Wazuh**: funcionalidades nativas, integração efetiva ou benchmark adjacente com contribuição explícita para SOC.
2. **Evidência de artefato**: repositório real com README, código, regras, queries, playbooks, arquivos de infraestrutura ou documentação metodológica identificável.
3. **Utilidade para analistas**: deve responder a um caso de uso concreto, preferencialmente com validação/inspeção de evidência.
4. **Distinção entre fato e intenção**: recursos em roadmap, rascunhos e resultados declarados pelo autor não são tratados como capacidades validadas.
5. **Segurança e responsabilidade**: priorizar coleta autorizada, investigação, resposta supervisionada, exercícios de mesa e replay de logs sintéticos.

## Etiquetas

| Campo | Interpretação |
|---|---|
| **A / essencial** | Fonte primária, biblioteca central ou referência de alto valor no domínio |
| **B / complementar** | Ajuda a expandir um fluxo existente ou traz outra abordagem |
| **C / contextual** | Estudo de caso, recurso adjacente, documentação ou material menos maduro |
| **Código** | Oferece implementação ou scripts de interesse; **não atesta funcionamento** |
| **Configuração** | Contém exemplos de rulesets, integrações, workflows ou infraestrutura |
| **Lab** | Ambiente/procedimento de laboratório, com escopo a conferir |
| **Guia** | Conteúdo primordialmente explicativo |
| **Oficial** | Repositório publicado pela organização Wazuh (não implica suporte permanente) |
| **Arquivo** | Projeto arquivado; referência histórica, não baseline recomendada |

**Sinal de verificação:** `repo_confirmado_readme` significa que existência e descrição do README foram conferidas; `repo_confirmado` significa que a existência foi confirmada e as demais alegações exigem revisão. Nenhuma dessas etiquetas significa “testado em produção”.

## Checklist antes de adotar

- [ ] Registrar commit/tag e versão do Wazuh, OpenSearch, plugin, SOAR ou ferramenta externa.
- [ ] Validar licença, dependências, provenance e integridade dos artefatos.
- [ ] Testar em ambiente segregado e com **logs/fixtures sintéticos ou autorizados**.
- [ ] Inspecionar variáveis de ambiente, tokens, permissões, webhooks e TLS.
- [ ] Confirmar IDs de regras únicos, mapeamento de campos, decoders e erros no `wazuh-logtest`.
- [ ] Preparar testes positivos **e negativos** e conferir o resultado na cadeia real.
- [ ] Aplicar RBAC, aprovação, limites de consulta, deduplicação, retenção e rollback.
- [ ] Documentar evidências, métricas e casos em que o resultado foi inconclusivo.

## Alertas descobertos durante a triagem

- [SOCFortress/Wazuh-Rules](https://github.com/socfortress/Wazuh-Rules) avisa que importar regras em lote pode produzir **colisões de IDs** e falha do manager.
- [WAZUH Process Tree Viewer](https://github.com/mym0us3r/WAZUH-Process-Tree-Viewer) documenta versões de plugin/OpenSearch específicas, portanto a compatibilidade não deve ser presumida.
- [Hotwash](https://github.com/lidless-labs/hotwash) identifica-se como **WIP**; parte das ações SOAR ainda é template.
- [Wazuh-TI](https://github.com/federicofantini/Wazuh-TI) prevê controles e limites de retro-hunting que devem ser ajustados à infraestrutura; revisar autenticação e condições de exportação.
- [Wazuh-IRIS-integration](https://github.com/nateuribe/Wazuh-IRIS-integration) aponta para documentação oficial mais recente e contém exemplo que desativa verificação TLS para certificados autoassinados. **Não usar essa opção como baseline**; configurar certificados confiáveis.
- [sigma-wazuh-converter](https://github.com/jeamf/sigma-wazuh-converter) exige revisão de semântica, IDs e condições antes de colocar regras convertidas em produção.
- [wazuh-ruleset](https://github.com/wazuh/wazuh-ruleset) está **arquivado**. Preferir a árvore de rulesets em [wazuh/wazuh](https://github.com/wazuh/wazuh).
- Catálogos de queries para **Dashboard/DQL**, **OpenSearch Query DSL**, **Sigma** e **regras Wazuh XML** têm sintaxes e objetivos diferentes. Não efetuar conversão por simples substituição textual.

## Fora do escopo desta primeira edição

- Qualquer importação automática de projetos de terceiros, execução de instaladores não revisados, distribuição de credenciais e reprodução de ações ofensivas.
- Afirmações sobre estrelas, taxa de detecção, manutenção futura ou capacidade de produção sem medições auditáveis.
- Coleções genéricas que não contribuam diretamente para entendimento das funcionalidades ou para o fluxo de trabalho do analista.

## Como propor uma referência

Usar a estrutura:

```yaml
repository: owner/name
url: https://github.com/owner/name
functional_domain: threat-hunting
artifact_type: code | configuration | lab | guide | official
proposed_tier: A | B | C
why_relevant: "qual lacuna funcional resolve"
verified_artifacts: ["README", "rules/", "tests/"]
limitations: ["versão", "dependências", "testes ausentes"]
license_review: required
```

**Critério editorial:** é melhor uma referência bem documentada e com limites explícitos do que dez repositórios tratados como sinônimos de maturidade.
