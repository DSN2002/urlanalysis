@echo off
set command=%~1%
set updata_url=%~2%
set down_path=%~dp0updata
cd %down_path%
set name=check.txt
if %command%==1 (
    echo "��ǰ��ִ��1��������������"
    powershell curl -o %name% %updata_url%
)
if %command%==2 (
    echo "��ǰ��ִ��2��������ظ����ļ�"
    powershell curl %updata_url%
)
