# Cyber Threat Intelligence e Retro-Hunting

**Objetivo:** enriquecer observações Wazuh e executar buscas históricas contextualizadas. **Match de IOC não equivale automaticamente a incidente.**

| Prioridade | Projeto | Entrega verificada por documentação | Cuidados |
|---|---|---|---|
| **A** | [Wazuh-TI](https://github.com/federicofantini/Wazuh-TI) | Integração Django/Celery, OpenCTI/TAXII, exportação de CDB e retro-hunting no Wazuh Indexer | Revisar autenticação, permissões, desempenho, limites de busca e licença |
| **A** | [wazuh-opencti-integration](https://github.com/Aandr34/wazuh-opencti-integration) | Integração de alertas com OpenCTI; exemplos para DNS, IPs, hashes e observáveis | Regras de disparo, volumes de consultas, semântica de IOC e versões |
| **B** | [opencti-integration](https://github.com/bonyjohn05/opencti-integration) | Docker e scripts/configuração de integração Wazuh + OpenCTI + regras XML | Referência de implementação; arquivos de exemplo não são configuração auditada |
| **B** | [Wazuh XDR, SOAR & Threat Intelligence Lab](https://github.com/0xcgz/threat-intelligence-threat-hunting-wazuh) | Integrações com Shuffle, VirusTotal, AbuseIPDB e AlienVault OTX | Documento de laboratório; não presumir conectores operacionais reaproveitáveis |
| **B** | [Wazuh SOC Enterprise](https://github.com/brunoflausino/wazuh-soc-enterprise) | Casos com CDB, MISP, Suricata, correlação e evidências | Selecionar casos e conferir integrações, sem importar stack inteira |
| **B** | [shuffle-soc-automation](https://github.com/heraclescap/shuffle-soc-automation) | Workflows de enriquecimento com Cortex, OpenCTI e criação de caso IRIS | Sanitizar observáveis e limitar envio a APIs externas |
| **A (oficial)** | [wazuh/integrations](https://github.com/wazuh/integrations) | Coleção oficial de contribuições para integrações de terceiros | Contribuições comunitárias não implicam compatibilidade/segurança garantidas |

## Modelo de pipeline desejável

```text
Fonte de inteligência (MISP / OpenCTI / TAXII)
    -> ingestão + proveniência
    -> tipagem/normalização de IOC
    -> confiança + validade temporal + escopo
    -> enriquecimento de alerta OU busca retrospectiva com limites
    -> evidência e hipótese analítica
    -> revisão humana / caso
    -> expiração, deduplicação e melhoria de detecção
```

## O que registrar para cada IOC

```yaml
indicator_id: "ioc-demo-001"
type: "domain"
value: "example.invalid"  # domínio reservado, valor fictício
source: "dataset sintético"
confidence: 50
first_seen: null
last_seen: null
valid_until: null
tlp: "TLP:CLEAR"
query_scope: "lab-only"
evidence_ids: []
```

O exemplo não define um padrão de classificação universal nem preenche metadados que não se conhece. **TLP, confiança e TTL** devem obedecer à política do consumidor.

## Checklist de retro-hunting

- [ ] Consultar somente índices e períodos autorizados.
- [ ] Definir limites de cardinalidade, paginação, taxa e timeout.
- [ ] Marcar o primeiro carregamento de feeds para não disparar buscas históricas massivas inadvertidamente.
- [ ] Distinguir IOC observado, inteligência válida, coincidência de campo e alerta confirmado.
- [ ] Não consultar serviços de reputação públicos com dados sensíveis sem autorização.
- [ ] Registrar consultas, evidências, fontes, resultados negativos e data da última atualização.

**Exercício sugerido:** [trilha CTI sintética](../docs/trilhas.md#trilha-3--cti-e-retro-hunting). Para triagem pós-match, veja [Incident Response](incident-response.md).
