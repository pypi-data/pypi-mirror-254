from cwtlib.units.unit import Unit
import numpy as np
class TDSUnit(Unit):
    units = dict(
        usm = dict(a=1, b=0),
        ppm_measured = dict(a=0.5, b=0),
    )
    @property
    def ppm(self):
        if self.usm > 7630:
            return 0.0000000000801 * np.exp((-50.6458-np.log(self.usm))**2 / 112.484)
        else:
            return 7.7E-20 * np.exp((-90.4756-np.log(self.usm))**2 / 188.884)
    @ppm.setter
    def ppm(self, ppm):
        if ppm > 4089.5:
            self.usm = np.exp(-50.6458 + (112.484*np.log(ppm/0.0000000000801))**0.5)
        else:
            self.usm = np.exp(-90.4756 + (188.84*np.log(ppm/7.7E-20))**0.5)
