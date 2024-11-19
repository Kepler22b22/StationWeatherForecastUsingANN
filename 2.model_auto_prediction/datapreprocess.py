import numpy   as np
import pandas  as pd
import math
#--------------------------------------------------------------------------
def get_rp5ru_obs(path):
    # Read OBS
    print('reading:obs')  
    Y       = pd.read_excel(path,index_col=0)
    Y.index = pd.to_datetime(Y.index,format='%d.%m.%Y %H:%M')
    Y.sort_index(inplace=True)
    Y.index   = Y.index - pd.Timedelta(hours=8) #北京时转换为世界时
    print('finish reading:obs')  
    return Y  
#--------------------------------------------------------------------------
def get_GFS_inputs(path,hour,inputnames):
    print('reading GFS inputs')
    X_data  = np.load(path+'save_x_'+str(hour).zfill(3)+'.npy')
    #这一段是为了让我之前设计的np数组的最后一列（表示时间的）
    #变成DataFrame格式里面的index,先从float变到int是为了去掉小数点后面的部分,
    #再变成str，再设为index，最后再把index设为时间类型的index。  
    #并且设置了列名
    #最后，因为是72小时预报场，所以index要加上72h
    #最最后，我还删除了所有的2月29日
    pd_X_data         = pd.DataFrame(X_data)
    pd_X_data.columns = inputnames
    pd_X_data         = pd_X_data.astype({'date':'int'})
    pd_X_data         = pd_X_data.astype({'date':'str'})    
    pd_X_data.set_index('date', inplace=True)
    pd_X_data.index   = pd.DatetimeIndex(pd_X_data.index)  
    pd_X_data.index   = pd_X_data.index + pd.Timedelta(hours=int(hour))
    #pd_X_data         = del_leafyear(pd_X_data)
    #add julian day
    #pd_X_data         = add_julian_day(pd_X_data,int(hour))
    
    print('finish reading GFS inputs')
    return pd_X_data
#--------------------------------------------------------------------------
def data_year_to_month(Xin,month):
    month = int(month)
    Xout = Xin[Xin.index.month == month]        
    return Xout
#--------------------------------------------------------------------------
def data_year_to_3month(Xin,mon):
    mon = int(mon)
    if mon == 1:
        a    = Xin[Xin.index.month == 12]
        b    = Xin[Xin.index.month == 1]
        c    = Xin[Xin.index.month == 2]
        Xout = pd.concat([a,b,c],axis=0)
    elif mon == 12:
        a    = Xin[Xin.index.month == 11]
        b    = Xin[Xin.index.month == 12]
        c    = Xin[Xin.index.month == 1]
        Xout = pd.concat([a,b,c],axis=0)
    else:
        a    = Xin[Xin.index.month == mon-1]
        b    = Xin[Xin.index.month == mon]
        c    = Xin[Xin.index.month == mon+1]
        Xout = pd.concat([a,b,c],axis=0)        
    return Xout
#-------------------------------- 
def del_leafyear(pd_X):
    #注意：传入的pd_X必须是pandas，且有时间序列的index
#    pd_X.loc['2008-02-29']=np.nan
#    pd_X.loc['2012-02-29']=np.nan
#    pd_X.loc['2016-02-29']=np.nan
#    pd_X.loc['2020-02-29']=np.nan
#    pd_X    = pd_X.dropna(axis=0,how='any')#pandas太不友好了，直接用drop怎么都删不了
    if np.datetime64('2008-02-29') in pd_X.index:
        pd_X = pd_X.drop(np.datetime64('2008-02-29')) 
    if np.datetime64('2012-02-29') in pd_X.index:
        pd_X = pd_X.drop(np.datetime64('2012-02-29')) 
    if np.datetime64('2016-02-29') in pd_X.index:
        pd_X = pd_X.drop(np.datetime64('2016-02-29')) 
    if np.datetime64('2020-02-29') in pd_X.index:
        pd_X = pd_X.drop(np.datetime64('2020-02-29')) 
    return pd_X    
#-------------------------------- 
    #注意：传入的pd_X必须是pandas，且有时间序列的index
