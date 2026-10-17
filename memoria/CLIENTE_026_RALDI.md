# Cliente 26 — RALDI (Raldi Comércio e Representações Ltda): dossiê para o fechamento

**Gatilho:** "fechamento da empresa #26". Criado em 17/10/2026 a partir da Controle_Fiscal (export 17/10), Cadastro_Clientes, FAT 2026, Declaração Mensal de 09/2026 e recibo REINF. Incluir sempre a conferência IBS/CBS (ver CLAUDE.md).

## Cadastro e particularidades
- CNPJ 05.057.885/0001-89 (na Controle perdeu o zero à esquerda: 13 dígitos na coluna B, formatar como texto), Porto Alegre/RS (Rua Marechal Floriano Peixoto 730, Centro), IM 199351-2-9, **Lucro Presumido**, sócio-administrador Antenor Raldi. CNAE 4613300 (representantes comerciais, madeira/material de construção/ferragens); secundário 4614100 (máquinas e equipamentos).
- Cadastro_Clientes: "Contribuinte ICMS" = **Baixada** e IE "Não localizada / Isento" (inscrição estadual baixada, não contribuinte de ICMS; situação do CNPJ não verificada aqui: conferir o Cartão CNPJ se houver dúvida). Portal Nacional: adesão obrigatória, mas não há arquivos de NFS-e do Portal do 26 no Drive em 08 e 09/2026 (só a Declaração Mensal); certificado A1 de Antenor Raldi existe (.pfx na pasta de certificados).
- **Empresa sem movimento:** FAT 2026 todo zerado (receitas e rendimentos financeiros, jan-dez); Ago2026 tudo `Sem movimento` após checagem das 5 fontes (municipal, Portal, XML, SIEG, Domínio). Sem retenções.
- **ISSQN/DecWeb:** declaração mensal com receita 0,00, imposto 0,00, sem guia. SPED Contribuições 08/2026: transmitido sem movimento (04/10 13:33:53, PIS e COFINS 0,00). O PVA apontou erro no registro 0120 (meses sem movimento) em 07/2026 e 08/2026 (ponto recorrente).
- **REINF:** R-2099 sem retenção (09/2026: recibo 12060343-05-2099-2609-12060343, 04/10 16:24).

## Situação em Set2026 (Controle_Fiscal, 17/10)
| Obrigação | Status | Observação |
|---|---|---|
| DECLARAÇÃO PREFEITURA | Enviado | recibo 03/10 11:17:09, receita 0,00, imposto 0,00 |
| GUIA ISSQN | Sem movimento | sem guia |
| REINF | Enviado | R-2099 04/10 |
| SERVIÇOS TOMADOS / PRESTADOS | (vazio) | falta confirmar nas fontes (Portal/XML/SIEG/Domínio) |
| DARF PIS / COFINS | (vazio) | venc. 23/10; esperado `Sem movimento` 0,00 |
| DARF IRPJ / CSLL | (vazio) | 3º tri, venc. 30/10; esperado `Sem movimento` (FAT zero; conferir CONTROLE\|Rendimentos 3º tri) |
| SPED CONTRIBUIÇÕES | (vazio) | venc. 16/11 |

## O que falta no fechamento de 09/2026
1. Domínio set (Saídas, Entradas, resumo dos impostos) e fonte oficial: confirmar que não há nota (Serviços Prestados e Tomados `Sem movimento`).
2. Rendimentos financeiros 3º tri (planilha CONTROLE | Rendimentos, linha 26): se `Zerado`, IRPJ/CSLL do trimestre `Sem movimento`.
3. IBS/CBS: sem notas, nada a conferir (confirmar no Portal/Domínio).
4. SPED Contribuições set (16/11) sem movimento (0120 do PVA).

## Conferência DecWeb x Portal Nacional (17/10/2026)
- **DecWeb zerado: coerente.** Declaração 09/2026 (recibo 03/10 11:17:09): receita 0,00, imposto 0,00, retido de terceiros 0,00; sem guia; sem zip de NFS-e prestadas/tomadas no Drive (nos clientes com nota, o robô baixa); FAT 2026 zerado; Ago idem. Isso vale para notas que entram no ISSQNdec (NFS-e emitida/recebida no sistema municipal/nacional).
- **Portal Nacional: NÃO verificado.** O 26 consta entre os 11 clientes sem certificado instalado no PC (lista de 02/10; PENDENCIAS); não há arquivos do Portal do 26 em 08 e 09/2026. "Zero" no Portal só vale se o robô rodar com certificado válido (existe um .pfx de Antenor Raldi de 2024 na pasta de certificados; validade não verificada). Alternativas: SIEG (CNPJ 05.057.885/0001-89) ou relação de notas do cliente.
