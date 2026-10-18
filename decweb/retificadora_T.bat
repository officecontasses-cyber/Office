@echo off
rem Retificadora DecWeb (fase T): abre a retificadora, ENVIA e baixa os PDFs. O envio e irreversivel.
cd /d "%~dp0"
set /p CLI=Numero(s) do cliente (ex: 133 ou 133,18): 
set /p COMP=Competencia [09/2026]: 
if "%COMP%"=="" set COMP=09/2026
echo.
echo Vai ABRIR retificadora, ENVIAR e BAIXAR a declaracao de %COMP% do(s) cliente(s) %CLI%.
set /p OK=Digite ENVIAR para confirmar: 
if /i not "%OK%"=="ENVIAR" goto fim
python decweb_login.py --competencia %COMP% --fase T --clientes %CLI% --retificadora --enviar
:fim
pause