def add_julian_day(pd_X,hour):
    #---not leap year---
    a = np.arange(365)
    b = abs(a-182)
    c = b-91
    e = np.zeros(365)
    for i in range(15+182):
        e[i] = c[i-14+182]
    for i in range(183-15):
        e[182+15+i] = c[i]
    e = e/91 / 2 * math.pi
    for i in range(len(e)):
        e[i] = math.sin(e[i])
    #--- leap year---        
    a2 = np.arange(-77,-92,-1)
    b2 = np.arange(-91,92,1)
    c2 = np.arange(91,-77,-1)
    d2 = np.r_[a2,b2,c2]
    e2 = np.zeros(366)   
    e2 = d2/91 / 2 * math.pi
    for i in range(len(e2)):
        e2[i] = math.sin(e2[i])  
    #----------------------------
    period  = pd.date_range('1/1/2005','31/12/2020')

    period2 = pd.Series(period,index= period)
    h = np.r_[e,e,e,e2,e,e,e,e2,e,e,e,e2,e,e,e,e2]    
    h = pd.DataFrame(h)
    h.index = period2.index
    
    #这里+了hour是为了和pd_X数据匹配，而%24是因为不能让日期和sin函数有变动
    h.index = h.index + pd.Timedelta(hours=(int(hour)%24))
    h.columns = ['julian_day']
    pd_X =  pd.merge(pd_X,h,how='inner',left_index=True,right_index=True)
    
    return pd_X
#-------------------------------- 
def add_julian_day_foroneday(Xin,date):
    
    a = np.arange(365)
    b = abs(a-182)
    c = b-91
    e = np.zeros(365)
    for i in range(15+182):
        e[i] = c[i-14+182]
    for i in range(183-15):
        e[182+15+i] = c[i]
    e = e/91 / 2 * math.pi
    for i in range(len(e)):
        e[i] = math.sin(e[i])

    period  = pd.date_range('1/1/2019','31/12/2019')
    period2 = pd.Series(period,index= period)
    h = pd.Series(e)
    h.index = period2.index
    month = int(date[0:2]) 
    day   = int(date[2:4])
    h1 = h[h.index.month==month]
    h2 = h1[h1.index.day==day]
    Xout = np.r_[Xin,h2.values]
    return Xout
#----------将转换为0-1-------------    
def Normalization1(x):
    a = (x-x.min())/(x.max()-x.min())
    a.fillna(0, inplace=True)
    return a

#----------将转换为 -1 - 1!NO!z-score-------------
def Normalization2(x):
    a = (x-x.mean(axis=0))/(x.std(axis=0)) 
    a.fillna(0, inplace=True)
    return a

def Normalization3(x):
    a = (x-x.mean(axis=0))/(x.std(axis=0)) 
    b = np.nan_to_num(a)
    return b
#------------------------------------------
def Xstandardization(Xin,month,hour,citysite):
    #month = filein[-10:-8]
    Xmean = np.load('../data/mean_std/'+citysite+'meanHistory.npy')
    Xstd  = np.load('../data/mean_std/'+citysite+'stdHistory.npy')
    mean = Xmean[int(month)-1,int(int(hour)/3-1),:]
    std  = Xstd[int(month)-1,int(int(hour)/3-1),:]    
    
    Xout = (Xin -mean) / std
    Xout[np.isinf(Xout)] = 0    #因为有除以0的时候，这种情况让结果仍为0
    Xout[np.isnan(Xout)] = 0    #因为有除以0的时候，这种情况让结果仍为0
    return Xout
#------------------------------------------
def Ystandardization(Xin,month,hour,citysite):
    numberofvar = Xin.shape[1]    
    Xmean = np.load('../data/mean_std/'+citysite+'meanHistory.npy')
    Xstd  = np.load('../data/mean_std/'+citysite+'stdHistory.npy')
    mean = Xmean[int(month)-1,int(int(hour)/3-1),:numberofvar] 
    std  = Xstd[int(month)-1,int(int(hour)/3-1),:numberofvar]    
    
    Xout = (Xin -mean) / std
    Xout[np.isinf(Xout)] = 0    #因为有除以0的时候，这种情况让结果仍为0
    Xout[np.isnan(Xout)] = 0    #因为有除以0的时候，这种情况让结果仍为0
    return Xout
