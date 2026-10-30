# Domínio Sistemas
Atualizado em: 30/10/2026 · por: sessão Claude Code (montagem da base)
Fontes: skill `fechamento-contabil-dominio` (referências `integracao-modulos-dominio.md` e `lancamentos-bancarios.md`); modelo de importação lido em 26/10/2026; links testados pela responsável em 26/10/2026

## Para que serve
Sistema contábil, fiscal, folha e patrimônio do escritório. Quem opera é o colaborador; o Claude orienta e confere.

## Importação de lançamentos (Excel)
- Modelo: `1015_ROTINA AUTOMATICA/003 CONTABILIDADE/planilhamodeloimportacaolancamentoscontabeis.xlsx` (no Drive).
- Colunas: Data · Cód. Conta Debito · Cód. Conta Credito · Valor · Cód. Histórico · Complemento Histórico ·
  Inicia Lote · Código Matriz/Filial · Centro de Custo Débito · Centro de Custo Crédito.
- **Inicia Lote = 1** marca o início de um lote (comentário do próprio modelo). Data como data, códigos
  como número, valor com formato `0.00`. Copiar o modelo e preencher é o jeito mais seguro.
- Ainda não confirmado numa importação real: se o Domínio aceita o arquivo sem erro.

## Manuais da central (suporte.dominioatendimento.com)
Endereço: `https://suporte.dominioatendimento.com/central/faces/solucao.html?codigo=N`

| Código | Assunto | Situação |
|---|---|---|
| 230 | Integração contábil dos lançamentos das notas | abre (26/10/2026) |
| 655 | Lançamentos que não foram regerados | abre (26/10/2026) |
| 5551 | Perguntas e respostas da integração | **inativo** |
| 1817 · 1809 · 44 · 51 | Razão · Balancete · Plano de contas · Livros contábeis | não conferido |
| 3609 · 3568 | Conferir a integração | não conferido |
| 71 | Acompanhamento de serviços | não conferido |
| 509 · 504 · 505 | Depreciação · relação de bens | não conferido |
| 881 · 1156 · 231 · 2846 · 10185 · 6703 | Integração fiscal, acumulador, impostos | não conferido |
| 822 · 4497 · 9272 · 3566 | Integração da folha | não conferido |
| 3522 · 1278 · 1998 | Baixa de bens · lançamento manual · demonstrativo de impostos | não conferido |

Sem manual mapeado: relatório de entradas/saídas e títulos em aberto. Perguntar o caminho que o colaborador usa.
A lista completa e atualizada fica na referência da skill.
