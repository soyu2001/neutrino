import numpy as np
import random
class Detector: 
    def __init__(self, R: float, N: int, r: float, a: float):
        """
        Рассмотрим сферический детектор радиусом R, заполненный
        сцинтиллирующей жидкостью.
        В сцинтилляторе свет от взаимодействия частиц излучается изотропно,
        выход фотонов для события с энергией 1 МэВ равен Y.
        Внутренняя поверхность детектора покрыта N фотоумножителями,
        улавливающими свет от взаимодействия частиц. Считаем, что у
        фотоумножителя плоский фотокатод радиусом r. Bероятность выбивания
        хотя бы одного фотоэлектрона равна a.
        Каждому фотоумножителю соответствует канал набора данных,
        сохраняющий число фотоэлектронов.

        """
        self.R = R 
        self.N = N
        self.r = r
        self.a = a
    def isEMT(self,x,y,EMTlist):
        EMT_angle=np.arcsin(self.r/self.R)
        for centre_coords in EMTlist:
            x_0,y_0=centre_coords
            print(x_0,y_0)
            distance=np.sqrt((x-x_0)**2+(y-y_0)**2) #так можно делать, тк радиус ФЭУ много меньше радиуса сферы(но можно переделать под сферическую метрику)
            print(distance)
            if(distance < EMT_angle):
                return(True)
        return(False)

''' для простоты координаты точек на поверхности детектора
и центров ФЭУ будем задавать в сферической системе координат в радианах
координаты phi, theta'''
R = 2
N = 40
r = 0.1
a = 0.5
EMTlist=[]
for i in range(N):
    pgen=2.*np.pi*random.random()
    tgen = np.arccos(2 * random.random() - 1)
    EMTlist.append((pgen, tgen)) 

det=Detector(R,N,r,a)
x = 2.*np.pi*random.random()
y = np.arccos(2 * random.random() - 1)
print(det.isEMT(x,y,EMTlist))