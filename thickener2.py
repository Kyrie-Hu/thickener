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
            ts.computation()
            #print(self.Y1)
            Y_1.append(self.Y1)
            #print(self.Y2)
            Y_2.append(self.Y2)
        # print(Y_1)
        # print(Y_2)
        # print(t_0)

    def computation(self):

        #计算Y1用到的系数
        k0 = 0.56         #系数
        T = 6.25          #时间常数
        #self.Uk          底流泵速

        # 计算Y2用到的系数
        k1 = 4150       #k1 = 4150kg/m3 ————浓密机内固体颗粒的平均浓度系数
        k2 = 1002       #k2 = 1002kg/m3 ————浓缩中流体粘度
        k3 = 0.0005     #k3 = 0.0005kg/m3——— 浓密机泥泥层⾼高度中的实验系数
        k4 = 0.5        #絮凝剂的作⽤用系数
        k5 = 3606       #k5 = 3606kg/m3 ———— 浓密机泥泥层⾼高度中的修正系数
        k6 = 0.005      #浓密机内的颗粒密度
        k7 = 0.03       #浓密机内的介质密度
        k8 = 1          #浓密机压缩区内介质密度的平均值
        d = 0.0008      #d = 0.0008m——————固体颗粒直径分布
        h = 6           #h(y1,y2) = 6m ---- 泥层界面高度（假设不变）
        g = 9.8         #g=9.8m/s2 -----重力加速度
        S = 1962.6      #S=1962.6m2 ---- 浓密机横截面积
        qinx = 20.5     #Qinx = 20.5m3/h --- 混合选别浓密过程的上⼀一道⼯工序磁选过程后的矿浆流量，
                        # 我们可将其设定为⼊入料料流量Qin
        Ps = 1520  # 固体浓度,初始值为y2(t)/k0


        #计算底流料浆流量Y1(k)
        c1_1 = 1-(1/T)
        c1_2 = (k0*self.Uk)/T
        y1 = c1_1*self.Y1+c1_2        #单位时间后的流量
        #print(y1)


        # 计算底流料浆浓度Y2(k)
        Φ = self.Cin/(Ps*(1-self.Cin)+self.Cin)   #体积浓度Φ=Cin/(Ps(1-Cin)+Cin)
        c2_1 = Φ*((pow(k7*qinx,2)*(k1-k2)*g)/(18*k5) + self.Y1/S)
        c2_2 = k4*h - (k3*k8*Φ*self.Qin)/(k2*S*(Φ+self.Y2))
        c2_3 = (self.Y1*self.Y2)/S + k4*k6*h*Φ
        y2 = self.Y2 + c2_1/c2_2 - c2_3/c2_2                   #单位时间后的底流料浆浓度

        self.Y2 = y2
        self.Y1 = y1




if __name__ == "__main__":
    ts = thickener_simulation(620, 0.22, 0.4, 370, 0.325)  # 类的实例化
    times = 100000
    t_0 = []
    for i in range(0,times):
            t_0.append(i)
    print(t_0)
    Y_1 = []
    Y_2 = []
    for i in range(0,times):
        ts.reset()

    plt.plot(t_0, Y_1)
    plt.show()
    plt.plot(t_0, Y_2)
    plt.show()








