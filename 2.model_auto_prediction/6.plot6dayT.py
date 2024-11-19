#!/opt/anaconda3/bin/python3
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import matplotlib
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname='/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc')
def toweekday(timein):
    if timein.weekday()==0:
        strout = '周日'
    elif timein.weekday()==1:
        strout = '周一'
    elif timein.weekday()==2:
        strout = '周二'
    elif timein.weekday()==3:
        strout = '周三'
    elif timein.weekday()==4:
        strout = '周四'
    elif timein.weekday()==5:
        strout = '周五'
    elif timein.weekday()==6:
        strout = '周六'
    return strout

def drawAplot(Array,ct):
    date = timeTostr(ct)
    Array = Array[:,:46]
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size'  : 100 }
    figsize = 50,30
    fig,ax  = plt.subplots(figsize=figsize)
    ax.plot(Array[0,:] ,color = 'grey' ,linewidth=8,label='NWP',linestyle='--',marker='.',markersize=40)
    ax.plot(Array[1,:] ,color = 'black'  ,linewidth=6,label='SLR',marker='.',markersize=40)
    ax.plot(Array[2,:] ,color = 'blue',linewidth=6,label='MLR',marker='.',markersize=40)
    ax.plot(Array[3,:] ,color = 'red'   ,linewidth=6,label='ANN',marker='.',markersize=40)
    ax.set_title('54401'+date+' 08(UTC+8) begin forecast',fontsize=140)
    ax.set_xlabel('forecast days (UTC+8)',fontsize=100)
    ax.set_ylabel('temperature',fontsize=100)
    
    # ax.set_xlim([-2,42])
    timeseries = ['                       '+date                           +'\n                      '+toweekday(ct+timedelta(days=1)),
                  '                       '+timeTostr(ct+timedelta(days=1))+'\n                      '+toweekday(ct+timedelta(days=2)),
                  '                       '+timeTostr(ct+timedelta(days=2))+'\n                      '+toweekday(ct+timedelta(days=3)),
                  '                       '+timeTostr(ct+timedelta(days=3))+'\n                      '+toweekday(ct+timedelta(days=4)),
                  '                       '+timeTostr(ct+timedelta(days=4))+'\n                      '+toweekday(ct+timedelta(days=5)),
                  '                       '+timeTostr(ct+timedelta(days=5))+'\n                      '+toweekday(ct+timedelta(days=6)),
                  ]
    siteseries = np.array([-3,5,13,21,29,37,45])
    siteseries = siteseries - 0.67#让所有位置向左移动一点，距离相当于2h
    plt.xticks(siteseries,timeseries,fontproperties=my_font)
    plt.tick_params(labelsize=60)
    
    ax.grid(linewidth=2)
    ax.spines['bottom'].set_linewidth(8)   #加粗边框
    ax.spines['right' ].set_linewidth(8)   #加粗边框
    ax.spines['top'   ].set_linewidth(8)   #加粗边框
    ax.spines['left'  ].set_linewidth(8)   #加粗边框
    ax.legend(loc='upper right',fontsize=70)
    fig.savefig(date+'_begin_forecast54401.png')

    
def timeTostr(time):
    year         = str(time.year).zfill(4)
    month        = str(time.month).zfill(2)
    day          = str(time.day).zfill(2)
    string       = year+month+day  
    return string
    
if __name__ == '__main__':
    
    current_time = datetime.datetime.now()
    citysite     = '54401'
    today = timeTostr(current_time)
    
    ANN = np.load(citysite+'_'+today+'ANNpredict.npy')
    SLR = np.load(citysite+'_'+today+'SLRpredict.npy')
    MLR = np.load(citysite+'_'+today+'MLRpredict.npy')
    NWP = np.load(citysite+'_'+today+'NWPpredict.npy')
    
    Array = np.zeros([4,60])
    Array[0,:] = NWP[0,:] - 273.15
    Array[1,:] = SLR[0,:]
    Array[2,:] = MLR[0,:]
    Array[3,:] = ANN[0,:]
    
    drawAplot(Array,current_time)
    print('done')