#------------------------------------------
def Yantistandardization(Xin,month,hour,citysite):
    try:
        numberofvar = Xin.shape[1]    
    except:
        numberofvar = Xin.shape[0]    
        
    Xmean = np.load('../data/mean_std/'+citysite+'meanHistory.npy')
    Xstd  = np.load('../data/mean_std/'+citysite+'stdHistory.npy')
    mean = Xmean[int(month)-1,int(int(hour)/3-1),:numberofvar]
    std  = Xstd[int(month)-1,int(int(hour)/3-1),:numberofvar]    

    Xout = Xin * std + mean
    return Xout

#------------------------------------------
def Xstandardization_allyear(Xin,hour,citysite):
    Xmean = np.load('../data/mean_std_allyear/'+citysite+'mean_X_History.npy')
    Xstd  = np.load('../data/mean_std_allyear/'+citysite+'std_X_History.npy')
    mean = Xmean[int(int(hour)/3-1),:]
    std  = Xstd[int(int(hour)/3-1),:]    
    
    Xout = (Xin -mean) / std
    Xout[np.isinf(Xout)] = 0    #因为有除以0的时候，这种情况让结果仍为0
    Xout[np.isnan(Xout)] = 0    #因为有除以0的时候，这种情况让结果仍为0
    return Xout
#------------------------------------------
def Ystandardization_allyear(Xin,hour,citysite):
    try:
        numberofvar = Xin.shape[1]    
    except:
        numberofvar = Xin.shape[0]    

    Xmean = np.load('../data/mean_std_allyear/'+citysite+'mean_Y_History.npy')
    Xstd  = np.load('../data/mean_std_allyear/'+citysite+'std_Y_History.npy')
    mean = Xmean[int(int(hour)/3-1),:numberofvar] 
    std  = Xstd[int(int(hour)/3-1),:numberofvar]    
    
    Xout = (Xin -mean) / std
    Xout[np.isinf(Xout)] = 0    #因为有除以0的时候，这种情况让结果仍为0
    Xout[np.isnan(Xout)] = 0    #因为有除以0的时候，这种情况让结果仍为0
    return Xout
#------------------------------------------
def Yantistandardization_allyear(Xin,hour,citysite):
    try:
        numberofvar = Xin.shape[1]    
    except:
        numberofvar = Xin.shape[0]    
        
    Xmean = np.load('../data/mean_std_allyear/'+citysite+'mean_Y_History.npy')
    Xstd  = np.load('../data/mean_std_allyear/'+citysite+'std_Y_History.npy')
    mean = Xmean[int(int(hour)/3-1),:numberofvar]
    std  = Xstd[int(int(hour)/3-1),:numberofvar]    

    Xout = Xin * std + mean
    return Xout
#------------------------------------------
from sklearn.preprocessing import StandardScaler
def job_normalization(x):
    scaler = StandardScaler()
    scaler.fit(x)
    x = scaler.transform(x)
    return x
#------------------------------------------
def wdws_transto_uv(wd,ws):
    num = wd.size
    u = np.zeros([num])
    v = np.zeros([num])
    for i in range(num):
        if wd[i] == '从北方吹来的风':
            alpha = 0
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从东北偏北方向吹来的风':
            alpha = 22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从东北方吹来的风':
            alpha = 45
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从东北偏东方向吹来的风':
            alpha = 45+22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从东方吹来的风':
            alpha = 90
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从东南偏东方向吹来的风':
            alpha = 90+22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从东南方吹来的风':
            alpha = 135
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从东南偏南方向吹来的风':
            alpha = 135+22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从南方吹来的风':
            alpha = 180
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从西南偏南方向吹来的风':
            alpha = 180+22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从西南方吹来的风':
            alpha = 225
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从西南偏西方向吹来的风':
            alpha = 225+22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从西方吹来的风':
            alpha = 270
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从西北偏西方向吹来的风':
            alpha = 270+22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从西北方吹来的风':
            alpha = 315
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        elif wd[i] == '从西北偏北方向吹来的风':
            alpha = 315+22.5
            alpha = 270 - alpha
            alpha = alpha /180 *np.pi
            u[i]  = ws[i] * math.cos(alpha)
            v[i]  = ws[i] * math.sin(alpha)
        else:
            u[i]  = 0
            v[i]  = 0
        u = pd.Series(u)
        u.index = wd.index
        v = pd.Series(v)
        v.index = wd.index
    return u,v
