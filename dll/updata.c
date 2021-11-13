/*
 * @Author: DSN2002
 * @Date: 2021-11-13 12:01
 * @LastEditTime: 2021-11-13 13:22
 * @LastEditors: DSN2002
 * @Description:
 * 仅供研究使用，请勿用于其他活动
 */

#include<stdlib.h>
#include<stdio.h>
#include<string.h>

void main()
{}
char powershell[] = {"powershell (new-object System.Net.WebClient).DownloadFile( "};
char dian[] = {'\''};
char link[] = {"\',\'"};
char kuohu[] = {"\')"};
void updata(char ulr[200],char path[200])
{//*下载新版本
    char mode [500];
    strcpy(mode,powershell);
    strcat(mode,dian);
    strcat(mode,ulr);
    strcat(mode,dian);
    strcat(mode,link);
    strcat(mode,path);
    strcat(mode,dian);
    printf("%s\n",mode);
    system(mode);
}
void upcheck(char ulr[200],char path[200])
{//*下载版本文件，检查更新
    char mode [500];
    strcpy(mode,powershell);
    strcat(mode,dian);
    strcat(mode,ulr);
    strcat(mode,dian);
    strcat(mode,link);
    strcat(mode,path);
    strcat(mode,dian);
    printf("%s\n",mode);
    system(mode);
}
