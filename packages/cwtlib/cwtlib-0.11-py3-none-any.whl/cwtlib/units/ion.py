from cwtlib.units.unit import Unit
from dataclasses import dataclass
import numpy as np
@dataclass
class IonData:
    name: str
    pk: str
    charge: int
    mol_mass: float
class Ion(Unit):
    units= dict(
        meq_l = dict(a=1, b=0),
        eq_l = dict(a=1e-3, b=0),
        ppm_caco3 = dict(a=50, b=0),
    )
    ions = dict(
        ca = IonData('calcium', 'ca', 2, 40.078),
        mg = IonData('magnesium', 'mg', 2, 24.305),
        na = IonData('sodium', 'na', 1, 22.989769),
        k = IonData('potassium', 'k', 1, 39.0983),
        hco3 = IonData('bicarbonate', 'hco3', -1, 61.0168),
        cl = IonData('chloride', 'cl', -1, 35.453),
        so4 = IonData('sulfate', 'so4', -2, 96.06),
        no3 = IonData('nitrate', 'no3', -1, 62.0049),
        fe = IonData('iron', 'fe', 2, 55.845),
        nh4 = IonData('ammonium', 'nh4', 1, 18.038),
        po4 = IonData('phosphate', 'po4', -3, 94.9714),
        mn = IonData('manganese', 'mn', 2, 54.938044),
        no2 = IonData('nitrite', 'no2', -1, 46.0055),
        sio2 = IonData('silica', 'sio2', -2, 60.0843),
    )
    def __init__(self, value, unit='meq_l', ion=None):
        if ion in self.ions:
            for k, v in self.ions[ion].__dict__.items():
                setattr(self, k, v)
        super().__init__(value, unit)
    @property
    def ppm(self):
        return np.abs(self._value*self.mol_mass/self.charge)
    @ppm.setter
    def ppm(self, value):
        self._value = np.abs(value*self.charge/self.mol_mass)
    @property
    def ppm_caco3(self):
        return self._value*50
    @ppm_caco3.setter
    def ppm_caco3(self, value):
        self._value = value/50
    @property
    def mol_l(self):
        return np.abs(self._value/self.charge/1000)
    @mol_l.setter
    def mol_l(self, value):
        self._value = np.abs(value*self.charge*1000)
    @property
    def mmol_l(self):
        return np.abs(self._value/self.charge)
    @mmol_l.setter
    def mmol_l(self, value):
        self._value = np.abs(value*self.charge)

