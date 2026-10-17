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

## Domínio 09/2026 — Resumo dos Impostos (arquivo "Empresa 18 - CCED SERVICOS DE INFORMATICA LTDA.pdf", 17/10 18:22; único arquivo novo no Drive; Entradas/Saídas/Serviços do 18 não foram salvos)
- PIS 0,65% x 2.100,00 = 13,65 e COFINS 3% x 2.100,00 = 63,00, **cobertos por retenção de 13,65 e 63,00** (a recolher 0). Saldo credor de retenção a transportar: PIS 48,95 e COFINS 225,00 (total 273,95), sem uso (mesmo ponto do SPED 08/2026, registros 1300/1700).
- **IRPJ 3º tri:** base 1.008,00 (= 6.300,00 x 16%), 15% = 151,20, IRRF retido 94,50 (3 x 31,50), **a recolher 56,70**. O Domínio usa **16%** de presunção no IRPJ (serviços com receita anual até R$ 120.000, art. 40 da Lei 9.250/95; sem confirmação total do artigo: conferir o FAT do ano).
- **CSLL 3º tri:** base 2.016,00 (= 6.300,00 x 32%), 9% = 181,44, retido 63,00 (3 x 21,00), **a recolher 118,44**.
- **REFIS:** base 2.100,00 x 1,5% = 31,50 (venc. 30/10).
- ISS 42,00 = guia enviada. Sem créditos de IBS/CBS (sem tomados nem entradas lançados).
- IBS/CBS prestados: débitos CBS 17,83 e IBS 1,98 = base 1.981,35 (2.100,00 - ISS 42,00 - PIS 13,65 - COFINS 63,00) x 0,9% e 0,1%, sem redução. Falta conferir CST/cClassTrib no XML da nota 11 (sem Portal).
- **Ressalva:** o Domínio assume retenção da Datasys em setembro (nota 11, 29/09). Sem confirmação (Inês não respondeu; XML não visto). Cenário sem retenção em set: PIS 13,65 + COFINS 63,00 a recolher; IRPJ 151,20 - 63,00 = 88,20; CSLL 181,44 - 42,00 = 139,44.

## Conferência completa 09/2026 (17/10/2026, dados salvos pela Fernanda)
- **Nota 11 Datasys (DANFSe lido, chave 43149022293309631000178000000000001126090976944995, emitida 29/09/2026 18:53, competência 28/09):** R$ 2.100,00; ISS 2% = 42,00 não retido; **retenções federais confirmadas: IRRF 31,50 + PIS/COFINS/CSLL 97,65 (13,65 + 63,00 + 21,00) = 129,15**; IBS/CBS CST 000 / cClassTrib 000001, base 1.981,35 (2.100,00 - 118,65), IBS 1,98 e CBS 17,83 sem redução = Domínio. (XML na pasta do cliente; lido só o PDF.)
- **Domínio Saídas (Serviços_18):** nota 11, 2.100,00, ISS 42,00, IRRF 31,50, PIS-RET 13,65, COFINS-R 63,00, CSOC-RET 21,00 = nota. Conciliado com a Declaração Mensal (receita 2.100,00).
- **FAT 2026 (018_CCED SERVICOS_FAT2026):** receita 2.100,00 todo mês (jan-set), total 18.900,00 (<= R$ 120.000, confirma presunção de 16% no IRPJ, rótulo "IRPJ - percentual de 16%"); 3º tri: receita 6.300,00, IRPJ 56,70 e CSLL 118,44 líquidos de retenção = Domínio; PIS/COFINS cobertos pela retenção; REFIS 31,50.
- **Entradas (Entradas_18):** NF 1029 OFFICECONT ASSESSORIA EMPRESARIAL LTDA (CNPJ 35.743.878/0001-00), emissão 05/10/2026, entrada 30/09/2026, R$ 474,80, CFOP 1-933, sem ISS e sem crédito de IBS/CBS no Domínio. A nota é de 05/10, depois da declaração DecWeb de 01/10: falta conferir se aparece nos tomados da prefeitura (ISSQNdec) e os dados IBS/CBS da nota.
- **REFIS set:** guia SENDA/Sicalc gerada 17/10 18:25, cód. 9100, PA 01/09/2026, venc. 30/10/2026, R$ 31,50 = Domínio/FAT. Falta G-Click.
- **IRPJ/CSLL 3º tri:** guias ainda não geradas/salvas (IRPJ 56,70 cód. 2089; CSLL 118,44 cód. 2372; venc. 30/10).
- Pasta do cliente (Movimento CCED 09-2026, enviada em 09/10): recibos RFL x CCED (devolução de empréstimo R$ 516,80 em 10/09 e 17/09) e "Slips" de pagamentos (10/09: RFL 1.970,85, Officecont 474,80 ref. NF 3607 08/2026, Prefeitura 42,00 ISS ago). Empréstimo entre RFL e CC&D não é receita (fora do FAT). Lidos só o recibo de 10/09 e o slip de 10/09.
- Em aberto: saldo credor de retenção PIS 48,95 / COFINS 225,00 no Domínio (a retenção mensal do FAT cobre exatamente o devido, o saldo não se explica; ver 1300/1700).

## G-Click REFIS (17/10/2026)
Print: tarefa REFIS (CC&D SERVICOS, meta 09/10, venc. 30/10), atividade "Guia" concluída por fernanda.officecont em 17/10/2026 18:30. DARF REFIS 31,50 = comprovada (`Enviado` no TSV final). **A Fernanda pediu o TSV final do #18 só depois que ela enviar o restante** (guia IRPJ/CSLL, NF 1029 etc.); não entregar antes.
