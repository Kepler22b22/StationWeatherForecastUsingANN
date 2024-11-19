# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:00:28 2020

@author: qyl
"""

import numpy          as np
import pandas         as pd
import datapreprocess as d
import function       as f
from keras.models import load_model
import gc,os
import sys

if  __name__ == "__main__":

    agument = sys.argv
    global hour
    hour    = str(agument[1])
    hour    = str(hour).zfill(3)
    global citysite
    citysite= str(agument[2])
    '''
    
    global hour
    hour    = 24
    hour    = str(hour).zfill(3)
    global citysite
    citysite      = '54511'
    '''        
    
    GFSpath       = '../data/input_npys/'+citysite+'npy/'+citysite
    OBSpath       = '../data/OBS/'+citysite+'obs_rp5ru.xlsx'
    modelsavepath = '../model/'+citysite+'allyear'

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
    
#--------load GFS input data , named X--------------
    X    = d.get_GFS_inputs(GFSpath,hour,inputnamesLong)
#--------load 54511 data , named Y--------------
    Y    = d.get_rp5ru_obs(OBSpath)
#--------data preprocess-------------------------------
#创建XY矩阵，使得日期对应上，将缺失资料的日期对应。
#最后，再加上Y_nwp，是GFS直接预报的T，也就是t2m    
    XYlab    = pd.merge(X,Y,left_index=True,right_index=True, how='inner')    
    XYlab    = XYlab[~XYlab['t2m'].isin([0])]#通过~取反，选取t2m中不包含数字0的行,是0就绝对零度了        
    XYlab    = XYlab.dropna(axis=0,how='any')#删除任何含有nan的行
    del X,Y
    gc.collect()
    
    X_train  = XYlab[years_train[0]:years_train[-1]][inputnamesShort]
    X_test   = XYlab[years_test[0]:years_test[-1]][inputnamesShort]
    Y_train  = XYlab[years_train[0]:years_train[-1]][outputnames]
    Y_test   = XYlab[years_test[0]:years_test[-1]][outputnames]
    Y_train['P'] = Y_train['P'] * 133.322
    #Y_train['T'] = Y_train['T'] - 273.15
    m_Y_nwp   = X_test.iloc[:,:len(outputnames)]

    del XYlab
    gc.collect()

    m_X_train = d.Xstandardization_allyear(X_train,hour,citysite)
    m_Y_train = d.Ystandardization_allyear(Y_train,hour,citysite)
    m_X_test  = d.Xstandardization_allyear(X_test,hour,citysite)
    
    #m_X_train = d.add_julian_day(m_X_train,hour)    
    #m_X_test  = d.add_julian_day(m_X_test,hour)

    m_Y_test  = Y_test
    
    if not os.path.exists('../model'):
        os.mkdir('../model')
    if not os.path.exists(modelsavepath):
        os.mkdir(modelsavepath)
    if not os.path.exists(modelsavepath+'/SLR'):
        os.mkdir(modelsavepath+'/SLR')
    if not os.path.exists(modelsavepath+'/MLR'):
        os.mkdir(modelsavepath+'/MLR')
    for var in outputnames:
        if not os.path.exists(modelsavepath+'/'+var):
            os.mkdir(modelsavepath+'/'+var)
           
    #Single-variable Linear Regression
    MyModel_1  = f.Model_mlr(m_X_train['t2m'],m_Y_train['T'])
    params_SLR1 = MyModel_1.params()
    MyModel_2  = f.Model_mlr(m_X_train['p_sfc'],m_Y_train['P'])
    params_SLR2 = MyModel_2.params()
    MyModel_3  = f.Model_mlr(m_X_train['rh2m'],m_Y_train['rh'])
    params_SLR3 = MyModel_3.params()
    MyModel_4  = f.Model_mlr(m_X_train['u10m'],m_Y_train['u'])
    params_SLR4 = MyModel_4.params()
    MyModel_5  = f.Model_mlr(m_X_train['v10m'],m_Y_train['v'])
    params_SLR5 = MyModel_5.params()
    params_SLR  = pd.concat([params_SLR1,params_SLR2,params_SLR3,params_SLR4,params_SLR5],axis=1)
    params_SLR.columns = ['T','P','rh','u','v']
    params_SLR.to_csv(modelsavepath+'/SLR/'  +  hour+'hour_SLR.csv',mode='w')
    
    m_Y_pred_SLR         = np.empty([m_Y_test.shape[0],len(outputnames)])
    m_Y_pred_SLR[:,0]    = m_X_test.iloc[:,0] * params_SLR.iloc[1,0] + params_SLR.iloc[0,0]
    m_Y_pred_SLR[:,1]    = m_X_test.iloc[:,1] * params_SLR.iloc[2,1] + params_SLR.iloc[0,1]
    m_Y_pred_SLR[:,2]    = m_X_test.iloc[:,2] * params_SLR.iloc[3,2] + params_SLR.iloc[0,2]
    m_Y_pred_SLR[:,3]    = m_X_test.iloc[:,3] * params_SLR.iloc[4,3] + params_SLR.iloc[0,3]
    m_Y_pred_SLR[:,4]    = m_X_test.iloc[:,4] * params_SLR.iloc[5,4] + params_SLR.iloc[0,4]
    m_Y_pred_SLR         = pd.DataFrame(m_Y_pred_SLR)
    m_Y_pred_SLR.index   = m_Y_test.index
    m_Y_pred_SLR.columns = m_Y_test.columns
    
    #Multi-variable Linear Regression
    MyModel2  = f.Model_mlr(m_X_train,m_Y_train) 
    params_MLR = MyModel2.params()
    params_MLR.columns = ['T','P','rh','u','v']
    params_MLR.to_csv(modelsavepath+'/MLR/'  +  hour+'hour_MLR.csv')

    m_Y_pred_MLR = np.dot(m_X_test.values , params_MLR.iloc[1:,:]) + params_MLR.iloc[0,:].values
    m_Y_pred_MLR = pd.DataFrame(m_Y_pred_MLR)
    m_Y_pred_MLR.index = m_Y_test.index
    m_Y_pred_MLR.columns = m_Y_test.columns
    
    #Artificial Neural Network    
    m_Y_pred_ANN = np.empty([m_Y_test.shape[0],len(outputnames)])
    i = 0
    for var in outputnames:
        MyModel = f.model_ann(n_neuron=64,input_dim=m_X_train.shape[1])
        MyModel.fit(m_X_train,m_Y_train[var],epoc=500,bsize=32,verb=0)
        #MyModel = load_model('tmp_ANN.h5')
        MyModel.save(modelsavepath  +'/'+var+'/' +citysite+'_'+var+'_'+hour+'hour_ANN_model.h5')
                
        m_Y_pred_ANN[:,i] = MyModel.predict(m_X_test,bsize=32).flatten() 
        i = i+1
    m_Y_pred_ANN = pd.DataFrame(m_Y_pred_ANN)
    m_Y_pred_ANN.index = m_Y_test.index
    m_Y_pred_ANN.columns = m_Y_test.columns       
    
#------------------------------------------------------

    #antistandardization
    m_Y_pred_SLR = d.Yantistandardization_allyear(m_Y_pred_SLR,hour,citysite)
    m_Y_pred_MLR = d.Yantistandardization_allyear(m_Y_pred_MLR,hour,citysite)
    m_Y_pred_ANN = d.Yantistandardization_allyear(m_Y_pred_ANN,hour,citysite)
    m_Y_pred_ANN['T'] = m_Y_pred_ANN['T'] - 273.15
    m_Y_pred_SLR['T'] = m_Y_pred_SLR['T'] - 273.15
    m_Y_pred_MLR['T'] = m_Y_pred_MLR['T'] - 273.15
    m_Y_nwp['t2m']    = m_Y_nwp['t2m']    - 273.15
    m_Y_test['P']     = m_Y_test['P'] * 133.322

    '''
    num_method = 4    #nwp,SLR,MLR,ANN
    Y_rmse = np.zeros([num_method*len(outputnames)])#method * variable ,month               
    for i in range(len(outputnames)):
        Y_rmse[num_method*i+0] = f.rmse(m_Y_test.iloc[:,i], m_Y_pred_SLR.iloc[:,i])
        Y_rmse[num_method*i+1] = f.rmse(m_Y_test.iloc[:,i], m_Y_pred_MLR.iloc[:,i])
        Y_rmse[num_method*i+2] = f.rmse(m_Y_test.iloc[:,i], m_Y_pred_ANN.iloc[:,i])
        Y_rmse[num_method*i+3] = f.rmse(m_Y_test.iloc[:,i], m_Y_nwp.iloc[:,i])
    '''
        
    test_result_path = '../test_result_path/' + citysite+'allyear'
    if not os.path.exists('../test_result_path'):
        os.mkdir('../test_result_path')
    if not os.path.exists(test_result_path):
        os.mkdir(test_result_path)
    m_Y_pred_SLR.to_excel(test_result_path+'/'+citysite+'_'+hour+'_hour_Y_pred_SLR.xlsx')
    m_Y_pred_MLR.to_excel(test_result_path+'/'+citysite+'_'+hour+'_hour_Y_pred_MLR.xlsx')
    m_Y_pred_ANN.to_excel(test_result_path+'/'+citysite+'_'+hour+'_hour_Y_pred_ANN.xlsx')
    m_Y_nwp.to_excel(test_result_path+'/'+citysite+'_'+hour+'_hour_Y_pred_NWP.xlsx')

    '''
    Y_rmse = pd.DataFrame(Y_rmse)
    Y_rmse.index = ['T_SLR','T_MLR','T_ANN','T_NWP',
                    'P_SLR','P_MLR','P_ANN','P_NWP',
                    'rh_SLR','rh_MLR','rh_ANN','rh_NWP',
                    'u_SLR','u_MLR','u_ANN','u_NWP',
                    'v_SLR','v_MLR','v_ANN','v_NWP']
    if not os.path.exists('../test_result_path/'+citysite+'allyear/rmse'):
        os.mkdir('../test_result_path/'+citysite+'allyear/rmse')
    Y_rmse.to_excel('../test_result_path/'+citysite+'allyear/rmse/'+citysite+'_'+hour+'_hour_rmse.xlsx')
    '''
    
