@echo off
set command=%~1%
if %command%==1 (
    echo "��ǰ��ִ��1��������������"
    set updata_url=%~2%
    set down_path=%~dp0
    cd /d %down_path%
    cd updata
    set name=check.txt
    powershell curl -o "%name%" "%updata_url%"
)
if %command%==2 (
    echo "��ǰ��ִ��2��������ظ����ļ�"
    set updata_url=%~2%
    set down_path=%~dp0
    cd /d %down_path%
    cd updata
    powershell curl -o "%name%" "%updata_url%"
)
