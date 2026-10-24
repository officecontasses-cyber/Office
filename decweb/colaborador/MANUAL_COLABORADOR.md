# Manual do colaborador: robô do ISSQN de Porto Alegre (DecWeb) no seu computador

O robô entra no DecWeb da Prefeitura de Porto Alegre, cria a declaração do mês de cada empresa, baixa os relatórios
de Serviços Prestados e Tomados, **envia** a declaração e baixa os PDFs (Declaração, Recibo e, quando há valor, a guia do ISSQN).
Ele roda **no seu computador** (Windows). Você abre o Claude Code do **fechamento fiscal**, pede o comando já com tudo
parametrizado, cola o comando no terminal e o robô trabalha no seu Chrome.

Empresas deste pacote: 22 clientes de Porto Alegre (lista no fim deste manual).
Só entram empresas com inscrição em **Porto Alegre**; as de outras cidades da planilha ficam de fora.

---

## Parte A. Instalação (uma vez só)

### Passo 1. Programas
1. **Google Chrome** (atualizado).
2. **Python 3.10 ou mais novo** (python.org). Na instalação, marque **"Add python.exe to PATH"**.
   Conferir: abra o *Prompt de Comando* e digite `python --version`. Deve aparecer a versão.
3. **Google Drive para computador**, com acesso à pasta `001 FECHAMENTO FISCAL` (a mesma que a Fernanda usa).
4. **Claude Code** instalado e entrando na sua conta (a Fernanda orienta).

### Passo 2. Copiar a pasta do robô (fora do Meu Drive)
1. A Fernanda envia o arquivo **`decweb.zip`** (sem o `clientes.csv`, sem `logs`).
2. Crie a pasta `C:\Robos` e extraia o zip dentro dela, de modo que exista **`C:\Robos\decweb\decweb_login.py`**.
3. **Nunca** coloque essa pasta dentro do "Meu Drive": o `clientes.csv` tem senhas e os `logs` iriam para a nuvem.

### Passo 3. Instalar as bibliotecas
No Prompt de Comando:
```
cd C:\Robos\decweb
pip install -r requirements.txt
```

### Passo 4. Configurar a pasta do Drive
1. Copie `config\configuracao.exemplo.ini` para `config\configuracao.ini`.
2. Abra o `configuracao.ini` no Bloco de Notas e ajuste só a linha:
   ```
   raiz_fechamento = <caminho da pasta 001_FECHAMENTO FISCAL no seu Drive>
   ```
   Como achar: no Explorador de Arquivos, abra a pasta `001_FECHAMENTO FISCAL` (a que tem dentro `08_AGOSTO`, `09_SETEMBRO`...),
   clique na barra de endereço e copie o caminho. Pode ser que a letra do seu Drive não seja `I:`.
   Escreva o caminho normal do Windows, sem aspas.
3. Deixe `conferencia = nao`.
4. O robô grava os arquivos em `<raiz>\<MM_MES>\002 ARQUIVOS MUNICIPAIS` (ex.: `09_SETEMBRO\002 ARQUIVOS MUNICIPAIS`).
   Confirme que essa pasta existe para o mês que vai fechar (se não existir, crie).

### Passo 5. Montar o `clientes.csv` (com as senhas)
O `clientes.csv` é a lista das empresas com o login e a senha do DecWeb. Ele já vem **pronto**, é só preencher as senhas
com a planilha de dados completos. **As senhas não vão por e-mail, chat, WhatsApp, Drive nem repositório.**

