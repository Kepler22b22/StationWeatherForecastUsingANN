#!/opt/anaconda3/bin/python3

import os
import datetime
import time

current_time = datetime.datetime.now()
print('begin time:')
print(current_time)

print('download begin...')
os.system('nohup /opt/anaconda3/bin/python3 1.nohuprunGFSdownload.py > download.log 2>&1')
print('download finished')

time.sleep(10)

print('extract core variables begin...')
os.system('nohup /opt/anaconda3/bin/python3 2.nohuprun_extractCoreVar.py > extract.log 2>&1')
print('extract core variables finished')

time.sleep(10)

print('predict begin...')
os.system('nohup /opt/anaconda3/bin/python3 3.nohuprun_readmodelandpredict.py > predict.log 2>&1')
print('predict finished')

time.sleep(10)

print('plot begin...')
os.system('nohup /opt/anaconda3/bin/python3 6.plot6dayT.py > plot6dayT.log 2>&1')
#os.system('nohup /opt/anaconda3/bin/python3 7.SendHTTPToMyTelephone.py >sendmesseage.log 2>&1')
print('plot finished')

print('npytoXml begin...')
os.system('nohup /opt/anaconda3/bin/python3 4.npytoxml.py > npytoxml.log 2>&1')
print('npytoXml finished')

time.sleep(10)


print('sendtoftp begin...')
os.system('nohup ./5.wputfile > wputfile.log 2>&1')
print('sendtoftp finished')

current_time = datetime.datetime.now()
print('end time:')
print(current_time)

time.sleep(10)

year  = str(current_time.year).zfill(4)
month = str(current_time.month).zfill(2)
day   = str(current_time.day).zfill(2)
os.system('rm -rf '+year+month+day)
#os.system('mv -r '+year+month+day+'nc '  + year+month+day+'predict')
os.system('mv 54401_'+year+month+day+'ANNpredict.npy '+ year+month+day+'predict')
os.system('mv 54401_'+year+month+day+'SLRpredict.npy '+ year+month+day+'predict')
os.system('mv 54401_'+year+month+day+'MLRpredict.npy '+ year+month+day+'predict')
os.system('mv 54401_'+year+month+day+'NWPpredict.npy '+ year+month+day+'predict')
os.system('mv '+year+month+day+'_begin_forecast54401.png '+ year+month+day+'predict')
os.system('cp '+year+month+day+'predict/*png ../../public_html')

