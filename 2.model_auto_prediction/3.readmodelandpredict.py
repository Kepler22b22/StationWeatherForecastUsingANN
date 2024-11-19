#!/opt/anaconda3/bin/python3

import pandas as pd
import numpy  as np
import netCDF4 as nc
import datapreprocess as d
from keras.models import load_model
import warnings
import datetime
import sys
warnings.filterwarnings("ignore")

def variable_read(filein):
    variablenames1 = ['t2m',  'p_sfc', 'rh2m',  'u10m','v10m',
                      'tcc_ave3'     , 'prep_sfc_ave3',
                      'dswave_ave3'  , 'dlwave_ave3'  ,
                      'uswave_ave3'  , 'ulwave_ave3'  ]
    variablenames2 = ['t2m',  'p_sfc', 'rh2m',  'u10m','v10m',
                      'tcc_ave6'     , 'prep_sfc_ave6',
                      'dswave_ave6'  , 'dlwave_ave6'  ,
                      'uswave_ave6'  , 'ulwave_ave6'  ]
    daynumber = int(filein[-6:-3])
    if   daynumber%6 == 3:
        nc_obj     = nc.Dataset(filein)
        variable   = []                 
        for s in variablenames1:
            variable_temp     = float(nc_obj.variables[s][:])   
            variable.append(variable_temp)
        variable = np.array(variable)
    elif daynumber%6 == 0:
        nc_obj     = nc.Dataset(filein)
        variable   = []                 
        for s in variablenames2:
            variable_temp     = float(nc_obj.variables[s][:])   
            variable.append(variable_temp)
        variable = np.array(variable)        
    else:
        print('hour error')
        return 0
                
    return variable

def standardization(Xin,filein,hour):
    month = filein[-10:-8]
    Xmean = np.load('../data/mean_std/'+citysite+'meanHistory.npy')
    Xstd  = np.load('../data/mean_std/'+citysite+'stdHistory.npy')
    mean = Xmean[int(month)-1,int(int(hour)/3-1),:-1]
    std  = Xstd[int(month)-1,int(int(hour)/3-1),:-1]    #不要最后一位了，因为我觉得加入的cos序列不用标准化
    
    Xout = (Xin -mean) / std
    Xout[np.isinf(Xout)] = 0    #因为有除以0的时候，这种情况让结果仍为0
    Xout[np.isnan(Xout)] = 0    #因为有除以0的时候，这种情况让结果仍为0
    return Xout

def ANNpredict(X_predict,today,hour,var):
    
    modelpathin  = './model/'+citysite+'allyear/'+var+'/'
    modelin      = modelpathin + citysite+'_'+var+'_'+str(hour).zfill(3)+'hour_ANN_model.h5'
    ANNmodel     = load_model(modelin)
    Y_ANNpredict = ANNmodel.predict(X_predict.reshape(1,-1),batch_size=256) 
    
    return Y_ANNpredict

def SLRpredict(X_predict,today,hour):
    modelpathin  = './model/'+citysite+'allyear/'+'SLR/'
    modelin      = modelpathin +str(hour).zfill(3)+'hour_SLR.csv'
    SLRparams    = pd.read_csv(modelin)
    Y_SLRpredict = np.zeros(5)
    Y_SLRpredict[0] = X_predict[0] * SLRparams.iloc[1,1] + SLRparams.iloc[0,1]
    Y_SLRpredict[1] = X_predict[1] * SLRparams.iloc[2,2] + SLRparams.iloc[0,2]
    Y_SLRpredict[2] = X_predict[2] * SLRparams.iloc[3,3] + SLRparams.iloc[0,3]
    Y_SLRpredict[3] = X_predict[3] * SLRparams.iloc[4,4] + SLRparams.iloc[0,4]
    Y_SLRpredict[4] = X_predict[4] * SLRparams.iloc[5,5] + SLRparams.iloc[0,5]
    return Y_SLRpredict

def MLRpredict(X_predict,today,hour):
    modelpathin  = './model/'+citysite+'allyear/'+'MLR/'
    modelin      = modelpathin +str(hour).zfill(3)+'hour_MLR.csv'
    MLRparams    = pd.read_csv(modelin)
    Y_MLRpredict = np.dot( X_predict,MLRparams.iloc[1:,1:]) + MLRparams.iloc[0,1:]
    Y_MLRpredict = Y_MLRpredict.values
    Y_MLRpredict = np.array(Y_MLRpredict,dtype=np.float)
    return Y_MLRpredict


if __name__ == '__main__':    
    
    global citysite
    citysite = '54401' 
    current_time = datetime.datetime.now()
    year         = str(current_time.year).zfill(4)
    month        = str(current_time.month).zfill(2)
    day          = str(current_time.day).zfill(2)
    today        = year+month+day

    agument = sys.argv
    hour    = str(agument[1]).zfill(3)
    
    filepathin   = './'+today+'nc/'
    filein       = filepathin + today + hour + '.nc'
    X_predict    = variable_read(filein)
    np.save(citysite+'_'+today+hour+'NWPpredict.npy',X_predict[:5])

    #标准化，使用train集的mean和std
    X_predict    = d.Xstandardization_allyear(X_predict,hour,citysite)

    #方法预报    
    Y_SLRpredict  = SLRpredict(X_predict,today,hour)
    Y_MLRpredict  = MLRpredict(X_predict,today,hour)

    X_predict     = d.add_julian_day_foroneday(X_predict,month+day)
    Y_ANNpredict_T  = ANNpredict(X_predict,today,hour,'T').reshape(1)
    Y_ANNpredict_P  = ANNpredict(X_predict,today,hour,'P').reshape(1)
    Y_ANNpredict_rh = ANNpredict(X_predict,today,hour,'rh').reshape(1)
    Y_ANNpredict_u  = ANNpredict(X_predict,today,hour,'u').reshape(1)
    Y_ANNpredict_v  = ANNpredict(X_predict,today,hour,'v').reshape(1)
    
    Y_ANNpredict = np.r_[Y_ANNpredict_T,Y_ANNpredict_P,Y_ANNpredict_rh,
                      Y_ANNpredict_u,Y_ANNpredict_v]
    #反标准化
    Y_SLRpredict = d.Yantistandardization_allyear(Y_SLRpredict,hour,citysite)
    Y_MLRpredict = d.Yantistandardization_allyear(Y_MLRpredict,hour,citysite)
    Y_ANNpredict = d.Yantistandardization_allyear(Y_ANNpredict,hour,citysite)
    #保存
    np.save(citysite+'_'+today+hour+'ANNpredict.npy',Y_ANNpredict)
    np.save(citysite+'_'+today+hour+'SLRpredict.npy',Y_SLRpredict)
    np.save(citysite+'_'+today+hour+'MLRpredict.npy',Y_MLRpredict)
    
    
