# Robô Portal Nacional NFS-e — OfficeCont

Baixa, por empresa, os relatórios **"Completa" de Emitidas e Recebidas** do Portal Nacional da NFS-e (nfse.gov.br),
entrando com o **certificado digital A1 da própria empresa** e usando a extensão de Chrome
*"Baixar NFSe Nota Fiscal de Serviço Eletrônica Emitidas e Recebidas"*. Salva e renomeia cada planilha por mês.
Não tem senha em nenhum arquivo: o login é só por certificado.

Adaptado em 02/10/2026 de um pacote de outro escritório. O que mudou:

| Assunto | Como ficou |
|---|---|
| Pasta de saída | `<raiz>\<MM_MES>\003 ARQUIVOS PORTAL NACIONAL` (a mesma raiz do DecWeb, no mesmo formato de `configuracao.ini`) |
| Período baixado | sai da **competência** pedida: do dia 1 dela ao último dia do mês seguinte (09/2026 → 01/09 a 31/10). Antes era relativo ao dia em que o robô rodava e perdia notas ao rodar meses depois |
| `clientes.csv` | aceita BOM do Excel, linhas em branco e CNPJ com pontuação; para com mensagem clara se faltar coluna ou o CNPJ não tiver 14 dígitos |
| Quarentena | `003 ARQUIVOS PORTAL NACIONAL\_QUARENTENA_cnpj_divergente` (a conferência do DecWeb não enxerga essa subpasta) |
| Conferência de CNPJ | normaliza a pontuação |

O nome do arquivo (`{n}_{apelido}_{cidade}_MM.AAAA_Emitidas.xlsx`) é achado pela conferência Prestados × Emitidas do
DecWeb (que também localiza pelo CNPJ dentro da planilha). Com o Portal Nacional de volta, basta ligar
`conferencia = sim` no `configuracao.ini` do DecWeb.

## Requisitos
- Windows, **Python 3.10+** e **Google Chrome**.
- Os **certificados e-CNPJ A1 das empresas instalados no Windows** (Certificados do Usuário Atual). O robô acha o
  certificado pelo CNPJ no nome (`RAZAO SOCIAL:CNPJ14`), escolhe sozinho e **pula** quem estiver sem certificado ou
  vencido (fica `login_falhou` no `logs\resultados.csv`, com o motivo).
- Pasta do robô em **disco local, caminho sem acento**, **fora do Meu Drive** (ex.: `C:\Robos\portalnacional`).
  O perfil do Chrome e os downloads temporários ficam em `C:\PortalNacionalRobo`.

## Instalação (uma vez)
1. Na pasta do robô: `pip install -r requirements.txt`
2. `config\configuracao.exemplo.ini` → `config\configuracao.ini` (pode copiar o do DecWeb; só a `raiz_fechamento` é usada).
3. `config\clientes.csv` com uma linha por empresa: `numero,apelido,razao_social,cnpj,cidade`
   (`numero` sem zeros à esquerda, como nos nomes dos arquivos do DecWeb; `apelido` e `cidade` sem espaços e sem acentos;
   UTF-8). Este arquivo tem CNPJs de clientes: **não vai para o repositório nem para o chat**.
4. Dê dois cliques em `instalar_extensao.bat`: o Chrome abre no perfil do robô. Clique em **Usar no Chrome** na extensão e
   **feche a janela**.

> A extensão é de terceiros e roda dentro da sessão logada no portal. Use apenas no perfil do robô (como acima).

## Uso
Primeiro veja quais empresas têm certificado válido (grava `logs\certificados_status.csv`):
```
python portal_nacional_download.py --verificar-certificados
```
Depois baixe (competência `MM/AAAA`; `todos` ou números separados por vírgula):
```
python portal_nacional_download.py --competencia 09/2026 --clientes 16,18
python portal_nacional_download.py --competencia 09/2026 --clientes todos
```
Sem `--competencia`/`--clientes`, o robô pergunta. `--manual` = você escolhe o certificado na janela do Windows.

Resultado: planilhas na `003` do mês; `logs\resultados.csv` (uma linha por empresa/tipo: `baixado`, `sem_movimento`,
`erro`, `login_falhou`).

## Cuidados
- **Confere o CNPJ** dentro da planilha antes de arquivar; se divergir, vai para a quarentena e o status fica `erro`.
- Enquanto roda, o robô grava por empresa uma política temporária do Chrome em `HKCU\Software\Policies\Google\Chrome`
  (seleção do certificado) e a **apaga ao terminar**. Não precisa de administrador.
- Não use o Chrome do robô ao mesmo tempo (o perfil trava com janela aberta).
- O portal do governo oscila (503, conexão resetada): o robô tenta 3 vezes e pula a empresa; é só rodar de novo.
- Empresas com muitas notas demoram (a extensão lê nota por nota; já levou ~5 min).
- Empresa sem notas no período: `sem_movimento`, nenhum arquivo é gerado.

## Testes (offline, sem navegador)
```
pip install -r requirements-dev.txt
python -m pytest tests -q
```
