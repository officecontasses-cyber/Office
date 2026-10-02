@echo off
rem Abre o Chrome no perfil dedicado do robo para instalar a extensao (so uma vez).
rem Clique em "Usar no Chrome" e depois FECHE a janela.
if not exist "C:\PortalNacionalRobo\perfil_chrome_robo" mkdir "C:\PortalNacionalRobo\perfil_chrome_robo"
set CHROME="C:\Program Files\Google\Chrome\Application\chrome.exe"
if not exist %CHROME% set CHROME="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
start "" %CHROME% --user-data-dir="C:\PortalNacionalRobo\perfil_chrome_robo" https://chromewebstore.google.com/detail/baixar-nfse-nota-fiscal-d/enehmclajcndmgefbmjhecccoegbdgea
