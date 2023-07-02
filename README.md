# 树莓派实现 无线网卡ZTE-MF832S 开机自动拨号并连接服务器 
在实现树莓派开启热点拨号之后，发现一次次手动拨号过于繁琐，于是想着写个shell来实现开机之后自动化打开串口输入AT指令进行拨号，于是使用expect来实现自动化输入AT指令。 

同时为实时监控温度和远程控制树莓派，于是写个python来监控温度和RAM和磁盘情况。

（其实接入阿里云IOT更加容易）
## 文件结构 
> Kill.sh --- 清理内存脚本    
> Minicom.exp  --- 自动化拨号expect源码  
> Temperature.py  --- 监控温度python源码  
> Temperature.sh  --- 开启自动启动服务入口  
## ZTE-MF832S拨号串口命令 
```
    AT+CGDCONT=1,"IP"
    AT+CFUN=1
    AT+CEREG=1
    AT+CGREG?
    AT+CEREG?
    AT+ZGACT=1,1
    AT+CGPADDR=1
```
在minicom里面输入此AT指令即可拨号 
## 运行环境配置 
 ```bash
#minicom
sudo apt install minicom #安装minicom
sudo minicom -s #配置minicom --注意配置为9600并修改tty
#expect
sudo apt install  expect
sudo apt install expect-devel
sudo apt install tcl
#python
pip install requests
```
## 开机自动运行 
```bash
sudo vim /etc/rc.local 
#在exit 0 前加入：
#su pi -c 'exec ~/Temperature.sh'
```

## 说明 
具体操作得按自己的环境来,要求python2.x运行,并自己配置好后台服务器,python文件必须修改API接口才可以用
