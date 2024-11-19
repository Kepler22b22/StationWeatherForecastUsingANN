#import numpy   as np
#import pandas as pd
import numpy   as np
import statsmodels.api as sm           # LINEAR REGRESSION
from math import sqrt
from keras.models               import Sequential ,load_model   # ANN
from keras.layers               import Dense ,Input     
from keras.layers.convolutional import Conv1D         # CNN
from keras.layers.pooling       import MaxPooling1D,AveragePooling1D
from keras.layers               import Dropout,BatchNormalization,Embedding
from keras.layers.core          import Flatten
from keras.layers               import LSTM
from keras.callbacks            import ModelCheckpoint
import gc
from tensorflow.keras import layers
#from keras.utils.training_utils import multi_gpu_model

#------------------------------------------------------
#---神经元数量---
#def run_ann(n,ts,X_trainANN,X_testANN,Y_train,Y_test): 
#    score = 10
#    for i in range(10):
#        print('------------------')
#        print('ANN calculating: '+str(ts*24)+' hour_'+str(i))
#        print('------------------')
#        MyModel = model_ann(n_neuron=n,input_dim=10)
#        MyModel.fit(X_trainANN,Y_train,epoc=200,bsize=250,verb=0)
#        MyModel = load_model('tmp_ANN.h5')
##        Y_pred_ANN = MyModel.predict(X_testANN,batch_size=250) 
#        score_tmp = MyModel.evaluate(X_testANN,Y_test,verbose=0)[0]
#        if score_tmp < score:
#            score = score_tmp
#            MyModel.save(str(ts*24)+'hour_ANN_model.h5')
#    print('ANN calculate finished')
#    return score    
#------------------------------------------------------
#---drop out---
#def run_ann(n,ts,X_trainANN,X_testANN,Y_train,Y_test): 
#    score = 10
#    for i in range(10):
#        print('------------------')
#        print('ANN calculating: '+str(ts*24)+' hour_'+str(i))
#        print('------------------')
#        MyModel = model_ann(n_neuron=32,input_dim=10,dropout=n)
#        MyModel.fit(X_trainANN,Y_train,epoc=200,bsize=250,verb=0)
#        MyModel = load_model('tmp_ANN.h5')
##        Y_pred_ANN = MyModel.predict(X_testANN,batch_size=250) 
#        score_tmp = MyModel.evaluate(X_testANN,Y_test,verbose=0)[0]
#        if score_tmp < score:
#            score = score_tmp
#            MyModel.save(str(ts*24)+'hour_ANN_model.h5')
#    print('ANN calculate finished')
#    return score
#------------------------------------------------------
#---activate function---
#def run_ann(n,ts,X_trainANN,X_testANN,Y_train,Y_test): 
#    score = 10
#    for i in range(30):
#        print('------------------')
#        print('ANN calculating: '+str(ts*24)+' hour_'+str(i))
#        print('------------------')
#        MyModel = model_ann(n_neuron=32,input_dim=10,dropout=0.3,acti = n)
#        MyModel.fit(X_trainANN,Y_train,epoc=200,bsize=250,verb=1)
#        MyModel = load_model('tmp_ANN.h5')
##        Y_pred_ANN = MyModel.predict(X_testANN,batch_size=250) 
#        score_tmp = MyModel.evaluate(X_testANN,Y_test,verbose=0)[0]
#        if score_tmp < score:
#            score = score_tmp
#            MyModel.save(str(ts*24)+'hour_ANN_model.h5')
#    print('ANN calculate finished')
#    return score
#------------------------------------------------------
#---use_bias---
#def run_ann(n,ts,X_trainANN,X_testANN,Y_train,Y_test): 
#    score = 10
#    for i in range(30):
#        print('------------------')
#        print('ANN calculating: '+str(ts*24)+' hour_'+str(i))
#        print('------------------')
#        MyModel = model_ann(n_neuron=32,input_dim=10,use_bias=n)
#        MyModel.fit(X_trainANN,Y_train,epoc=200,bsize=250,verb=1)
#        MyModel = load_model('tmp_ANN.h5')
##        Y_pred_ANN = MyModel.predict(X_testANN,batch_size=250) 
#        score_tmp = MyModel.evaluate(X_testANN,Y_test,verbose=0)[0]
#        if score_tmp < score:
#            score = score_tmp
#            MyModel.save(str(ts*24)+'hour_ANN_model.h5')
#    print('ANN calculate finished')
#    return score
#------------------------------------------------------
#---opt---
#def run_ann(n,ts,X_trainANN,X_testANN,Y_train,Y_test): 
#    score = 10
#    for i in range(30):
#        print('------------------')
#        print('ANN calculating: '+str(ts*24)+' hour_'+str(i))
#        print('------------------')
#        MyModel = model_ann(n_neuron=32,input_dim=10,opti=n)
#        MyModel.fit(X_trainANN,Y_train,epoc=200,bsize=250,verb=1)
#        MyModel = load_model('tmp_ANN.h5')
##        Y_pred_ANN = MyModel.predict(X_testANN,batch_size=250) 
#        score_tmp = MyModel.evaluate(X_testANN,Y_test,verbose=0)[0]
#        if score_tmp < score:
#            score = score_tmp
#            MyModel.save(str(ts*24)+'hour_ANN_model.h5')
#    print('ANN calculate finished')
#    return score
#------------------------------------------------------
#---kernel_initializer---
'''
def run_ANN_and_save(hour,month,X_train,X_test,Y_train,Y_test,ANNruntimes,n_neuron,
                     epoc=200,bsize=250,verb=0): 
    ANNruntimes = int(ANNruntimes)
    hour     = str(hour).zfill(3)
    month    = str(month).zfill(2)
    score    = 5000
    print('----------------------------------------------')
    print(month+'_month_'+hour+'_hour ANN calculate begin')
    for i in range(ANNruntimes):        
        MyModel = model_ann(n_neuron=n_neuron,input_dim=X_train.shape[1])
        MyModel.fit(X_train,Y_train,epoc=epoc,bsize=bsize,verb=verb)
        MyModel = load_model('tmp_ANN.h5')
        score_tmp = MyModel.evaluate(X_test,Y_test,verbose=0)[0]
        if i%2==0:
            print('ANN calculating: '+str(i+1)+'times')            
        if score_tmp < score:
            score = score_tmp
            MyModel.save(hour+'hour_'+month+'_month_ANN_model.h5')
        del MyModel
        gc.collect()
    print(month+' month '+hour+' hour ANN calculate finished')
    #return score
    return 0
'''
#------------------------------------------------------
    
    
class model_ann:

    def __init__(self,  n_neuron=64,          
                        input_dim=20,
                        kernel_ini="RandomUniform",
                        use_bias=True,
                        dropout=0.3,
                        acti='tanh',
                        loss='mean_squared_error',
                        opti='Adadelta',
                        #opti='SGD',
                        metr=['accuracy'], ):        
        
        self.model = Sequential()
        self.model.add(Dense(n_neuron, 
                             input_dim=input_dim, 
                             activation=acti,
                             use_bias=use_bias,
                             kernel_initializer=kernel_ini,))
        self.model.add(BatchNormalization())
        self.model.add(Dropout(dropout))

        self.model.add(Dense(1))
        self.model.compile(loss=loss, optimizer=opti, metrics=metr)   
        
    def save(self,path):
        self.model.save(path)
        
    def fit(self, X, Y, epoc=200,
                        bsize=250,
                        verb=0, ):
        #X = X.featurewise_std_normalization
        filepath = 'tmp_ANN.h5'
        Model_Checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=verb,
                                           save_best_only=True, mode='min', period=1)
        #self.model.fit(X, Y, batch_size=bsize, epochs=epoc,verbose=verb, 
        #               callbacks=[Model_Checkpoint],validation_split=0.2)
        self.model.fit(X, Y, batch_size=bsize, epochs=epoc,verbose=verb)
    
    def predict(self, X, bsize=250,
                         verb=0, ):        
        return self.model.predict(X, batch_size=bsize, verbose=verb)

