@echo off
set command=%~1%
if %command%==1 (
    echo "当前在执行1号命令，检测程序更新"
    set updata_url=%~2%
    set down_path=%~dp0
    cd /d %down_path%
    cd updata
    set name=check.txt
    powershell curl -o "%name%" "%updata_url%"
)
if %command%==2 (
    echo "当前在执行2号命令，下载更新文件"
    set updata_url=%~2%
    set down_path=%~dp0
    cd /d %down_path%
    cd updata
    powershell curl -o "%name%" "%updata_url%"
)
