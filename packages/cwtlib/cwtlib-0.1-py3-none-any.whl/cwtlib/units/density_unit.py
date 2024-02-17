from cwtlib.units.unit import Unit

class DensityUnit(Unit):
    units = dict(
        kg_m3 = dict(a=1, b=0),
        g_cm3 = dict(a=1, b=0),
        g_ml = dict(a=1, b=0),
        g_l = dict(a=1e3, b=0),
        mg_ml = dict(a=1, b=0),
        pounds_gallon = dict(a=119.826, b=0),
    )
    def __init__(self, value, unit='kg_m3'):
        super().__init__(value, unit)