#    def evaluate(self,X,Y,verb=0,):
#        return self.model.evaluate(X,Y,batch_size=None, verbose=verb)
#------------------------------------------------------
    
    
class model_multiclass_ann:

    def __init__(self,  n_neuron=(64),          
                        input_dim=20,
                        kernel_ini="RandomUniform",
                        use_bias=True,
                        dropout=0.3,
                        acti='tanh',
                        loss='mean_squared_error',
                        opti='Adadelta',
                        metr=['accuracy'], ):        
        
        self.model = Sequential()
        self.model.add(Dense(n_neuron, 
                             input_dim=input_dim, 
                             activation=acti,
                             use_bias=use_bias,
                             kernel_initializer=kernel_ini,))
        self.model.add(BatchNormalization())
        self.model.add(Dropout(dropout))

        self.model.add(Dense(1))
        self.model.compile(loss=loss, optimizer=opti, metrics=metr)        
    
    def fit(self, X, Y, epoc=200,
                        bsize=256,
                        verb=0, ):
        #X = X.featurewise_std_normalization
        filepath = 'tmp_ANNtest.h5'
        Model_Checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=verb,
                                           save_best_only=True, mode='min', period=1)
        self.model.fit(X, Y, batch_size=bsize, epochs=epoc,verbose=verb, callbacks=[Model_Checkpoint],validation_split=0.2)
    
    def predict(self, X, bsize=256,
                         verb=0, ):        
        return self.model.predict(X, batch_size=bsize, verbose=verb)    