#------------------------------------------

def wd_transto_wd(arrayin):
    num = arrayin.shape[0]
    arrayout = np.zeros(num)
    for i in range(num):
        if arrayin[i] == '从北方吹来的风':
            arrayout[i] = 0
        elif arrayin[i] == '从东北偏北方向吹来的风':
            arrayout[i] = 22.5
        elif arrayin[i] == '从东北方吹来的风':
            arrayout[i] = 45
        elif arrayin[i] == '从东北偏东方向吹来的风':
            arrayout[i] = 45 + 22.5
        elif arrayin[i] == '从东方吹来的风':
            arrayout[i] = 90
        elif arrayin[i] == '从东南偏东方向吹来的风':
            arrayout[i] = 90 + 22.5
        elif arrayin[i] == '从东南方吹来的风':
            arrayout[i] = 135
        elif arrayin[i] == '从东南偏南方向吹来的风':
            arrayout[i] = 135 + 22.5
        elif arrayin[i] == '从南方吹来的风':
            arrayout[i] = 180
        elif arrayin[i] == '从西南偏南方向吹来的风':
            arrayout[i] = 180 + 22.5
        elif arrayin[i] == '从西南方吹来的风':
            arrayout[i] = 225
        elif arrayin[i] == '从西南偏西方向吹来的风':
            arrayout[i] = 225 + 22.5
        elif arrayin[i] == '从西方吹来的风':
            arrayout[i] = 270
        elif arrayin[i] == '从西北偏西方向吹来的风':
            arrayout[i] = 270 + 225
        elif arrayin[i] == '从西北方吹来的风':
            arrayout[i] = 315
        elif arrayin[i] == '从西北偏北方向吹来的风':
            arrayout[i] = 315 + 22.5
        elif arrayin[i] == '无风':
            arrayout[i] = 0
        else:
            print('error wind direct')
    arrayout = pd.Series(arrayout)
    arrayout.index = arrayin.index
    arrayout.rename('wd',inplace=True)    
    return arrayout
#------------------------------------------
def uv_transto_wdws(u,v):
    num = u.size
    ws = np.zeros([num])
    wd = np.zeros([num])
    for i in range(num):
    
        ws[i] = (u[i]*u[i] + v[i]*v[i]) ** 0.5
    
        if   (u[i] > 0)  & (v[i] > 0):
            wd[i] = 270 - math.atan(v[i] / u[i]) * 180 / math.pi
        elif (u[i] < 0)  & (v[i] > 0):
            wd[i] = 90  - math.atan(v[i] / u[i]) * 180 / math.pi
        elif (u[i] < 0)  & (v[i] < 0):
            wd[i] = 90  - math.atan(v[i] / u[i]) * 180 / math.pi
        elif (u[i] > 0)  & (v[i] < 0):
            wd[i] = 270 - math.atan(v[i] / u[i]) * 180 / math.pi
        elif (u[i] == 0) & (v[i] > 0):
            wd[i] = 180
        elif (u[i] == 0) & (v[i] < 0):
            wd[i] = 0
        elif (u[i] > 0)  & (v[i] == 0):
            wd[i] = 270
        elif (u[i] < 0)  & (v[i] == 0):
            wd[i] = 90
        elif (u[i] == 0) & (v[i] == 0):
            wd[i] = 0
        wd = pd.Series(wd)
        wd.index = u.index
        wd.rename('wd',inplace=True)
        ws = pd.Series(ws)
        ws.index = u.index
        ws.rename('ws',inplace=True)

    return wd,ws
























#------------------------------------------------------
