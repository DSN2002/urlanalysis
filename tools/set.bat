@echo off
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c "^&chr(34)^&"%~0"^&chr(34)^&" ::","%cd%","runas",1)(window.close)&&exit
set BASE_DIR=%~dp0
set BASE_DIR=%BASE_DIR:~0,-1%
for %%d in (%BASE_DIR%) do set BASE_DIR=%%~dpd
set mpv_path=%BASE_DIR%MPV
set ffmpeg_path=%BASE_DIR%ffmpeg\bin;%mpv_path%
start %BASE_DIR%MPV\installer\mpv-install.bat
setx "path" "%ffmpeg_path%;%path%"

