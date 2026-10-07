import numpy as np
vector3 = np.ndarray
class Source:
    def __init__(self, Y: float) -> vector3:
        self.Y = Y
    def initgen(self,E:float):
        """ E - энергия """
        nphot = int(round(self.Y * E))
        phi = np.random.uniform(0.0, 2.0 * np.pi, nphot)
        cos_theta = np.random.uniform(-1.0, 1.0, nphot)
        sin_theta = np.sqrt(1.0 - cos_theta ** 2)
        return np.array([sin_theta * np.cos(phi), sin_theta * np.sin(phi),cos_theta])
    
surs=Source(10000.)
print(surs.initgen(0.0001))