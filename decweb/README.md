# Robô DecWeb (ISSQN de Porto Alegre) — OfficeCont

Automatiza, por empresa, no DecWeb da Prefeitura de Porto Alegre: criar a declaração do mês, baixar os relatórios de
Prestados e Tomados, **enviar** a declaração e baixar os PDFs (Declaração + Recibo; Guia/ISSQN só quando há valor).
**Serve apenas para empresas com inscrição em Porto Alegre (DecWeb).** Adaptado do pacote de outro escritório (01/10/2026).

## O que mudou em relação ao pacote original
| Assunto | Como ficou |
|---|---|
| Pastas | `<raiz>\<MM_MES>\002 ARQUIVOS MUNICIPAIS` (primeiro o mês, depois o tipo), como no Drive do escritório |
| Nomes dos arquivos | `{n}_{apelido}_PortoAlegre_MM.AAAA_NFSE_ServPrestados.zip` (+ subpasta extraída com o mesmo nome), `..._NFSE_ServTomados.zip`, `..._DeclaraçãoMensal.pdf`, `..._ISSQN.pdf` |
| Conferência com o Portal Nacional | **desligada** (config). Ligada, acha a planilha Emitidas pelo **CNPJ** dentro dela e, sem planilha, envia assim mesmo (`sem_emitidas = enviar`) |
| Avisos "Não foi informado serviço prestado/tomado" | por cliente: coluna `aceitar_avisos` do `clientes.csv` (além do `--aceitar-avisos` da rodada inteira) |
| `clientes.csv` | aceita BOM, linhas em branco e a coluna `cnpj` |

## Instalação (uma vez)
1. Instale **Python 3.10+** e o **Google Chrome**.
2. Copie esta pasta (`decweb`) para **fora do "Meu Drive"**, por exemplo `C:\Robos\decweb`.
   Dentro do Meu Drive, o `clientes.csv` (com senhas) e os `logs` seriam sincronizados com a nuvem.
3. Na pasta: `pip install -r requirements.txt`
4. Copie `config\configuracao.exemplo.ini` para `config\configuracao.ini` e confira `raiz_fechamento`
   (a pasta `FECHAMENTO FISCAL` que contém `08_AGOSTO`, `09_SETEMBRO`...).
5. Copie `config\clientes.exemplo.csv` para `config\clientes.csv` e preencha **uma linha por empresa**:
   `numero,apelido,nome_painel,cnpj,usuario,senha,aceitar_avisos`
   - `numero` **sem zero à esquerda** (`16`, não `016`) e `apelido` **igual ao usado hoje nos nomes dos arquivos**
     (`CentroClinico`, `CC&D`, `L S Becker`...), para o robô não criar arquivos com outro nome.
   - `usuario` / `senha`: login do DecWeb da empresa. **Esse arquivo tem senhas: não envie por e-mail/chat/Drive
     nem coloque no repositório** (já está no `.gitignore`).
   - `aceitar_avisos`: deixe em branco; escreva `sim` **só** para a empresa que você sabe que não teve receita
     no mês (veja "Receita zero" abaixo).
   - Salve em UTF-8.

## Uso (fase T = tudo, envio oficial)
```
python decweb_login.py --competencia 09/2026 --fase T --clientes 177 --enviar
python decweb_login.py --competencia 09/2026 --fase T --clientes 177,173,186 --enviar
python decweb_login.py --competencia 09/2026 --fase T --clientes todos --enviar
```
A fase T cria (ou reaproveita) a declaração, baixa e extrai os zips, **envia oficialmente** e baixa os PDFs.
**O envio é irreversível e sem pausa.** Sem `--enviar` o robô recusa; no modo interativo pede para digitar `ENVIAR`.
Se a competência já tem declaração enviada, o robô **não** cria outra (registra pendência); só retifica com
`--retificadora`. Se uma rodada falhar depois do envio, rodar de novo pula direto para a impressão.

Outras fases: `--fase 1` (cria + baixa, **não envia**), `--fase 2` (envia), `--fase 3` (baixa o PDF),
`--fase C` (só conferir com o Portal Nacional, sem abrir o site).

| Opção | O que faz |
|---|---|
| `--clientes 12,15` ou `todos` | quais empresas (pelo `numero` do CSV) |
| `--retificadora` | cria retificadora quando a competência já tem declaração enviada |
| `--com-conferencia` / `--sem-conferencia` | liga/desliga, só nesta rodada, a conferência com a planilha Emitidas do Portal Nacional |
| `--aceitar-avisos` | aceita os avisos de receita zero para **todas** as empresas da rodada (prefira a coluna do CSV) |

### Receita zero
Quando a empresa não teve notas, o DecWeb avisa "Não foi informado serviço prestado/tomado" e o robô, por segurança,
para e registra pendência. Para empresas que você **confirmou** que não tiveram receita, marque `sim` em
`aceitar_avisos`. Só esses avisos são aceitos; qualquer outra pendência (cadastro, valor inválido...) continua bloqueando.

## Resultado
`logs\resumo_atual.csv` (status e etapas por empresa: `declaracao_criada;zips_baixados;conferido;enviada;pdf_baixado`),
`logs\resultados.csv` (histórico) e `logs\` (execução). Em erro ou pendência, imagem e HTML da tela em `logs\diagnostico\`.
O robô nunca grava usuário nem senha nos logs. Os PDFs e planilhas ficam em `002 ARQUIVOS MUNICIPAIS` do mês.

## Cuidados
- Não use o mesmo Chrome do robô ao mesmo tempo. Em lotes grandes o Chrome pode cair; o robô tenta de novo.
- Se o DecWeb apontar pendência (cadastro do responsável desatualizado etc.), o robô para nessa empresa, registra e
  segue para a próxima; resolva no site.
- A fase T ainda não tinha sido testada de ponta a ponta no pacote original: acompanhe a **primeira** rodada.
- Registro na Controle_Fiscal: este robô **não escreve na planilha**. Status só muda com a sua confirmação.

## Testes (opcional, não abrem o site)
```
pip install -r requirements-dev.txt
python -m pytest tests
```
