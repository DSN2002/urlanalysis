@echo off
set command=%~1%
set updata_url=%~2%
set down_path=%~dp0updata
cd %down_path%
set name=check.txt
if %command%==1 (
    echo "当前在执行1号命令，检测程序更新"
    powershell curl -o %name% %updata_url%
)
if %command%==2 (
    echo "当前在执行2号命令，下载更新文件"
    powershell curl %updata_url%
)
