# Acrescenta o cliente 265 (BELEM BRASIL) ao clientes.csv do DecWeb, SEM apagar as outras linhas.
# A senha é digitada aqui, na hora, no PC: não fica neste arquivo, no repositório nem no chat.
# Faz cópia de segurança (clientes.csv.bak_DATA) na mesma pasta (fora do Meu Drive) antes de mexer.
$ErrorActionPreference = 'Stop'
$arq = 'C:\Robos\decweb\config\clientes.csv'
$numero = '265'
$apelido = 'BelemBrasil'
$painel = 'BELEM BRASIL ARQUITETURA E PARTICIPACOES LTDA'
$cnpj = '69405790000191'
$usuario = '69405790000191'

if (-not (Test-Path $arq)) { throw "Não achei $arq" }
$linhas = Get-Content -Path $arq -Encoding UTF8
$cab = ($linhas | Select-Object -First 1).TrimStart([char]0xFEFF)
if ($cab -ne 'numero,apelido,nome_painel,cnpj,usuario,senha,aceitar_avisos') {
    throw "Cabeçalho inesperado: $cab"
}
foreach ($l in $linhas | Select-Object -Skip 1) {
    if (($l -split ',')[0].Trim() -eq $numero) { throw "O cliente $numero já existe no arquivo. Nada foi alterado." }
}

$sec = Read-Host -Prompt "Digite a senha do DecWeb do 265 (não aparece na tela)" -AsSecureString
$senha = [System.Net.NetworkCredential]::new('', $sec).Password
if ([string]::IsNullOrWhiteSpace($senha)) { throw 'Senha vazia. Nada foi alterado.' }

function CsvCampo([string]$v) {
    if ($v -match '[",\r\n]') { return '"' + ($v -replace '"', '""') + '"' }
    return $v
}
$nova = (@($numero, $apelido, $painel, $cnpj, $usuario, $senha, '') | ForEach-Object { CsvCampo $_ }) -join ','

Copy-Item $arq ($arq + '.bak_' + (Get-Date -Format 'yyyyMMdd_HHmmss'))
$bruto = [System.IO.File]::ReadAllText($arq)
$prefixo = ''
if ($bruto.Length -gt 0 -and -not $bruto.EndsWith("`n")) { $prefixo = "`r`n" }
[System.IO.File]::AppendAllText($arq, $prefixo + $nova + "`r`n", (New-Object System.Text.UTF8Encoding($false)))
Write-Host "Cliente $numero incluído em $arq (senha não exibida)." -ForegroundColor Green
Write-Host "Conferência: abra o arquivo e veja a última linha. Não envie esse arquivo a ninguém."
