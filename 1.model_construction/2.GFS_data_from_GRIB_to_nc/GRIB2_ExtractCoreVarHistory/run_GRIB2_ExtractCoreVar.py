#!/opt/anaconda3/bin/python3
import os
import time
import numpy as np
import pandas as pd
import datetime

year = '2020'
if not os.path.exists('../data/'+year+'/'+year+'nc'):
    os.mkdir('../data/'+year+'/'+year+'nc')

for hour in range(3,57,6):
    hour = str(hour).zfill(3)
    os.system('nohup python GRIB2_ExtractCoreVar3.py '+year+' '+hour+' > '+year+'_3.log 2>&1 &')
hour = '057'
os.system('nohup python GRIB2_ExtractCoreVar3.py '+year+' '+hour+' > '+year+'_3.log 2>&1')
          
for hour in range(63,117,6):
    hour = str(hour).zfill(3)
    os.system('nohup python GRIB2_ExtractCoreVar3.py '+year+' '+hour+' > '+year+'_3.log 2>&1 &')
hour = '117'
os.system('nohup python GRIB2_ExtractCoreVar3.py '+year+' '+hour+' > '+year+'_3.log 2>&1')
        
for hour in range(123,177,6):
    hour = str(hour).zfill(3)
    os.system('nohup python GRIB2_ExtractCoreVar3.py '+year+' '+hour+' > '+year+'_3.log 2>&1 &')
hour = '177'
os.system('nohup python GRIB2_ExtractCoreVar3.py '+year+' '+hour+' > '+year+'_3.log 2>&1')

for hour in range(6,60,6):
    hour = str(hour).zfill(3)
    os.system('nohup python GRIB2_ExtractCoreVar6.py '+year+' '+hour+' > '+year+'_6.log 2>&1 &')
hour = '060'
os.system('nohup python GRIB2_ExtractCoreVar6.py '+year+' '+hour+' > '+year+'_6.log 2>&1')
          
for hour in range(66,120,6):
    hour = str(hour).zfill(3)
    os.system('nohup python GRIB2_ExtractCoreVar6.py '+year+' '+hour+' > '+year+'_6.log 2>&1 &')
hour = '120'
os.system('nohup python GRIB2_ExtractCoreVar6.py '+year+' '+hour+' > '+year+'_6.log 2>&1')
        
for hour in range(126,180,6):
    hour = str(hour).zfill(3)
    os.system('nohup python GRIB2_ExtractCoreVar6.py '+year+' '+hour+' > '+year+'_6.log 2>&1 &')
hour = '180'
os.system('nohup python GRIB2_ExtractCoreVar6.py '+year+' '+hour+' > '+year+'_6.log 2>&1')

print('done')
