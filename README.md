# Office: robô ISSQN São Leopoldo/RS

Automação do fechamento mensal do ISSQN (cliente 126 Tatsch & Leite), baseada na skill `sao-leopoldo-issqn`.

## Etapas
1. Esqueleto e configuração (feita)
2. Conciliação DMS × Portal Nacional × guia
3. Nomes de arquivo e linha TSV da Controle_Fiscal
4. Google Drive
5. Navegação no portal (para antes de "Gerar faturamento")

## Regras
- Nunca colocar senha no chat nem no repositório (`.env` é ignorado pelo Git).
- Status `Enviado` só com confirmação explícita da Fernanda.

## Uso
    python -m robo_issqn 09/2026
    python -m unittest discover tests
