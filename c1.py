#折线图/散点图
'''
import matplotlib.pylab as pyl
import numpy as np
x = [1,2,3,4,5,6]
y = [3,2,1,4,5,7]
#pyl.plot(x,y,'r:h')#plot(x轴数据，y轴数据，展现形式)
#pyl.show()

#pyl.plot(x,y,'r')
#pyl.plot(x,y,'b')
#pyl.plot(x,y,'c')
'''

'''
c-cyan-青色
r-red-红色
m-magente-品红
b-blue-蓝色
y-yellow-黄色
k-black-黑色
w-white-白色
'''

#pyl.plot(x,y,'--')
#pyl.plot(x,y,':')
#pyl.show()
#线条样式
'''
-直线
--虚线
-.-  形式
: 细小虚线
'''
#pyl.plot(x,y,'s')
#pyl.plot(x,y,'h')
#pyl.plot(x,y,'D')
#pyl.show()
#点的样式
'''
s--方形
h--六角形
*--星形
x--x形
d--菱形
D--菱形
p--五角形
'''
'''
m = [3,4,5,2,7,8]
n = [7,9,0,1,2,3]
pyl.plot(x,y)
pyl.plot(m,n,'r')
pyl.title("show")  #图的名称
pyl.xlabel("ages") #横轴的名称
pyl.ylabel("temp") #纵轴的名称
pyl.xlim(0,20)     #横轴的取值
pyl.ylim(0,18)     #纵轴的取值
'''
#pyl.show()

#生成随机数
import random
#data = np.random.random_integers(1,20,10) #(最小值，最大值，个数)
#print(data)

#生成正太分布的随机数
#data2 = np.random.normal(9.0,3.0,50)#(均数，西格玛，个数)
#print(data2)


#更多随机数生成
#www.mamicode.com/info-detail-507676.html


#直方图hist
#data3 = np.random.normal(1.2,20.1,10000)

#sty = np.arange(1,22,1)
#pyl.hist(data3)
#pyl.show()
'''
pyl.subplot(3,2,3)
pyl.subplot(3,2,1)
pyl.subplot(3,2,2)
pyl.subplot(3,2,4)
pyl.subplot(3,2,5)
pyl.subplot(3,2,6)
'''

'''
pyl.subplot(2,2,1)
x1 = [1,2,3,4,5,6]
y1 = [4,5,6,7,8,9]
pyl.plot(x1,y1)
pyl.subplot(2,2,2)
x2 = [4,5,6,7,8,9]
y2 = [7,8,9,4,5,6]
pyl.plot(x2,y2)
pyl.subplot(2,1,2)
x3 = np.random.randint(1,20,20)
y3 = np.random.randint(5,40,20)
pyl.plot(x3,y3)
pyl.show()
'''

#读取博客数据并可视化分析
import pandas as pda
import numpy as np
import matplotlib.pylab as pyl
data = pda.read_csv("C:/Users/Administrator/Desktop/weather.csv")
data.describe()



