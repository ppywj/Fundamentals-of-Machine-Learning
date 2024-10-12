import matplotlib as plt
import numpy as np


# 对函数 f=x^2进行梯度下降求极小值
# 定义函数
def f(x):
    return np.power(x, 2)


# 定义一阶导数 f=2*x
def f_1(x):
    return 2 * x


# 定义另一种一阶导数
def f_2(f, x, delta=1e-4):
    return (f(x + delta) - f(x - delta)) / 2 * delta


# 创建等差数列
xArr = np.arange(-20, 20, 1)

# 定义步长（学习率）μ:0.1
μ = 0.1
# 定义标准 flag:0.01
flag = 0.0001

# 定义 迭代次数100
maxLoop = 100

# 定义起始值 -10
startX = -10


def fit():
    global startX  # 使用全局变量 startX
    for i in range(maxLoop):
        deltaX = f_1(startX) * μ
        if abs(deltaX) <= flag:  # 使用 abs() 因为 deltaX 可能是负数
            print("deltax{index}:{delta}".format(index=i + 1, delta=abs(deltaX)))
            break  # 达到条件后退出循环
        startX = startX - deltaX
        print("deltax{index}:{delta}".format(index=i + 1, delta=deltaX))
    return startX  # 循环结束后返回 startX



res = fit()
print("res:", res)
