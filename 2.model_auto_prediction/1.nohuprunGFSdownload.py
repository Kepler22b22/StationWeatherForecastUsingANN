#!/opt/anaconda3/bin/python3

import os
import datetime

current_time = datetime.datetime.now()
year         = str(current_time.year).zfill(4)
month        = str(current_time.month).zfill(2)
day          = str(current_time.day).zfill(2)

if not os.path.exists(year+month+day):
    os.system('mkdir '+year+month+day)

for hour in range(3,60,3):
    hour = str(hour).zfill(3)
    os.system('nohup /opt/anaconda3/bin/python3 1.GFS_download.py '+year+' '+month+' '+day+' '+hour+' > '+year+month+day+'.log 2>&1 &')
hour = '060'
os.system('nohup /opt/anaconda3/bin/python3 1.GFS_download.py '+year+' '+month+' '+day+' '+hour+' > '+year+month+day+'.log 2>&1')
os.system('mv *gfs* '+year+month+day)

for hour in range(63,120,3):
    hour = str(hour).zfill(3)
    os.system('nohup /opt/anaconda3/bin/python3 1.GFS_download.py '+year+' '+month+' '+day+' '+hour+' > '+year+month+day+'.log 2>&1 &')
hour = '120'
os.system('nohup /opt/anaconda3/bin/python3 1.GFS_download.py '+year+' '+month+' '+day+' '+hour+' > '+year+month+day+'.log 2>&1')
os.system('mv *gfs* '+year+month+day)
    
for hour in range(123,180,3):
    hour = str(hour).zfill(3)
    os.system('nohup /opt/anaconda3/bin/python3 1.GFS_download.py '+year+' '+month+' '+day+' '+hour+' > '+year+month+day+'.log 2>&1 &')
hour = '180'
os.system('nohup /opt/anaconda3/bin/python3 1.GFS_download.py '+year+' '+month+' '+day+' '+hour+' > '+year+month+day+'.log 2>&1')
os.system('mv *gfs* '+year+month+day)

os.system('mv '+year+month+day+'.log '+year+month+day)
print(year+month+day+'_GFS download is finished')
