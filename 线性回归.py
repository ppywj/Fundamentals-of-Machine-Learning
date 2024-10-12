import numpy as np
from matplotlib import pylab as pl
#Defining training data
# 简单的线性回归模型 y=wx+b
# 自变量矩阵
x = np.array([1,3,2,1,3])
# 因变量矩阵
y = np.array([14,24,18,17,27])
# 拟合
def fit(x,y):
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    numerator=0
    denominator=0
    for i in range(len(x)):
        numerator += (x[i]-x_mean)*(y[i]-y_mean)
        denominator += np.square((x[i]-x_mean))
    b=numerator/denominator
    a=(y_mean-b)/x_mean
    return a,b
# Define prediction function
def predit(x,a,b):
    return a*x + b
# Find the regression equation
a,b = fit(x,y)
print('Line is:y = %2.0fx + %2.0f'%(a,b))
# prediction
x_test = np.array([0.5,1.5,2.5,3,4])
y_test = np.zeros((1,len(x_test)))
for i in range(len(x_test)):
    y_test[0][i] = predit(x_test[i],a,b)
# 创建一个等间隔分布的数组从0~5
xx = np.linspace(0, 5,50)
yy = a*xx + b
pl.plot(xx,yy,'k-')
# 绘制散点
pl.scatter(x,y,cmap=pl.cm.Paired)
pl.scatter(x_test,y_test[0],cmap=pl.cm.Paired)
pl.show()
