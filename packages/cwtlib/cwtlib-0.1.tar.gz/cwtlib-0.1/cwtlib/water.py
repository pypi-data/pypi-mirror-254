import numpy as np
from cwtlib.units.temp_unit import TempUnit
from cwtlib.units.ion import Ion
from cwtlib.units.tds_unit import TDSUnit
from cwtlib.units.time_unit import TimeUnit
class Water:
    def __init__(self, ph=7, *args):
        self.ph = ph
        self._cycles = 1
        for arg in args:
            if isinstance(arg, Ion):
                setattr(self, arg.pk, arg)
            if isinstance(arg, TDSUnit):
                self.tds = arg
            if isinstance(arg, TempUnit):
                self.temp = arg
    @property
    def hrd(self):
        return self.ca + self.mg
    @property
    def alk(self):
        return self.hco3
    @property
    def cycles(self):
        return self._cycles
    @cycles.setter
    def cycles(self, c):
        c_old = self._cycles
        self._cycles = c
        for k, v in self.__dict__.items():
            if isinstance(v, Ion) or isinstance(v, TDSUnit) and not k in ['alk', 'hrd']:
                self.__dict__[k] *= c/c_old
        self.ph = self.ph_predict()
    def ph_predict(self):
        ans = 4.17 + 1.7177 * np.log10(self.hco3.ppm_caco3 + 0.001)
        if ans < 4.5:
            ans = 4.5
        elif ans > 10:
            ans = 10
        return ans

    def phs(self):
        return self.pk2() - self.pks() - np.log10(self.ca.mol_l+0.001) + self.phco3() + 5 * self.pfm()
    def pk2(self):
        return 107.8871 + 0.03252849 * self.temp.k- 5151.79 /self.temp.k  - 38.92561 * np.log10(self.temp.k) + 563713.9 / self.temp.k ** 2
    def pks(self):
        return 171.9065 + 0.077993 * self.temp.k - 2839.319/self.temp.k- 71.595 * np.log10(self.temp.k)
    def pkw(self):
        return 4471/self.temp.k  + 0.01706 * self.temp.k - 6.0875
    def phco3(self):
        ans = self.hco3.mol_l + 10 ** (self.pfm() - self.ph) - 10 ** (self.ph + self.pfm() - self.pkw())
        ans /= 1 + 0.5 * 10 ** (self.ph - self.pk2())
        return -np.log10(ans)
    def pfm(self):
        return 1.82E6 * (self.e_help() * self.temp.k) ** (-1.5) * (self.ionic_strength() ** 0.5 / (1 + self.ionic_strength() ** 0.5) - 0.3 * self.ionic_strength() ** 0.5)
    def e_help(self):
        return 60954.0 / (self.temp.k + 116) - 68.937
    def ionic_strength(self):
        return 1.6E-5 * self.tds.ppm

    def ccsp(self):
        if self.phs() > self.ph_predict():
            return -1
        else:
            cycles = self.cycles
            while self.phs() < self.ph_predict() and self.cycles >0:
                self.cycles -= 0.01
            cycles_fin = self.cycles
            self.cycles = cycles
            return cycles_fin/cycles
    def lsi(self):
        return self.ph - self.phs()
    def rzn(self):
        return 2*self.phs() - self.ph
    def larsen(self):
        return 100*(self.cl.meq_l + self.so4.meq_l)/self.alk.meq_l
    def calc_tds(self):
        return sum([v.ppm_caco3 for k, v in self.__dict__.items() if isinstance(v, Ion)])
    def calc_na(self):
        return self.calc_ions()
    def larsen_modified(self, hti):
        if not isinstance(hti, TimeUnit):
            hti = TimeUnit(hti, 'h')
        return (self.cl.meq_l + self.so4.meq_l + self.calc_ions())**0.5/self.alk.meq_l*self.temp.c/25*hti.h/50/24
    def po4_si(self):
        return self.ph - (11.75 - np.log10(self.ca.ppm_caco3) - np.log10(self.po4.ppm) - 2 * np.log10(self.temp.c))/0.65
    def sio2_si(self):
        sio2_max = 21.43*self.ph - 4.3
        return self.sio2.ppm/sio2_max
    def caso4_si(self):
        return self.ca.ppm*self.so4.ppm/50000
    def phs_simple(self):
        a = (np.log10(self.tds.ppm)-1)/10
        b = -13.12*np.log10(self.temp.k) + 34.55
        c = np.log10(self.ca.ppm_caco3) - 0.4
        d = np.log10(self.alk.ppm_caco3)
        return 9.3 + a + b - c - d
    def lsi_simple(self):
        return self.ph - self.phs_simple()
    def rzn_simple(self):
        return 2*self.phs_simple() - self.ph
    def calc_ions(self):
        return self.cations - self.anions
    @property
    def cations(self):
        try:
            return sum([v.ppm_caco3 for k, v in self.__dict__.items() if (isinstance(v, Ion) and v.charge > 0)])
        except:
            return 0
    @property
    def anions(self):
        try:
            return sum([v.ppm_caco3 for k, v in self.__dict__.items() if (isinstance(v, Ion) and v.charge < 0)])
        except:
            return 0
