@echo off

cls

rem Vers�o do script: 0.1.2r
rem Data da cria��o: 18/09/2022
rem Data da revis�o: 03/10/2022

::Altera a pagina do cmd para 1252 trabalhando assim com acentos e caracteres especiais
chcp 1252 >nul 2>&1

::Define o caminho do script
set folderScript=%~dp0
cd %folderScript%

::Vers�o do script
set version=Script V0.4.2r

::Define as variaveis dos arquivos tempor�rio
set returnMenu=%tmp%\returnMenu.txt

