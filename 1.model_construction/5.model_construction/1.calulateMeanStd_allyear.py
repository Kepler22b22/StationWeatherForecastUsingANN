# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:11:58 2020

@author: qyl
"""

import numpy          as np
import pandas         as pd
import datapreprocess as d
import os 
#------------------------------------------------------
if __name__ == "__main__":

    citysites = ['54511','50953','51463','52866','53463','54662','54857','55591',
                 '56187','56778','57083','57494','58362','58847','59287','59758']
    #citysites = ['54511']
    years         = ['2005','2006','2007','2008','2009',
                     '2010','2011','2012','2013','2014',
                     '2015','2016','2017','2018','2019','2020']
    years_train   = years[:-2]
    years_test    = years[-2:]
    
    inputnamesLong    = ['t2m',  'p_sfc', 'rh2m', 'u10m','v10m',
                     'tcc_ave'      , 'prep_sfc_ave',
                     'dswave_ave'   , 'dlwave_ave'  ,
                     'uswave_ave'   , 'ulwave_ave'  ,'date']
    inputnamesShort   = ['t2m',  'p_sfc', 'rh2m', 'u10m','v10m',
                         'tcc_ave'      , 'prep_sfc_ave',
                         'dswave_ave'   , 'dlwave_ave'  ,
                         'uswave_ave'   , 'ulwave_ave'  ]
    outputnames   = ['T','P','rh','u','v']
    
    for citysite in citysites:
        GFSpath       = '../data/input_npys/'+citysite+'npy/'+citysite
        OBSpath       = '../data/OBS/'+citysite+'obs_rp5ru.xlsx'
        mean_std_savepath = '../data/'+'mean_std/'+citysite+'/'

#--------load 54511 data , named Y--------------
        Y    = d.get_rp5ru_obs(OBSpath)
    
        meantotal_X = np.zeros([60,len(inputnamesShort)])#60代表有60个预报时效，3-180
        stdtotal_X  = np.zeros([60,len(inputnamesShort)])    
        meantotal_Y = np.zeros([60,len(outputnames)])#60代表有60个预报时效，3-180
        stdtotal_Y  = np.zeros([60,len(outputnames)])    
    
        hours   = np.arange(3,181,3)
        for hour in hours:   
            hour    = str(hour).zfill(3)
#------------------------------------------------------
#--------load GFS data , named X_data--------------
            X    = d.get_GFS_inputs(GFSpath,hour,inputnamesLong)
#------------------------------------------------------
#--------data preprocess-------------------------------
#创建XY矩阵，使得日期对应上，将缺失资料的日期对应。
#最后，再加上Y_nwp，是GFS直接预报的T，也就是t2m
    
            XYlab    = pd.merge(X,Y,left_index=True,right_index=True, how='inner')
            XYlab    = XYlab[~XYlab['t2m'].isin([0])]#通过~取反，选取t2m中不包含数字0的行,是0就绝对零度了        
            XYlab    = XYlab.dropna(axis=0,how='any')#删除任何含有nan的行
    
            X_train  = XYlab[years_train[0]:years_train[-1]][inputnamesShort]
            #X_test   = XYlab[years_test[0] :years_test[-1]].drop(['T'],axis=1)
            Y_train  = XYlab[years_train[0]:years_train[-1]][outputnames]
            Y_train['P']  = Y_train['P'] * 133.322
            #Y_test   = XYlab[years_test[0] :years_test[-1]]['T']
      
#------------------------------------------------------

            Xave      = X_train.mean(axis=0)
            Xstd      = X_train.std(axis=0)                       
            meantotal_X[int(int(hour)/3)-1,:] = Xave.values
            stdtotal_X[int(int(hour)/3)-1,:]  = Xstd.values
            
            Yave      = Y_train.mean(axis=0)
            Ystd      = Y_train.std(axis=0)                       
            meantotal_Y[int(int(hour)/3)-1,:] = Yave.values
            stdtotal_Y[int(int(hour)/3)-1,:]  = Ystd.values

        if not os.path.exists('../data/mean_std_allyear'):
            os.mkdir('../data/mean_std_allyear')        
        np.save('../data/mean_std_allyear/'+citysite+'mean_X_History.npy',meantotal_X)
        np.save('../data/mean_std_allyear/'+citysite+'std_X_History.npy', stdtotal_X)
        np.save('../data/mean_std_allyear/'+citysite+'mean_Y_History.npy',meantotal_Y)
        np.save('../data/mean_std_allyear/'+citysite+'std_Y_History.npy', stdtotal_Y)
        #其中，第一维预报时效，第二维是变量