#------------------------------------------------------
class model_CNN1:
    model = ''
    def __init__(self,  kinit='uniform',
                        loss='mean_squared_error',
                        opti='adam',
                        metr=['accuracy'],
                        input_shape=(1,9) ):
        
        self.model = Sequential()
        self.model.add(Conv1D(64, 
                              kernel_size = 2 , 
                              padding     = 'same',
                              data_format = 'channels_last', 
                              input_shape = input_shape ,
                              activation  = 'relu', 
                              kernel_initializer=kinit))                              
        self.model.add(BatchNormalization())        
        self.model.add(MaxPooling1D(pool_size=2, padding = 'same',))  
        self.model.add(Dropout(0.2))
 
#        self.model.add(Conv1D(64, 
#                              kernel_size = 2 , 
#                              padding     = 'valid' ,
#                              data_format = 'channels_last',
#                              activation  = 'relu'))                              
#        self.model.add(BatchNormalization())        
#        self.model.add(MaxPooling1D(pool_size=2, padding = 'valid',))  
#        self.model.add(Dropout(0.2))


        self.model.add(Flatten())
        self.model.add(Dense(32, activation ='relu'))
        self.model.add(Dropout(0.3))
#        self.model.add(Dense(64,  activation ='relu'))
#        self.model.add(BatchNormalization())
        self.model.add(Dense(1,   activation =None))
        self.model.compile(loss=loss,optimizer=opti,metrics=metr)   

    def fit(self,X,Y,bsize=250,epoc=80,verb=1,):
#        early_stopping = EarlyStopping(monitor='val_loss', patience=20, verbose=1, mode='min')
        filepath = 'tmp_CNN.h5'
        Model_Checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=1,
                                           save_best_only=True, mode='min', period=1)
        self.model.fit(X, Y, batch_size=bsize, epochs=epoc,verbose=verb, callbacks=[Model_Checkpoint],validation_split=0.2)
       
    def evaluate(self,X,Y):
        return self.model.evaluate(X,Y,batch_size=None, verbose=1,)

    def predict(self,X,bsize=1000,verb=1,):
        return self.model.predict(X, batch_size=bsize, verbose=verb)
    
    def save(self,path):
        self.model.save(path)
#--------------------------------------------------------------------------        
def run_lstm(n,ts,X_trainLSTM,X_testLSTM,Y_train,Y_test): 
    score = 10
    for i in range(30):
        print('------------------')
        print('LSTM calculating: '+str(ts*24)+' hour_'+str(i))
        print('------------------')
        MyModel = model_lstm(kernel_ini=n)
        MyModel.fit(X_trainLSTM,Y_train,epoc=200,bsize=250,verb=0)
        MyModel = load_model('tmp_LSTM.h5')
        score_tmp = MyModel.evaluate(X_testLSTM,Y_test,verbose=0)[0]
        if score_tmp < score:
            score = score_tmp
            MyModel.save(str(ts*24)+'hour_LSTM_model.h5')
    print('LSTM calculate finished')
    return score
