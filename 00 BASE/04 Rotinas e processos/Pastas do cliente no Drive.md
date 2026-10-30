# Pastas do cliente no Drive
Atualizado em: 30/10/2026 · por: sessão Claude Code (montagem da base)
Fontes: leitura das pastas do 238 e de outros clientes no Drive (24 a 27/10/2026); skill `fechamento-contabil-dominio/references/checklist-documentos.md`

O Claude não cria, move nem apaga nada nessas pastas. Ele lê e diz onde salvar.

## Padrão
```
NNN_NOME DO CLIENTE/
├── CADASTRO/                          contrato social e cadastro
└── {ano}/
    ├── 001_DOCUMENTOS DIGITALIZADOS/{MM_MÊS}/   extratos, comprovantes, notas, documentos do cliente
    ├── 002_FISCAL/001_FEDERAIS/                 DARFs emitidos
    ├── 003_FOPAG/{MM_MÊS}/                      folha salva pelo DP (extrato mensal, DCTFWeb)
    └── 005_CONTABIL RELATORIOS/
        ├── MAPA CONTABIL NNN.xlsx
        ├── 013_APURAÇÃO LALUR/                  (Lucro Real) planilhas de apuração
        └── {MM_MÊS}/                            razão, balancete e arquivos do fechamento
```
`{MM_MÊS}` segue `09_SETEMBRO`. A pasta do cliente é achada pelo número: "238" → `238_REAT HOLDING`.

## Onde salvar
| Arquivo | Pasta |
|---|---|
| Extratos e comprovantes de pagamento | `{ano}/001_DOCUMENTOS DIGITALIZADOS/{MM_MÊS}` |
| Situação fiscal, Diagnóstico SIEG, certidões | `{ano}/001_DOCUMENTOS DIGITALIZADOS/{MM_MÊS}` |
| Razão, balancete, plano de contas, relatórios fiscais do Domínio | `{ano}/005_CONTABIL RELATORIOS/{MM_MÊS}` |
| Conciliação bancária, importação, ajustes, papel de trabalho | `{ano}/005_CONTABIL RELATORIOS/{MM_MÊS}` |
| Mapa contábil do cliente | `{ano}/005_CONTABIL RELATORIOS/` |

## Outras pastas do escritório
- Modelo de importação do Domínio: `1015_ROTINA AUTOMATICA/003 CONTABILIDADE/`.
- O contábil não salva relatórios da folha: lê o que o DP salva em `003_FOPAG`.
