@echo off
title Servidor Controle de TVs
cd "C:\Users\Venda de Plano USER\CONTROLE REMOTO TVS"
adb connect 192.168.15.145
timeout /t 1 >nul

adb connect 192.168.15.128
timeout /t 1 >nul

adb connect 192.168.15.138
timeout /t 1 >nul

adb connect 192.168.15.131
timeout /t 1 >nul

adb connect 192.168.15.132
timeout /t 1 >nul

adb connect 192.168.15.130
timeout /t 1 >nul

adb connect 192.168.15.129
timeout /t 1 >nul

python app.py
pause
