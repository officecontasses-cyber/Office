# Cliente 18 — CC&D (CC&D Serviços de Informática Ltda): dossiê para o fechamento

**Gatilho:** "fechamento da empresa #18". Criado em 17/10/2026 a partir da Controle_Fiscal (export 17/10), Cadastro_Clientes, Drive (DecWeb 09/2026) e memória. Incluir sempre a conferência IBS/CBS (ver CLAUDE.md). Os dados que a Fernanda "mapeou" em 17/10 ainda não foram vistos aqui: ela deve dizer onde salvou (Domínio set, Portal, e-mails).

## Cadastro e particularidades
- CNPJ 93.309.631/0001-78, Porto Alegre/RS, IM 503138-2-7 (nome na prefeitura: CC&D SERVIÇOS DE INFORMATICA LTDA), **Lucro Presumido**, não contribuinte de ICMS. CNAE 9511800 (reparação e manutenção de computadores e periféricos); secundário 3314709. Sócios: Isabel Lorena Sebben (administradora), Mario Guilherme Sebben, RFL Sistemas S/A. Grupo com a RFL (133) e ILS (177).
- **Portal Nacional:** adesão obrigatória, mas a linha CERTIFICADO DIGITAL da Controle diz: "CLIENTE ENVIA AS NOTAS | NÃO TEMOS ACESSO AO CERTIFICADO DIGITAL". Sem certificado: o robô não baixa Emitidas/Recebidas; as notas vêm do cliente (Inês), do DecWeb/ISSQNdec e do SIEG.
- **ISSQN:** guia mensal de 2% sobre o prestado (set: base 2.100,00, ISS 42,00). Declaração pelo DecWeb (robô); recibo e guia em `002 ARQUIVOS MUNICIPAIS`. Não é Sociedade de Profissionais.
- **Cliente-fonte:** a receita vem de notas para a **Datasys Sistemas em Informática**, que retém tributos federais. Padrão de agosto (nota 10, R$ 2.100,00): retenção total R$ 129,15 = IRRF 1,5% (31,50) + PIS 0,65% (13,65) + COFINS 3% (63,00) + CSLL 1% (21,00), Lei 10.833 art. 30. PIS/COFINS do mês ficam `Compensado` (DARF 0,00); IRRF e CSLL retidos viram crédito no IRPJ/CSLL trimestral.
- **DARF REFIS:** parcela mensal de R$ 31,50, venc. último dia útil do mês (guia `18_CC&D_PortoAlegre_MM.2026_REFIS.pdf`; ago foi G-Click 14/09, venc. 30/09). Set: vence 30/10.
- **REINF:** R-2099 sem retenção, provisório "aguardando movimento (Inês)": R-2099 de 09/2026 enviado 04/10 16:21 (recibo 12177287-01-2099-2609-12177287). Se a Datasys/outro tomador reteve, avaliar R-4020 do prestador? (retenção sofrida não gera R-4020 para o prestador; conferir o que o escritório faz nos outros clientes).
- **Atenção SPED Contribuições 08/2026:** saldo de retenção de 06, 07 e 08/2026 aparece sem uso nos registros 1300/1700, embora M200/M600 usem a retenção (conferir no Domínio).

## Situação em Set2026 (Controle_Fiscal, 17/10)
| Obrigação | Status | Observação |
|---|---|---|
| DECLARAÇÃO PREFEITURA | Enviado | DecWeb 01/10 17:35:13; receita 2.100,00, ISS 42,00, retido de terceiros 0,00 |
| GUIA ISSQN | Enviado | R$ 42,00, G-Click 04/10; venc. 13/10 (impresso na guia) |
| REINF | Enviado | R-2099 04/10 (provisório) |
| SERVIÇOS PRESTADOS | (vazio) | falta Domínio importado e conciliado (nota 11 Datasys, 29/09, R$ 2.100,00) |
| SERVIÇOS TOMADOS | (vazio) | DecWeb: sem tomados? conferir; ago teve 2 (Officecont 474,80 + Safeweb 330,00) |
| DARF PIS / COFINS | (vazio) | venc. 23/10; provável `Compensado` se a Datasys reteve |
| DARF IRPJ / CSLL | (vazio) | 3º tri, venc. 30/10 (exige jul+ago+set) |
| DARF REFIS | (vazio) | venc. 30/10 |
| SPED CONTRIBUIÇÕES | (vazio) | venc. 16/11 |
- Pendente com a Inês (desde 05/10): movimento de setembro e **se a Datasys reteve** na nota 11 (R$ 2.100,00, 29/09). Sem resposta registrada até 17/10.

## O que falta levantar no fechamento de 09/2026
1. Retenção da nota 11 (Datasys): XML/Portal/Domínio; definir PIS/COFINS (13,65 / 63,00) `Compensado` ou DARF.
2. Domínio set: Saídas (prestados), Entradas (tomados), resumo dos impostos; conciliar com DecWeb (receita 2.100,00).
3. IRPJ/CSLL do 3º tri (jul+ago+set): receita do trimestre x 32%; IRPJ 15% (adicional só acima de R$ 60.000/tri); CSLL 9%; abater IRRF/CSLL retidos; DARF só se o valor for ≥ R$ 10,00 (confirmar no Domínio). Receita de julho a levantar (só ago = 2.100,00 e set = 2.100,00 conhecidos).
4. REFIS de set (R$ 31,50, venc. 30/10).
5. IBS/CBS: prestados (nota 11: CST/cClassTrib; sem Portal sem certificado, usar XML/DecWeb), tomados (NFS-e), entradas (NF-e), créditos x acumuladores.
6. EFD-Contribuições set (venc. 16/11) e saldo de retenção sem uso (1300/1700).
