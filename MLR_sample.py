"""
A sample script for multi-linear regression
"""
#########################################
# Import Pakcages, may need to install some
#########################################
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from scipy import signal
from sklearn.linear_model import LinearRegression
from leave_one_out_MLR import lv1out_mlr
from normalization import normalize

nyr=65				#sample size
iyr1=1990;iyr2=iyr1+nyr-1
yrs=np.arange(iyr1,iyr2+1)

#testing random data
X1=np.sin(2*np.pi*(yrs-iyr1)/nyr)
X2=np.cos(3*np.pi*(yrs-iyr1)/nyr)
X3=np.sin(6*np.pi*(yrs-iyr1)/nyr)
Y=2*X1+3*X2+X3+0.5*np.random.rand(nyr)
X=np.column_stack((X1,X2,X3))
yhat=lv1out_mlr(X,Y)
corr,p = stats.pearsonr(Y,yhat)
print('Test: ',corr,p)

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(yrs,Y)
plt.plot(yrs,yhat)
plt.legend(['Y', 'Yhat'])
plt.xlabel('Year')
plt.ylabel('Y')
plt.title('Y and Yhat Time Series')

plt.subplot(1,2,2)
plt.plot(Y,yhat,'ro')
plt.xlabel('Y')
plt.ylabel('Yhat')
r,p=stats.pearsonr(Y,yhat)
plt.title('Scatterplot (r='+str(round(r,2))+')')
fmt='png'
plt.savefig('fig-MLR-sample.'+fmt,format=fmt,bbox_inches='tight')

plt.show(block=False)
