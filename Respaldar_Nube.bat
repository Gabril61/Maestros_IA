@echo off
echo ========================================================
echo       RESPALDO AUTOMATICO TEXTILFIT M.A.S.
echo ========================================================
echo.
echo Detectando cambios en los archivos maestros...

cd /d "C:\Users\Ricx18\Desktop\Maestros_IA"

git add .
git commit -m "Respaldo Automatico: %date% %time%"
git push origin main

echo.
echo Sincronizando patrones con el Bot Generador local...
xcopy /Y /D "*.val" "..\App_Formulario\TextilFit_Bot\Maestros\"
xcopy /Y /D "*.smis" "..\App_Formulario\TextilFit_Bot\Maestros\"
echo.
echo ========================================================
echo       RESPALDO COMPLETADO EXITOSAMENTE
echo Sincronizando patrones con el Bot Generador local...
xcopy /Y /D "*.val" "..\App_Formulario\TextilFit_Bot\Maestros\"
xcopy /Y /D "*.smis" "..\App_Formulario\TextilFit_Bot\Maestros\"
echo.
echo ========================================================
timeout /t 5