1. Abra a planilha **"Clientes Simples - Dados_Completos"** (a Fernanda dá o acesso).
2. Menu *Arquivo > Fazer download > Valores separados por vírgula (.csv)*.
3. Salve o arquivo em uma pasta **fora do Drive**, por exemplo `C:\Robos\temp\` (crie a pasta).
4. No Prompt de Comando:
   ```
   cd C:\Robos\decweb
   python colaborador\montar_clientes.py "C:\Robos\temp\Clientes Simples - Dados_Completos.csv" --apagar-origem
   ```
   (Ajuste o nome do arquivo se o download vier com outro nome.)
5. O programa mostra quantas empresas gravou e **avisa** quem ficou de fora. O esperado hoje:
   - **148 ARS, 213 GCL e 222 RC Bertoglio** ficam fora, porque a planilha não tem a senha do DecWeb (a 222 está com "-").
     Peça à Fernanda as senhas; depois rode o script de novo (ele refaz o arquivo inteiro).
   - **38 Valmac (Tubarão/SC), 44 STN (Caxias do Sul/RS), 216 Maricota (Palhoça/SC) e 235 Sandra Carvalho (Canoas/RS)**
     não entram: não têm inscrição em Porto Alegre.
6. Com `--apagar-origem` o programa apaga o CSV exportado no fim. Se não usou, **apague você** (ele tem senhas).
7. O resultado fica em `C:\Robos\decweb\config\clientes.csv`. **Não envie esse arquivo a ninguém** (o `.gitignore` já o protege).
   Se preferir montar à mão, copie `colaborador\clientes_colaborador_MODELO.csv` para `config\clientes.csv` e preencha só a coluna `senha`
   (salve como **CSV UTF-8**).

> Colunas do arquivo: `numero,apelido,nome_painel,cnpj,usuario,senha,aceitar_avisos`.
> `usuario` é o CNPJ com 14 dígitos (login do DecWeb). `aceitar_avisos` fica em branco (veja "Receita zero" mais abaixo).

### Passo 6. Teste sem enviar nada (obrigatório na primeira vez)
1. Abra o Claude Code na pasta `C:\Robos\decweb` (projeto do **fechamento fiscal**).
2. Peça: *"Fechamento fiscal, DecWeb: gerar o comando da Fase 1 (cria e baixa, SEM enviar) da competência MM/AAAA para a empresa 92."*
3. Cole o comando no Prompt de Comando (o Claude entrega algo como
   `python decweb_login.py --competencia 09/2026 --fase 1 --clientes 92`).
4. O Chrome abre sozinho, faz login e baixa os relatórios. **Não use esse Chrome enquanto roda.**
5. Confira em `...\09_SETEMBRO\002 ARQUIVOS MUNICIPAIS` os zips de Prestados e Tomados e em `logs\resumo_atual.csv` o status.
6. Se deu certo, a instalação está pronta.

---

## Parte B. Rotina de todo mês

1. **Avise a Fernanda** que vai rodar e confirme a **competência** (o mês anterior ao atual, ex.: em outubro roda `09/2026`).
2. Abra o Claude Code do fechamento fiscal e peça o comando (modelo pronto em `colaborador\CLAUDE_COLABORADOR.md`):
   > *Fechamento fiscal, DecWeb, competência MM/AAAA. Gerar o comando para todas as empresas do meu clientes.csv.
   > Primeiro a Fase 1 (sem enviar) para eu conferir; depois eu confirmo e você gera o comando com envio.*
3. Rode primeiro a **Fase 1** (cria a declaração e baixa os zips, não envia). Confira em `resumo_atual.csv`
   se todas as empresas aparecem com `zips_baixados` e sem pendência.
4. Confira os valores no DecWeb quando o robô avisar de nota ou aviso estranho (veja "Avisos").
5. Só então peça o comando de envio e rode. **O envio é irreversível e sem pausa.** Fase T (tudo):
   ```
   python decweb_login.py --competencia 09/2026 --fase T --clientes todos --enviar
   python decweb_login.py --competencia 09/2026 --fase T --clientes 92,210 --enviar
   ```
   Comece por poucas empresas na primeira vez; depois `--clientes todos`.
6. Ao terminar, abra `logs\resumo_atual.csv` (empresa por empresa: `declaracao_criada;zips_baixados;enviada;pdf_baixado`).
   Mande o resumo para a Fernanda (o arquivo **não** tem senha). Se algo falhou, peça ao Claude para rodar só as que faltaram.
7. Os PDFs ficam no Drive em `002 ARQUIVOS MUNICIPAIS` do mês, com o nome
   `{n}_{apelido}_PortoAlegre_MM.AAAA_DeclaraçãoMensal.pdf` e `..._ISSQN.pdf`.

### Regras do escritório (não discutir)
- **O robô não escreve na Controle_Fiscal.** Quem atualiza a planilha é a Fernanda, com a sua informação.
- **Guia só conta como enviada com a comprovação do G-Click.** Gerar a guia e salvar no Drive não é enviar ao cliente.
  A **declaração da prefeitura** é diferente: o recibo da própria prefeitura comprova o envio.
- **O prazo é o impresso na guia** ("Não receber esta guia após dd/mm/aaaa"). Nunca deduza data: confira a guia.
- Se a competência **já tem declaração enviada**, o robô **não cria outra**; ele registra pendência. Retificar só com a Fernanda (`--retificadora`).

### Avisos "Não foi informado serviço prestado/tomado"
- **Com notas no relatório baixado**: o robô segue sozinho e anota `aviso_escrituracao_aceito`; confira o valor da guia.
- **Sem notas** (receita zero): o robô **para** e registra pendência. Só marque `sim` em `aceitar_avisos` do `clientes.csv`
  para a empresa que a **Fernanda confirmou** que não teve receita no mês. Nunca para todas.

### Se der problema
| Sintoma | O que fazer |
|---|---|
| "Não achei clientes.csv" | refaça o Passo 5 |
| Login recusado | senha do DecWeb mudou: peça a nova à Fernanda e rode `montar_clientes.py` de novo |
| Chrome fecha ou trava no meio | rode de novo só as empresas que faltaram (o robô retoma; se já enviou, pula direto para o PDF) |
| Pendência de cadastro no DecWeb (responsável desatualizado etc.) | o robô pula a empresa; resolva no site e avise a Fernanda |
| Nenhuma nota em várias empresas seguidas | sinal de alerta: confira o log antes de aceitar |
| Erro de Python/biblioteca | `pip install -r requirements.txt` de novo |

Em erro ou pendência, o robô salva imagem e HTML da tela em `logs\diagnostico\`. Mande esses arquivos à Fernanda
(**nunca** o `clientes.csv`).

---

## Parte C. Segurança das senhas
- `config\clientes.csv`: só no seu PC, fora do Meu Drive. Não anexe a e-mail, WhatsApp, chat ou repositório.
- Não cole senha no Claude Code. O Claude só precisa de **número, apelido e competência**.
- Apague o CSV exportado da planilha assim que montar o `clientes.csv`.
- Se trocar de computador ou sair do escritório, apague a pasta `C:\Robos\decweb`.

---

## Empresas deste pacote (22)
| Nº | Apelido (nome nos arquivos) | Empresa | Obs. |
|---|---|---|---|
| 1 | FPVanzetto | FP Vanzetto | |
| 11 | StarCeo | StarCeo | |
| 34 | EFSConsulting | EFS Consulting | |
| 75 | VCTAudiodub | VCT Audiodub | |
| 79 | HomeroZenker | Homero Zenker | |
| 85 | BergmannMassaro | Bergmann & Massaro | |
| 92 | RFS | RFS | |
| 93 | Flaviarte | Flaviarte | |
| 115 | Projeta | Projeta | |
| 148 | ARS | ARS | **sem senha na planilha** |
| 158 | Joga | Joga | |
| 164 | PorticoJobLeite | Pórtico (Job e Leite) | |
| 167 | BMSoft | BMSoft | |
| 169 | DMSouza | DM Souza | |
| 176 | BelaVistaSul | Bela Vista Sul | |
| 199 | F8Gestao | F8 Gestão | |
| 210 | OfficeCont | OfficeCont | |
| 213 | GCL | GCL | **sem senha na planilha** |
| 222 | RCBertoglio | RC Bertoglio Arquitetura | **senha "-" na planilha** |
| 226 | LDG | LDG | |
| 230 | FRB | FRB | |
| 236 | PeludosDaMontanha | Peludos da Montanha | inscrição estadual consta como BAIXADA: confirmar com a Fernanda se ainda declara no município |

Fora do pacote (não são de Porto Alegre): 38 Valmac, 44 STN, 216 Maricota, 235 Sandra Carvalho.

**Apelidos:** são os nomes que o robô usa nos arquivos. Se o escritório já usa outro nome para a empresa nas pastas do Drive,
a Fernanda corrige a coluna `apelido` no `montar_clientes.py` (lista `CLIENTES`) antes da primeira rodada, para o robô não criar arquivos com outro nome.
