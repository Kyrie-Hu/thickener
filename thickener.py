import matplotlib.pyplot as plt
import math
import numpy


class thickener_simulation():
    def __init__(self,Qin,Cin,Uk,Y1,Y2):
        self.Qin = Qin
        self.Cin = Cin
        self.Uk = Uk
        self.Y1 = Y1
        self.Y2 = Y2




    def reset(self):
        for i in range(0,width):
            ts.computation(width)
            #print(self.Y1)
            Y_1.append(self.Y1)
            #print(self.Y2)
            Y_2.append(self.Y2)
        # print(Y_1)
        # print(Y_2)
        # print(t_0)

    def computation(self,width):

        #计算Y1用到的系数
        k0 = 0.56         #系数
        T = 6.25          #时间常数
        t = 0.0001        #采样间隔
        d = 151.0748      # potential energy difference = △p(t)/(gp(y2))-----矿浆泵两端管路单位重量矿浆的势能差
        K = 1.12          #浓密机相关常数
        C = 100000        #阻力系数

        # 计算Y2用到的系数
        ki = 0.001        #与工艺相关的常数
        A = 1962.5        #浓密机横截面积
        p = 0.01          #平均浓度系数
        k1 = 1.9625       #k1 = Aki
        k2 = 19.652       #k2 = Ap
        k3 = 0.0049       #k3 = ki-u(ps-pl)/(Ap)
        vp = 1.825        #矿浆颗粒沉降速度
        h = 6             #h(y1,y2) = 6m ---- 泥层界面高度（假设不变）
        Ps = 1520         #固体浓度,初始值为y2(t)/k0

        #计算底流料浆流量Y1(k)
        c1_1 = math.sqrt((k0*pow(self.Uk,2)-d+C)/K)   #将复杂的开方式转换为一个常数
        incre1 = (c1_1-self.Y1)/T/width     #单位步长的流量增量
        y1 = self.Y1+incre1        #单位步长后的流量
        #print(y1)


        # 计算底流料浆浓度Y2(k)
        Φ = self.Cin/(Ps*(1-self.Cin)+self.Cin)   #体积浓度Φ=Cin/(Ps(1-Cin)+Cin)
        Q = self.Qin*Φ                            #Q = Qin*Φin     进料矿浆体积
        c2_1 = 1/(k2*h)
        c2_2 = k1*vp*Q
        c2_3 = (k1*(ki-k3)*vp*Q)/(self.Y2+k3*Q)
        c2_4 = (pow(self.Y2,2)*self.Y1)/(self.Y2+k3*Q)
        incre2 = c2_1*(c2_2+c2_3-c2_4)/width   #单位步长后的浓度增量
        y2 = self.Y2 + incre2            #单位步长后的浓度

        self.Y2 = y2
        self.Y1 = y1




if __name__ == "__main__":
    #ts = thickener_simulation(620, 0.22, 660, 370, 0.325)  # 类的实例化
    ts = thickener_simulation(600, 0.25, 660, 300, 0.5)  # 类的实例化
    width = 1000
    times = 100
    t_0 = []
    for i in range(0,times):
        for j in range(0,width):
            t_0.append(i+j/width)
    print(t_0)
    Y_1 = []
    Y_2 = []
    for i in range(0,times):
        ts.reset()

    plt.plot(t_0, Y_1)
    plt.show()
    plt.plot(t_0, Y_2)
    plt.show()








