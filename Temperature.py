#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,requests,time,json
time.sleep(60)
 
# Return CPU temperature as a character string                                     
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
 
# Return RAM information (unit=kb) in a list                                      
# Index 0: total RAM                                                              
# Index 1: used RAM                                                                
# Index 2: free RAM                                                                
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            res = line.split()[1:4]
            return(round(100*int(res[1])/int(res[0]),2))


# Return % of CPU used by user as a character string                               
# def getCPUuse():
#     return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))
 
#Return disk %
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            res = line.split()[1:5]
            return res[3]
 
 


 




# Requests
url="输入的你的接口地址"

if __name__ == '__main__':
    while True:
        payload = {'device':'pi','temperature': getCPUtemperature(), 'RAM': getRAMinfo(),'Disk': getDiskSpace()[0:(getDiskSpace().find('%'))],'time':time.time(),'token':'输入token'}


        r = requests.get(url, params=payload)

        if r.status_code == 200:
            print('')
        else:
            print('Error')
            os.system("sudo nohup ~/Minicom.exp > Com.file 2>&1 &")
            time.sleep(60)
            continue

        print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()+8*60*60)))
        print('CPU Temperature = '+getCPUtemperature())
        print('RAM Used = '+str(getRAMinfo())+'%')
        print('DISK Used Percentage = '+str(getDiskSpace()[0:(getDiskSpace().find('%'))])+'%')
        print r.status_code
        print r.content
        print('')
        print(' ---------')
        print('')
        obj = json.loads(r.content)
        if obj["cmd"]!="null":
            os.system(obj["cmd"])
        time.sleep(float(obj["sleep"]))
