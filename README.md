<!--
 * @Author: DSN2002
 * @Date: 2021-11-13 13:44
 * @LastEditTime: 2021-11-13 15:02
 * @LastEditors: DSN2002
 * @Description:
 * 仅供研究使用，请勿用于其他活动
-->

# 说明
这个脚本是调用python的you-get和youtube-dl来解析网页，来下载视频或者资源的，因为mpv播放器可以导入ulr来播放网络视频，且可以安装anime4k插件实时提升番剧的画质，对于480p，720p提升良好。
## 这个脚本可以做什么？
功能：<br>
1，将网络视频导入本地mpv播放器播放<br>
2，解析网络资源在服务器上的ulr<br>
3，下载网络资源<br>
4，显示网络资源的信息<br>
## 更新日志：

>2021.11.13  更新为2.1.0版本<br>
该版本提供了一个简单的图形化界面来操作命令行<br>
该版本修复了：<br>
1，解析带有`&`字符的ulr时的报错<br>
该版本添加了：<br>
1，自动更新<br>
2，针对bilbil的ulr的优化<br>
3，用户自定义设置视频存放路径与cookie的路径<br>
2021.09.18  更新使用youtube-dl指令的版本<br>
优化了多文件下载的文件夹命名<br>
2021.09.10  更新使用youtube-dl指令的版本<br>
修复了无法在线观看b站视频的问题<br>
2021.08.26  2.0版更新<br>
保留了1.0版本的大部分功能<br>
修复了：<br>
1，解析ulr时的报错<br>
2，解析文件信息时的报错<br>
添加了：<br>
1，将文件下载在D盘的video文件夹中，并且下载剧集时可以选择建立文件夹保存剧集<br>
2，对下载多文件的支持<br>
删除了：<br>
1，加载cookies观看在线视频的功能<br>
2，去除了一些重复的垃圾代码，精简了脚本<br>
2021.08.24  1.0版发布<br>
1.0版可以：<br>
1，导入视频或歌曲到mpv播放<br>
2，解析ulr并显示真实的ulr连接<br>
~~3，加载cookie以在线观看视频~~<br>
~~4，下载非会员或会员(需要cookie)观看的视频~~<br>
>5，解析ulr下所有文件的信息<br>

## 用到的所有程序的官方连接如下：
### [Anime4K](https://github.com/bloc97/Anime4K)
### [you-get](https://github.com/soimort/you-get)
### [mpv](https://mpv.io/)
### [you-get与Anime4K的使用方法blibli](https://www.bilibili.com/read/cv12828208)
### [youtube-dl](https://github.com/ytdl-org/youtube-dl)
### [DownKyi](https://github.com/leiurayer/downkyi)

## 关于Releases安装程序后
### 这些文件是些什么？
1，lazycode文件夹是存放脚本的主文件<br>
2，MPV文件夹是存放[`mpv播放器`](https://mpv.io/)的文件夹<br>
3，ffmpeg是存放[`ffmpeg程序`](https://ffmpeg.org/)的文件夹<br>
4，[`DownKyi`](https://github.com/leiurayer/downkyi)是另一个大佬写的专门下载bilbil资源的程序，可以与脚本配合完成下载某些bilbil视频<br>
### 这些文件里有些什么？
1，lazycode中的`dll`和`version`是存放脚本依赖的dll运行库和设置文件的文件夹<br>
2，ffmpeg中的文件夹不需要我们了解<br>
3，MPV文件夹内的`mpv`,`7z`,`doc`文件夹是mpv自己的运行文件不需要我们修改，我们需要打开的只有`installer`下的`mpv-install.bat`将mpv设置为默认播放器，当然不想用mpv了可以点击`mpv-uninstall.bat`进行卸载<br>
4，关于`portable_config`文件夹就比较复杂了，这个是存放mpv播放器的配置文件的文件夹,其中的`scripts`，`shaders`，`shaders_cache`，`watch_later`分别是mpv的脚本文件夹，着色器文件夹，着色器缓存文件夹，观看记录文件夹我都已经设置好了<br>
5，关于`portable_config`下的文件<br>
>1,input.conf 是键盘快捷键设置文件<br>
>2,mpv.conf 是mpv配置文件，前面带`#`的是标识了部分功能的未启用配置文件<br>
>3,anime4K使用说明.txt 是我整理的anime4k组合，可以根据提示自行更换到input.conf中的相应位置<br>
>4,anime4K.xlsx 是我渣翻后的各个anime4K模式说明。因为我电脑配置太渣所以用的是我自己的组合`(你们下载后的默认配置)`所以只有`A`,`B`,`C`和`默认配置`。`A+`,`B+`,`C+`请符合`anime4K使用说明`的用户自己尝试。
