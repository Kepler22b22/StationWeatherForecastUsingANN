# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 11:21:46 2020

@author: qyl
"""

import os
import time
import numpy as np
import pandas as pd
import datetime
current_time = datetime.datetime.now()
year         = str(current_time.year).zfill(4)
month        = str(current_time.month).zfill(2)
day          = str(current_time.day).zfill(2)
citysite = '54401'

for hour in range(3,60,3):
    hour = str(hour).zfill(3)
    os.system('nohup /opt/anaconda3/bin/python3 3.readmodelandpredict.py '+hour+' > '+hour+'.log 2>&1 &')
hour = '060'
os.system('nohup /opt/anaconda3/bin/python3 3.readmodelandpredict.py '+hour+' > '+hour+'.log 2>&1')

for hour in range(63,120,3):
    hour = str(hour).zfill(3)
    os.system('nohup /opt/anaconda3/bin/python3 3.readmodelandpredict.py '+hour+' > '+hour+'.log 2>&1 &')
hour = '120'
os.system('nohup /opt/anaconda3/bin/python3 3.readmodelandpredict.py '+hour+' > '+hour+'.log 2>&1')

for hour in range(123,180,3):
    hour = str(hour).zfill(3)
    os.system('nohup /opt/anaconda3/bin/python3 3.readmodelandpredict.py '+hour+' > '+hour+'.log 2>&1 &')
hour = '180'
os.system('nohup /opt/anaconda3/bin/python3 3.readmodelandpredict.py '+hour+' > '+hour+'.log 2>&1')

time.sleep(20)

os.system('mv *log logs')

Y_ANNpredict = np.zeros([5,60])
Y_SLRpredict = np.zeros([5,60])
Y_MLRpredict = np.zeros([5,60])
Y_NWPpredict = np.zeros([5,60])

for hour in range(3,181,3):
    hour = str(hour).zfill(3)
    Y_ANNpredict[:,int(int(hour)/3)-1] = np.load(citysite+'_'+year+month+day+hour+'ANNpredict.npy')
    os.system('rm -rf '+citysite+'_'+year+month+day+hour+'ANNpredict.npy')
    Y_SLRpredict[:,int(int(hour)/3)-1] = np.load(citysite+'_'+year+month+day+hour+'SLRpredict.npy')
    os.system('rm -rf '+citysite+'_'+year+month+day+hour+'SLRpredict.npy')
    Y_MLRpredict[:,int(int(hour)/3)-1] = np.load(citysite+'_'+year+month+day+hour+'MLRpredict.npy')
    os.system('rm -rf '+citysite+'_'+year+month+day+hour+'MLRpredict.npy')
    Y_NWPpredict[:,int(int(hour)/3)-1] = np.load(citysite+'_'+year+month+day+hour+'NWPpredict.npy')
    os.system('rm -rf '+citysite+'_'+year+month+day+hour+'NWPpredict.npy')
np.save(citysite+'_'+year+month+day+'ANNpredict.npy',Y_ANNpredict)
np.save(citysite+'_'+year+month+day+'SLRpredict.npy',Y_SLRpredict)
np.save(citysite+'_'+year+month+day+'MLRpredict.npy',Y_MLRpredict)
np.save(citysite+'_'+year+month+day+'NWPpredict.npy',Y_NWPpredict)



