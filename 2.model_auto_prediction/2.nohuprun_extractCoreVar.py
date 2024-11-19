#!/opt/anaconda3/bin/python3
# Need correct working directory as .

import os
import datetime

current_time = datetime.datetime.now()
year         = str(current_time.year).zfill(4)
month        = str(current_time.month).zfill(2)
day          = str(current_time.day).zfill(2)

if not os.path.exists(year+month+day+'nc'):
    os.system('mkdir '+year+month+day+'nc')

pathin  = year+month+day
pathout = year+month+day+'nc/'

print('=================================')
print(year+month+day+' is extracting...')
    
for hour in range(3,60,6):
    hour = str(hour).zfill(3)
    os.system('nohup ./2.extract3.py '+pathin+'/gfs.t00z.pgrb2.1p00.f'+hour+ ' '+pathout+year+month+day+hour+'.nc > extract.log 2>&1 &')
hour = '057'
os.system('nohup ./2.extract3.py '+pathin+'/gfs.t00z.pgrb2.1p00.f'+hour+ ' '+pathout+year+month+day+hour+'.nc > extract.log 2>&1')

for hour in range(63,120,6):
    hour = str(hour).zfill(3)
    os.system('nohup ./2.extract3.py '+pathin+'/gfs.t00z.pgrb2.1p00.f'+hour+ ' '+pathout+year+month+day+hour+'.nc > extract.log 2>&1 &')
hour = '117'
os.system('nohup ./2.extract3.py '+pathin+'/gfs.t00z.pgrb2.1p00.f'+hour+ ' '+pathout+year+month+day+hour+'.nc > extract.log 2>&1')

for hour in range(123,180,6):
    hour = str(hour).zfill(3)
    os.system('nohup ./2.extract3.py '+pathin+'/gfs.t00z.pgrb2.1p00.f'+hour+ ' '+pathout+year+month+day+hour+'.nc > extract.log 2>&1 &')
hour = '177'
os.system('nohup ./2.extract3.py '+pathin+'/gfs.t00z.pgrb2.1p00.f'+hour+ ' '+pathout+year+month+day+hour+'.nc > extract.log 2>&1')


for hour in range(6,60,6):
    hour = str(hour).zfill(3)
    os.system('nohup ./2.extract6.py '+pathin+'/gfs.t00z.pgrb2.1p00.f'+hour+ ' '+pathout+year+month+day+hour+'.nc > extract.log 2>&1 &')
hour = '060'
os.system('nohup ./2.extract6.py '+pathin+'/gfs.t00z.pgrb2.1p00.f'+hour+ ' '+pathout+year+month+day+hour+'.nc > extract.log 2>&1')

for hour in range(66,120,6):
    hour = str(hour).zfill(3)
    os.system('nohup ./2.extract6.py '+pathin+'/gfs.t00z.pgrb2.1p00.f'+hour+ ' '+pathout+year+month+day+hour+'.nc > extract.log 2>&1 &')
hour = '120'
os.system('nohup ./2.extract6.py '+pathin+'/gfs.t00z.pgrb2.1p00.f'+hour+ ' '+pathout+year+month+day+hour+'.nc > extract.log 2>&1')

for hour in range(126,180,6):
    hour = str(hour).zfill(3)
    os.system('nohup ./2.extract6.py '+pathin+'/gfs.t00z.pgrb2.1p00.f'+hour+ ' '+pathout+year+month+day+hour+'.nc > extract.log 2>&1 &')
hour = '180'
os.system('nohup ./2.extract6.py '+pathin+'/gfs.t00z.pgrb2.1p00.f'+hour+ ' '+pathout+year+month+day+hour+'.nc > extract.log 2>&1')


print('done!')    
