# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:20:52 2020

@author: qyl
"""

#!/opt/anaconda3/bin/python3
import os,shutil
if not os.path.exists('log'):
    os.mkdir('log')

#hours = ['048','072']
#citysites = ['53463']
#citysites = ['50953','51463','52866','53463','54662','54857','55591',
#             '56187','56778','57083','57494','58362','58847','59287','59758']
citysites = ['55591','59758']

for citysite in citysites:
    #for hour in hours:
    for hour in range(3,181,3):
        hour = str(hour).zfill(3)
        print(citysite+'_'+hour+'hour is calculating...')
        os.system('python 2.GFS_runModelandSave_allyear.py '+hour+' '+citysite+' > '+citysite+'_'+hour+'hour.log 2>&1')
        shutil.move(os.path.join('./'    , citysite+'_'+hour+'hour.log'),
                os.path.join('./log/', citysite+'_'+hour+'hour.log') )
print('done!')
