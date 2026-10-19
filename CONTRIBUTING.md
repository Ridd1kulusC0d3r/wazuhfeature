# Contribuindo com o Wazuh Feature Atlas

Este é um catálogo **independente** de funcionalidades e projetos do ecossistema Wazuh. Contribuições são bem-vindas quando incluem fonte primária, contexto técnico e limites explícitos.

## O que enviar

- Referência de repositório que resolva um caso de uso específico de detecção, CTI, hunting, DFIR, incident response, war games defensivos, plataforma ou automação.
- Correção factual, link desatualizado ou compatibilidade de versão documentada.
- Uma trilha guiada com dados sintéticos, objetivos, evidências e critérios de aceite.

## Antes de abrir PR

1. Verifique [`catalog/repositorios.csv`](catalog/repositorios.csv) para evitar duplicações.
2. Descreva **qual funcionalidade** o item cobre e se é código, configuração, laboratório ou guia.
3. Identifique mantenedor, licença **a verificar**, dependências, versão-alvo, artefatos presentes e limitações.
4. Diferencie **testado por você** de **declarado pelo README do autor**.
5. Execute `python scripts/validate_catalog.py`.
6. Não inclua dados pessoais, tokens, telemetria privada ou ferramentas/datasets sem direito de redistribuição.

## Sugestão de referência

Abra uma [nova issue](https://github.com/Ridd1kulusC0d3r/wazuhfeature/issues/new/choose) usando o modelo `Sugestão de repositório`, informando URL, capacidade, uso e cautelas. Para conteúdo aprovado, um PR pode atualizar o CSV e o módulo correspondente.

## Política de autoria, licenças e transparência

Não copiamos código de repositórios listados. Atribuímos mantenedores por links diretos. O licenciamento de uma referência não concede licença automática para reutilizar seu conteúdo no atlas.

A identidade visual e a refatoração inicial do README foram desenvolvidas com assistência de IA e identificadas como tal no [guia visual](docs/design-system.md). **Este repositório não declara seus materiais automaticamente elegíveis como contribuições de Wazuh Ambassador.** Para esse programa, verificar a versão publicada de suas [regras oficiais](https://wazuh.com/legal-resources/ambassadors-program-rules/).

## Checklist de revisão

- [ ] Link GitHub canônico e sem duplicação.
- [ ] Relacionado a pelo menos uma capacidade Wazuh.
- [ ] Observações técnicas, limitações e documentação própria.
- [ ] Links internos e integridade CSV válidos.
- [ ] Referência não tratada como solução “production ready” sem provas.
- [ ] Nenhuma marca de terceiro alterada ou identidade de endosso presumida.

## Código de conduta

Seja técnico, respeitoso, documente desacordos e preserve privacidade. Vulnerabilidades reais e dados de incidentes devem ser tratados pelos canais responsáveis, não publicados como exemplos no atlas.
