# Guia passo a passo: robô do Portal Nacional (notas fiscais) no seu computador

**Para que serve:** o robô entra sozinho no Portal Nacional da NFS-e (nfse.gov.br) com o certificado digital de cada empresa,
baixa as planilhas de notas **Emitidas** e **Recebidas** do mês e salva no Drive, já com o nome certo.
Você instala uma vez e, todo mês, pede ao Claude o comando e cola numa janela.

**Diferença para o robô do DecWeb:** aqui **não tem senha**. O robô entra com o **certificado digital** de cada empresa,
que precisa estar instalado no seu Windows (Passo 6).

**Se travar em qualquer passo:** abra o Claude, diga em qual passo está e o que apareceu na tela (pode mandar um print).
**Nunca escreva ou cole senhas de certificado para o Claude.**

Tempo da instalação: cerca de 40 minutos, uma única vez.

---

## PARTE 1. Instalar (uma vez só)

### Passo 1. Chrome e Python
- Precisa do **Google Chrome**.
- Precisa do **Python**. Se você já instalou o robô do DecWeb, **já está pronto, pule para o Passo 2**.
  Se não: abra **python.org/downloads**, baixe, abra o arquivo, **marque a caixinha "Add python.exe to PATH"** (embaixo, na primeira tela) e clique em **Install Now**.

### Passo 2. Trazer o robô para o seu computador
1. No disco **C:** deve existir a pasta **Robos** (se não existir, crie: botão direito > Novo > Pasta).
2. No Drive, abra: `1015_ROTINA AUTOMATICA` > `002 FISCAL CAMILA` > `ROBO PORTAL NACIONAL`.
3. Baixe o arquivo **portalnacional.zip** e coloque dentro de `C:\Robos`.
4. Clique com o botão direito no zip > **Extrair tudo** > Extrair.
5. Confira: deve existir a pasta **C:\Robos\portalnacional** com vários arquivos dentro (um deles chama `portal_nacional_download.py`).

> Essa pasta **não** pode ficar dentro do Meu Drive. Fica em `C:\Robos`, ao lado da pasta `decweb`.

### Passo 3. Instalar as peças
1. Aperte a tecla **Windows**, digite **cmd** e aperte **Enter**. Abre uma janela preta.
2. Digite e aperte **Enter**:
   ```
   cd C:\Robos\portalnacional
   ```
3. Digite e aperte **Enter**:
   ```
   pip install -r requirements.txt
   ```
4. Espere terminar (aparece algo como "Successfully installed" no fim).

### Passo 4. Dizer ao robô onde fica a pasta do fechamento no seu Drive
**Se você já fez isso no robô do DecWeb:** abra `C:\Robos\decweb\config`, copie o arquivo **configuracao.ini**, cole em
`C:\Robos\portalnacional\config` e pronto.

**Se ainda não fez:**
1. Abra a pasta `C:\Robos\portalnacional\config`.
2. Copie **configuracao.exemplo.ini**, cole na mesma pasta e troque o nome da cópia para **configuracao.ini**.
3. Abra com o Bloco de Notas (botão direito > Abrir com > Bloco de Notas).
4. Ache a linha `raiz_fechamento =` e troque o caminho depois do `=` pelo da sua máquina: abra a pasta **001_FECHAMENTO FISCAL**
   (a que tem dentro `08_AGOSTO`, `09_SETEMBRO`...), clique na barra de endereço, **Ctrl + C**, volte ao Bloco de Notas e cole.
5. **Ctrl + S** para salvar.

### Passo 5. Lista de empresas
A lista já vem pronta em `C:\Robos\portalnacional\config\clientes.csv` (26 empresas). Não precisa mexer.
Ela não tem senhas, mas tem CNPJs de clientes: **não mande para fora do escritório**.

### Passo 6. Instalar os certificados digitais das empresas
O portal só deixa o robô entrar com o certificado da empresa. Cada certificado (arquivo **.pfx**) precisa estar instalado no seu Windows.

Para cada empresa:
1. Peça à **Fernanda** o arquivo `.pfx` do certificado e a senha dele (a Fernanda diz onde estão). **A senha não vai para o Claude.**
2. Dê **dois cliques** no arquivo `.pfx`. Abre um assistente.
3. Marque **Usuário Atual** e clique em **Avançar**. Avançar de novo.
4. Digite a **senha do certificado** e clique em **Avançar**. (Não precisa marcar nenhuma outra opção.)
5. Deixe marcada a opção "Selecionar automaticamente o repositório" e clique em **Avançar** e depois **Concluir**.
6. Aparece "A importação obteve êxito". Pronto.

Empresa **sem certificado, ou com certificado vencido, é pulada** pelo robô. Isso não trava as outras.

Depois de instalar os que tiver, confira quem está com certificado válido. Na janela preta:
```
cd C:\Robos\portalnacional
python portal_nacional_download.py --verificar-certificados
```
Abra o arquivo `C:\Robos\portalnacional\logs\certificados_status.csv` (abre no Excel). Ele mostra, empresa por empresa, se o certificado foi
encontrado e se está na validade. **Guarde essa lista**: você vai usar no teste.

### Passo 7. Instalar a extensão do Chrome (é ela que baixa as planilhas)
1. Na pasta `C:\Robos\portalnacional`, dê **dois cliques** em **instalar_extensao.bat**.
2. O Chrome abre numa janela própria do robô, na página da extensão "Baixar NFSe Nota Fiscal de Serviço Eletrônica Emitidas e Recebidas".
3. Clique no botão **Usar no Chrome** (ou "Adicionar ao Chrome") e confirme.
4. **Feche a janela.**

