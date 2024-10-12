# 房屋价格与面积
# 序号：1     2    3    4     5     6     7
# 面积：150  200  250  300   350   400   600
# 价格：6450 7450 8450 9450 11450 15450 18450
import matplotlib.pyplot as plt
import matplotlib
from math import pow
import random

import numpy as np
import pylab as pl

x0 = [150, 200, 250, 300, 350, 400, 600]
y0 = [6450, 7450, 8450, 9450, 11450, 15450, 18450]
# 为了方便计算，将所有数据缩小 100 倍
x = [1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 6.00]
y = [64.50, 74.50, 84.50, 94.50, 114.50, 154.50, 184.50]
# 线性回归函数为 y=theta0+theta1*x
# 损失函数 J (θ)=(1/(2*m))*pow((theta0+theta1*x[i]-y[i]),2)
# 参数定义
theta0 = 0.1  # 对 theata0 赋值
theta1 = 0.1  # 对 theata1 赋值
alpha = 0.1  # 学习率
m = len(x)
count0 = 0
theta0_list = []
theta1_list = []
flag = 0.001
# 最大迭代次数
maxLoop = 10000
# 1、使用批量梯度下降BGD
for i in range(maxLoop):
    count0 += 1
    diss = 0  # 误差
    deriv0 = 0  # 对 theata0 导数
    deriv1 = 0  # 对 theata1 导数
    # 求导
    for i in range(m):
        deriv0 += (theta0 + theta1 * x[i] - y[i]) / m  # 对每一项测试数据求导再求和取平均值
        deriv1 += ((theta0 + theta1 * x[i] - y[i]) / m) * x[i]
    theta0 = theta0 - alpha * deriv0
    theta1 = theta1 - alpha * deriv1
    theta1_list.append(theta1)
    theta0_list.append(theta0*100)
    # 求损失值
    loss = 0
    for index in range(m):
        loss += np.power((theta0 + theta1 * x[index] - y[index]), 2)
    loss = loss / (2 * m)
    if loss < flag:
        break
theta0 = theta0*100#前面所有数据缩小了 100 倍，所以求出的 theta0 需要放大 100 倍，theta1 不用变

pl.plot(x0,y0,"k-")

# 绘制原始数据散点图
plt.scatter(x0, y0, color='red', label='Original Data')

# 绘制拟合后的直线
x_line = np.linspace(150, 600, 100)
y_line = theta0 + theta1 * x_line
plt.plot(x_line, y_line, color='blue', label='Fitted Line')

# 绘制每次迭代后的直线
for i in range(0, len(theta0_list), 100):  # 每 100 次迭代绘制一次
    y_iter = theta0_list[i] + theta1_list[i] * x_line
    plt.plot(x_line, y_iter, color='green', alpha=0.1)

# 设置图表标题和标签
plt.title('House Price vs Area')
plt.xlabel('Area (sq.m)')
plt.ylabel('Price (1000 CNY)')
plt.legend()

# 显示图表
plt.show()