#--------------------------------------------------------------------------
class model_lstm:
    model = ''
    def __init__(self,  n_neuron=512,          # number of INPUT 
                        input_d=10,
                        input_l=1,
                        kernel_ini="RandomUniform",
                        dropout=0,
                        recurrent_dropout=0.4,
                        acti='relu',
                        recurrent_activation='hard_sigmoid',
                        loss='mean_squared_error',
                        opti='Adadelta',
                        metr=['accuracy'], ):
        
        self.model = Sequential()
        self.model.add(LSTM(n_neuron,input_length = input_l,input_dim = input_d,\
                            activation=acti,\
                            recurrent_activation=recurrent_activation, use_bias=True,\
                            dropout=dropout, recurrent_dropout=recurrent_dropout,))
        self.model.add(BatchNormalization())
#        self.model.add(Dropout(0.1))
        
        self.model.add(Dense(32, activation='tanh'))
        self.model.add(BatchNormalization())
        self.model.add(Dropout(0.3))
        self.model.add(Dense(1))
        self.model.compile(loss=loss,optimizer=opti,metrics=metr)

    def fit(self,X,Y,bsize=1000,epoc=1000,verb=1,):
#        early_stopping = EarlyStopping(monitor='val_loss', patience=20, verbose=1, mode='min')
        filepath = 'tmp_LSTM.h5'
        Model_Checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=0,
                                           save_best_only=True, mode='min', period=1)
        self.model.fit(X, Y, batch_size=bsize, epochs=epoc,verbose=verb, callbacks=[Model_Checkpoint],validation_split=0.1)
       
    def predict(self,X,bsize=1000,verb=0,):
        return self.model.predict(X, batch_size=bsize, verbose=verb)
    
    def save(self,path):
        self.model.save(path)
#--------------------------------------------------------------------------
'''
class model_mlr:

    Model with Multi-variable Linear Regression

    def __init__(self):
        pass
    
    def fit(self, X, Y):
 
        X : multi-row(samples) multi-column(x1,x2,...,xn) matrix
        Y : multi-row(samples)     1-column(y           ) vector

        X              = sm.add_constant(X)
        self.beta      = sm.OLS(Y,X).fit()
        
    def predict(self, X):
        X              = sm.add_constant(X)
        return self.beta.predict(X)
'''
class Model_mlr:
    def __init__(self,X,Y):
        #has_constant='add'的意思是，就算数组中已经有一列是常数了，也仍然在前一行加常数1
        X    = sm.add_constant(X,has_constant='add')
        self.est  = sm.OLS(Y,X).fit()
        
    def summary(self):
        return self.est.summary()
    def params(self):
        return self.est.params
    def predict(self,Xtest):
        Xtest        = sm.add_constant(Xtest,has_constant='add')
        self.predict = self.est.predict(Xtest)
        return self.predict
    
#--------------------------------------------------------------------------    
def rmse(y_true, y_pred):
    y_true = np.array(y_true).reshape(-1,1)
    y_pred = np.array(y_pred).reshape(-1,1)
    error = []
    for i in range(len(y_true)):
        error.append(y_true[i] - y_pred[i])
    squaredError = []
#    absError = []
    for val in error:
        squaredError.append(val * val)#target-prediction之差平方 
        #absError.append(abs(val))#误差绝对值
        
#    print("MSE = ", sum(squaredError) / len(squaredError))#均方误差MSE
#    print("RMSE = ", sqrt(sum(squaredError) / len(squaredError)))#均方根误差RMSE
#    print("MAE = ", sum(absError) / len(absError))#平均绝对误差MAE
    result = sqrt(sum(squaredError) / len(squaredError))
    result = round(result,3)#结果保留3位小数
    return result





















#------------------------------------------------------