> Essa extensão só pode ficar nesse Chrome do robô. Não use essa janela para mais nada.

### Passo 8. Primeiro teste
1. Escolha uma empresa que apareceu com certificado válido no Passo 6 (anote o número dela, por exemplo `92`).
2. Abra o seu Claude do fechamento fiscal (o mesmo do robô do DecWeb; se for a primeira vez, cole o texto do arquivo **CLAUDE_COLABORADOR.md**) e escreva:
   > Fechamento fiscal, Portal Nacional, competência 09/2026, empresa 92. Gere o comando.
3. Ele dá um comando parecido com:
   ```
   python portal_nacional_download.py --competencia 09/2026 --clientes 92
   ```
4. Na janela preta, entre na pasta (`cd C:\Robos\portalnacional`), cole o comando (botão direito do mouse) e aperte Enter.
5. O Chrome abre sozinho, entra no portal e baixa as planilhas. **Não mexa nesse Chrome.** Pode levar alguns minutos (empresas com muitas notas demoram mais).
6. Quando acabar, abra no Drive a pasta `09_SETEMBRO` > `003 ARQUIVOS PORTAL NACIONAL`. Devem aparecer arquivos como
   `92_RFS_PortoAlegre_09.2026_Emitidas.xlsx` e `..._Recebidas.xlsx`. Empresa sem nenhuma nota no período **não gera arquivo** (fica "sem movimento").

Se apareceu, **a instalação está pronta.** Se deu erro, veja a Parte 3.

---

## PARTE 2. Todo mês (a rotina)

1. **Avise a Fernanda** que vai rodar e combine o mês. Em geral é o mês anterior (em outubro, `09/2026`).
2. Abra o Claude e escreva:
   > Fechamento fiscal, Portal Nacional, competência MM/AAAA, todas as empresas. Gere o comando.
3. Na janela preta (dentro de `C:\Robos\portalnacional`), cole o comando e deixe rodar. **Pode levar bastante tempo**:
   deixe o computador ligado, sem hibernar, e não mexa no Chrome do robô.
4. Quando terminar, abra o arquivo `C:\Robos\portalnacional\logs\resultados.csv`, copie o conteúdo e cole para o Claude pedir um resumo.
   Cada empresa aparece com um destes resultados:
   - **baixado**: deu certo, o arquivo está no Drive;
   - **sem_movimento**: a empresa não teve nota no período (não gera arquivo);
   - **login_falhou**: certificado ausente ou vencido (o motivo vem escrito);
   - **erro**: algo falhou naquela empresa; rode de novo só ela.
5. Mande o resumo para a Fernanda.

**Atenção a esta armadilha:** se **várias empresas seguidas** aparecerem como "sem movimento", **pare e avise a Fernanda**, não aceite.
Isso já aconteceu uma vez, quando o portal ficou logado numa empresa só. O robô agora limpa a sessão a cada empresa, mas a Fernanda quer conferir.

**Sobre o período:** o robô baixa do dia 1 do mês pedido até o último dia do mês seguinte (competência 09/2026 baixa de 01/09 a 31/10),
para pegar notas lançadas depois. Isso é normal.

---

## PARTE 3. Se algo der errado

| O que apareceu | O que fazer |
|---|---|
| "python não é reconhecido" | Refaça a instalação do Python e marque "Add python.exe to PATH". |
| `login_falhou` numa empresa | Certificado ausente ou vencido. Peça o certificado novo à Fernanda e instale (Passo 6). |
| `erro` numa empresa | O portal do governo às vezes cai. Rode o comando de novo só para ela. O robô já tenta 3 vezes sozinho. |
| O Chrome não abre ou trava logo no início | Feche todas as janelas do Chrome do robô e tente de novo. |
| Faltou a extensão | Refaça o Passo 7. |
| Arquivo foi para a pasta `_QUARENTENA_cnpj_divergente` | O CNPJ da planilha não bateu com o da empresa. Não use o arquivo: avise a Fernanda. |
| Várias empresas seguidas "sem movimento" | Pare e avise a Fernanda. |
| Outro erro | Mande à Fernanda o `resultados.csv` e um print da janela preta. |

---

## PARTE 4. Cuidados
- Os certificados ficam instalados só no seu Windows. **Não mande .pfx nem senha de certificado por WhatsApp, e-mail ou pelo Claude.**
- Use só o Chrome do robô para esse trabalho (a extensão é de terceiros).
- O Windows guarda um pequeno ajuste do Chrome enquanto o robô roda e apaga sozinho no fim. Não precisa fazer nada.
- Se sair do escritório ou trocar de computador, remova os certificados do Windows e apague `C:\Robos` e `C:\PortalNacionalRobo`.

---

## As 26 empresas do robô
1 FP Vanzetto · 11 StarCeo · 34 EFS Consulting · 38 Valmac (Tubarão/SC) · 44 STN (Caxias do Sul/RS) · 75 VCT Audiodub · 79 Homero Zenker ·
85 Bergmann & Massaro · 92 RFS · 93 Flaviarte · 115 Projeta · 148 ARS · 158 Joga · 164 Pórtico Job e Leite · 167 BMSoft · 169 DM Souza ·
176 Bela Vista Sul · 199 F8 Gestão · 210 OfficeCont · 213 GCL · 216 Maricota (Palhoça/SC) · 222 RC Bertoglio · 226 LDG · 230 FRB ·
235 Sandra Carvalho (Canoas/RS) · 236 Peludos da Montanha.

Diferente do DecWeb, aqui entram **todas**, inclusive as de fora de Porto Alegre, porque o Portal Nacional vale para qualquer cidade.
