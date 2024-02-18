from cwtlib.units.unit import Unit

class HeatUnit(Unit):
    units = dict(
        default = dict(a=1, b=0),
        J = dict(a=1, b=0),
        kJ = dict(a=1/1e3, b=0),
        MJ = dict(a=1/1e6, b=0),
        GJ = dict(a=1/1e9, b=0),
        cal = dict(a=1/4.184, b=0),
        kcal = dict(a=1/4184, b=0),
        Wh = dict(a=1/3600, b=0),
        kWh = dict(a=1/3.6e6, b=0),
        MWh = dict(a=1/3.6e9, b=0),
        GWh = dict(a=1/3.6e12, b=0),
        BTU = dict(a=1/1055.06, b=0),)
    def __init__(self, value, unit='default'):
        super().__init__(value, unit)
