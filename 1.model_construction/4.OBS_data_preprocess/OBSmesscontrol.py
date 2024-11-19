# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:42:10 2020

@author: qyl
"""

import numpy          as np
import pandas         as pd
import datapreprocess as d
import matplotlib.pyplot as plt


if  __name__ == "__main__":

    global citysite
    citysite= '54511'
    
    OBSpath       = '../data/OBS/'+citysite+'obs_rp5ru.xlsx'
    Y    = d.get_rp5ru_obs(OBSpath)
    error=pd.DataFrame([])
    for month in np.arange(1,13,1):
        #month = str(month).zfill(2)
        for hour in np.arange(3,181,3):
            #hour = str(hour).zfill(3)
            Y1 = Y[Y.index.hour==hour]
            Y1 = Y1[Y1.index.month==month]
            '''
            figsize = 50,30
            fig,ax  = plt.subplots(figsize=figsize)

            ax.plot(Y1.iloc[:,0],color = 'grey'  ,linewidth=12,)
            plt.show()
            '''
            mean = Y1.mean()
            std  = Y1.std()
            Tmax = mean[0] + std[0]*3
            Tmin = mean[0] - std[0]*3
            a = Y1[Y1.iloc[:,0]>Tmax]
            b = Y1[Y1.iloc[:,0]<Tmin]
            error = pd.concat([error,a,b])
            Tmax = mean[1] + std[1]*3
            Tmin = mean[1] - std[1]*3
            a = Y1[Y1.iloc[:,1]>Tmax]
            b = Y1[Y1.iloc[:,1]<Tmin]
            error = pd.concat([error,a,b])
            
            error = error.sort_index()
            '''
            Tmax = mean[2] + std[2]*3
            Tmin = mean[2] - std[2]*3
            a = Y1[Y1.iloc[:,2]>Tmax]
            b = Y1[Y1.iloc[:,2]<Tmin]
            error = pd.concat([error,a,b])           
            Tmax = mean[3] + std[3]*3
            Tmin = mean[3] - std[3]*3
            a = Y1[Y1.iloc[:,3]>Tmax]
            b = Y1[Y1.iloc[:,3]<Tmin]
            error = pd.concat([error,a,b])
            Tmax = mean[4] + std[4]*3
            Tmin = mean[4] - std[4]*3
            a = Y1[Y1.iloc[:,4]>Tmax]
            b = Y1[Y1.iloc[:,4]<Tmin]
            error = pd.concat([error,a,b])
            '''
    '''
    import datetime
    for hour in np.arange(78,177,24):
        hour = str(hour).zfill(3)
        resultpath = '../test_result_path/'+citysite+'allyear/'+citysite+'_'+hour+'_hour_Y_pred_'
        for var in ['NWP','SLR','ANN']:
            a = pd.read_excel(resultpath+var+'.xlsx',header=0,index_col=0)
            a.drop(datetime.datetime(2019,10,2,6,0),inplace=True)
            a.drop(datetime.datetime(2019,10,6,6,0),inplace=True)
            a.drop(datetime.datetime(2019,10,10,6,0),inplace=True)
            a.to_excel(resultpath+var+'.xlsx')
    '''
        
    
    
    
    
    
    