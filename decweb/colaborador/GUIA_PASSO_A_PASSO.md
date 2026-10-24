# Guia passo a passo: robô do ISS de Porto Alegre no seu computador

**Para que serve:** o robô entra sozinho no site da Prefeitura de Porto Alegre (DecWeb), faz a declaração do mês de cada empresa,
envia e salva os PDFs no Drive. Você só instala uma vez e, todo mês, pede ao Claude o comando e cola numa janela.

**Se travar em qualquer passo:** abra o Claude, diga em qual passo está e o que apareceu na tela (pode tirar um print).
Ele te ajuda. **Nunca escreva ou cole senhas para o Claude.**

Tempo da instalação: cerca de 30 minutos, uma única vez.

---

## PARTE 1. Instalar (uma vez só)

### Passo 1. Confira o Google Chrome
O robô usa o Chrome. Se ele já está no computador, siga em frente.

### Passo 2. Instalar o Python (é o "motor" do robô)
1. Abra o site **python.org/downloads** e clique no botão amarelo de baixar.
2. Abra o arquivo baixado.
3. **Muito importante:** na primeira tela, marque a caixinha **"Add python.exe to PATH"** (fica embaixo). Depois clique em **Install Now**.
4. Quando terminar, clique em Close.

### Passo 3. Trazer o robô para o seu computador
1. No Explorador de Arquivos, abra o disco **C:** e crie uma pasta chamada **Robos** (botão direito > Novo > Pasta).
2. No Drive, abra: `1015_ROTINA AUTOMATICA` > `002 FISCAL CAMILA` > `ROBO DECWEB - PORTO ALEGRE`.
3. Baixe o arquivo **decweb.zip** e coloque dentro de `C:\Robos`.
4. Clique com o botão direito no zip > **Extrair tudo** > Extrair.
5. Confira: deve existir a pasta **C:\Robos\decweb** com vários arquivos dentro (um deles chama `decweb_login.py`).

> Por que fora do Drive? Porque o robô guarda as senhas das empresas e elas não podem ir para a nuvem.
> **Nunca coloque a pasta `decweb` dentro do Meu Drive.**

### Passo 4. Abrir a "janela preta" e instalar as peças
1. Aperte a tecla **Windows**, digite **cmd** e aperte **Enter**. Abre uma janela preta.
2. Digite o comando abaixo e aperte **Enter**:
   ```
   cd C:\Robos\decweb
   ```
3. Digite este e aperte **Enter**:
   ```
   pip install -r requirements.txt
   ```
4. Espere. Vão aparecer várias linhas e, no fim, algo como "Successfully installed". Pode levar alguns minutos.

### Passo 5. Dizer ao robô onde fica a pasta do fechamento no seu Drive
1. Abra a pasta `C:\Robos\decweb\config`.
2. Copie o arquivo **configuracao.exemplo.ini**, cole na mesma pasta e troque o nome da cópia para **configuracao.ini**.
3. Abra o **configuracao.ini** com o Bloco de Notas (botão direito > Abrir com > Bloco de Notas).
4. Ache a linha que começa com `raiz_fechamento =`. Depois do sinal de igual fica um caminho. Troque esse caminho pelo da sua máquina:
   - no Explorador de Arquivos, abra a pasta **001_FECHAMENTO FISCAL** (a que tem dentro as pastas `08_AGOSTO`, `09_SETEMBRO`...);
   - clique na barra de endereço lá em cima, aperte **Ctrl + C** para copiar o caminho;
   - volte ao Bloco de Notas e cole depois do `=`.
5. Aperte **Ctrl + S** para salvar e feche.

### Passo 6. Montar a lista de empresas com as senhas
A lista de empresas já está pronta no robô. Falta só colocar as senhas, que vêm da planilha de dados das empresas.
Você vai baixar a planilha, rodar um programa que monta a lista e apagar a planilha baixada.

1. Abra a planilha **"Clientes Simples - Dados_Completos"** (se não tiver acesso, peça à Fernanda).
2. Menu **Arquivo > Fazer download > Valores separados por vírgula (.csv)**.
3. Crie a pasta **C:\Robos\temp** e salve o arquivo baixado lá. Anote o nome do arquivo.
4. Na janela preta (se fechou, repita o Passo 4, itens 1 e 2), digite o comando abaixo trocando o nome do arquivo pelo seu, e aperte Enter:
   ```
   python colaborador\montar_clientes.py "C:\Robos\temp\NOME-DO-SEU-ARQUIVO.csv" --apagar-origem
   ```
5. O programa vai escrever quantas empresas montou. **Hoje o normal é aparecer 19 empresas**, e avisar que 3 ficaram de fora
   por falta de senha na planilha: **148 ARS, 213 GCL e 222 RC Bertoglio**. Isso é esperado. Peça as senhas à Fernanda e,
   quando ela atualizar a planilha, repita este passo.
6. O programa apaga sozinho a planilha baixada. Confira se ela sumiu de `C:\Robos\temp`; se não sumiu, apague.

> Essa lista (`clientes.csv`) tem senhas. Ela fica só no seu computador: não mande por WhatsApp, e-mail, Drive nem para o Claude.

### Passo 7. Primeiro teste, sem enviar nada
O teste serve para ver se está tudo funcionando. **Ele não envia declaração nenhuma.**

