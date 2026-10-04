# Office: robô ISSQN São Leopoldo/RS

Automação do fechamento mensal do ISSQN (cliente 126 Tatsch & Leite), baseada na skill `sao-leopoldo-issqn`.

## Etapas (o robô fecha a prefeitura de ponta a ponta)
- 0. Esqueleto e configuração (feita)
- A. Abrir o portal com o Chrome e login por certificado digital, somente leitura (feita, falta testar no portal real)
- B. Consulta DMS (feita no portal real) e baixar o Livro Fiscal (B2: pronta, falta testar no portal real)
- C. Conferir DMS × Emitidas do Portal Nacional × guia (se divergir, o robô para)
- D. Pedir confirmação no terminal, gerar faturamento e imprimir a guia
- E. Salvar no Drive e montar a linha da Controle_Fiscal (sem marcar status)

## Regras
- Nunca colocar senha no chat nem no repositório (`.env` é ignorado pelo Git).
- Status `Enviado` só com confirmação explícita da Fernanda.

## Uso
    pip install -r requirements.txt
    copy .env.example .env      (preencha ISSQN_PORTAL_URL)
    python -m robo_issqn abrir
    python -m robo_issqn consultar 09/2026
    python -m robo_issqn livro 09/2026
    python -m robo_issqn 09/2026
    python -m unittest discover tests
