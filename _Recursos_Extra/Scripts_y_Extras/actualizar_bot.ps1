Write-Host "1. Moviendo index.html al App_Formulario real..."
Copy-Item -Path "C:\Users\Ricx18\Desktop\Cambios_App_Formulario\index.html" -Destination "C:\Users\Ricx18\Desktop\App_Formulario\index.html" -Force

Write-Host "2. Moviendo archivos Maestros al Bot..."
Copy-Item -Path "C:\Users\Ricx18\Desktop\Cambios_App_Formulario\Maestros\*" -Destination "C:\Users\Ricx18\Desktop\App_Formulario\TextilFit_Bot\Maestros" -Recurse -Force

Write-Host "3. Entrando a la carpeta del proyecto App_Formulario..."
Set-Location -Path "C:\Users\Ricx18\Desktop\App_Formulario"

Write-Host "4. Subiendo SOLO los archivos necesarios a Git (omitiendo la caché bloqueada del Bot)..."
git add index.html
git add TextilFit_Bot/bot.js
git add TextilFit_Bot/Maestros/
git commit -m "Automatizacion total de variables al estandar MAS"
git push

Write-Host "==============================="
Write-Host "PROCESO COMPLETADO EXITOSAMENTE"
Write-Host "==============================="