1. Abra o seu Claude do fechamento fiscal.
2. Cole para ele o texto do arquivo **CLAUDE_COLABORADOR.md** (está na mesma pasta do Drive do robô) ou peça "leia o arquivo CLAUDE_COLABORADOR.md".
3. Escreva para ele:
   > Fechamento fiscal, DecWeb, competência 09/2026, empresa 92. Gere o comando de teste, sem enviar.
4. Ele vai te dar um comando parecido com este:
   ```
   python decweb_login.py --competencia 09/2026 --fase 1 --clientes 92
   ```
5. Copie esse comando, vá na janela preta (já dentro de `C:\Robos\decweb`), cole (botão direito do mouse) e aperte Enter.
6. O Chrome abre sozinho, entra no site da Prefeitura e baixa os relatórios. **Não mexa no Chrome enquanto ele trabalha.**
7. Quando terminar, abra no Drive a pasta `09_SETEMBRO` > `002 ARQUIVOS MUNICIPAIS` e veja se apareceram arquivos da empresa 92.

Se apareceram, **a instalação está pronta.** Se deu erro, veja a Parte 3.

---

## PARTE 2. Todo mês (a rotina)

1. **Avise a Fernanda** que vai rodar e combine o mês. Em geral é o mês anterior (em outubro, roda `09/2026`).
2. Abra o Claude e escreva:
   > Fechamento fiscal, DecWeb, competência MM/AAAA, todas as empresas. Gere o comando de teste, sem enviar.
3. Cole o comando na janela preta e deixe rodar (pode demorar). Quando acabar, peça ao Claude para conferir o resultado:
   abra o arquivo `C:\Robos\decweb\logs\resumo_atual.csv` e cole o conteúdo para ele (esse arquivo não tem senha).
   Ele diz quais empresas deram certo e quais ficaram pendentes.
4. **Só depois de conferir**, escreva ao Claude: "Conferi, pode gerar o comando para enviar." Ele vai dar um comando com a palavra `--enviar`.
   **Enviar não tem volta.** Na primeira vez, envie só uma ou duas empresas.
5. Cole o comando, deixe rodar e confira de novo o `resumo_atual.csv`. Mande o resultado para a Fernanda.

Os PDFs (declaração, recibo e, quando há valor, a guia) ficam no Drive em `002 ARQUIVOS MUNICIPAIS` do mês.

### Regras do escritório
- **O robô não mexe na planilha de controle.** Quem atualiza é a Fernanda, com o que você informar.
- **Guia só vale como enviada ao cliente com a confirmação do G-Click.** Salvar o PDF no Drive não é enviar.
  O recibo da prefeitura comprova que a **declaração** foi enviada.
- **O vencimento é o que está escrito na guia.** Nunca calcule a data de cabeça.
- Se o mês **já tem declaração enviada**, o robô não cria outra e avisa. Não insista: fale com a Fernanda.
- Se o robô avisar "Não foi informado serviço" e a empresa não teve nenhuma nota, **ele para**. Fale com a Fernanda antes de seguir.

---

## PARTE 3. Se algo der errado

| O que apareceu | O que fazer |
|---|---|
| "python não é reconhecido" | O Python não foi instalado direito. Refaça o Passo 2 e marque a caixinha "Add python.exe to PATH". |
| "Não achei clientes.csv" | Refaça o Passo 6. |
| O site recusou o login de uma empresa | A senha mudou. Peça a nova à Fernanda e refaça o Passo 6. |
| O Chrome fechou no meio | Peça ao Claude o comando só para as empresas que faltaram e rode de novo. Pode repetir sem medo. |
| A empresa ficou "pendente" | O robô pulou por algum aviso do site (cadastro, por exemplo). Avise a Fernanda. |
| Várias empresas seguidas sem nota nenhuma | Pare e avise a Fernanda antes de aceitar. |
| Outro erro | Mande à Fernanda a imagem que o robô salva em `C:\Robos\decweb\logs\diagnostico`. **Nunca** mande o `clientes.csv`. |

---

## PARTE 4. Cuidados com as senhas
- A lista `clientes.csv` fica só no seu computador, na pasta `C:\Robos\decweb\config`.
- Não envie esse arquivo a ninguém e não cole senhas no Claude.
- Se trocar de computador ou sair do escritório, apague a pasta `C:\Robos`.

---

## As 22 empresas do robô
1 FP Vanzetto · 11 StarCeo · 34 EFS Consulting · 75 VCT Audiodub · 79 Homero Zenker · 85 Bergmann & Massaro · 92 RFS ·
93 Flaviarte · 115 Projeta · 148 ARS (sem senha na planilha) · 158 Joga · 164 Pórtico Job e Leite · 167 BMSoft · 169 DM Souza ·
176 Bela Vista Sul · 199 F8 Gestão · 210 OfficeCont · 213 GCL (sem senha na planilha) · 222 RC Bertoglio (sem senha na planilha) ·
226 LDG · 230 FRB · 236 Peludos da Montanha (a inscrição estadual consta como baixada; confirme com a Fernanda se ainda declara em Porto Alegre).

Ficam de fora porque não são de Porto Alegre: 38 Valmac, 44 STN, 216 Maricota e 235 Sandra Carvalho.
