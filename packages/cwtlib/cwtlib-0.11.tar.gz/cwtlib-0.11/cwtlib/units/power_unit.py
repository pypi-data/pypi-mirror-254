from cwtlib.units.unit import Unit

class PowerUnit(Unit):
    units = dict(
        default = dict(a=1, b=0),
        W = dict(a=1, b=0),
        kW = dict(a=1/1e3, b=0),
        MW = dict(a=1/1e6, b=0),
        GW = dict(a=1/1e9, b=0),
        hp = dict(a=1/745.7, b=0),
        BTU_h = dict(a=1/0.293071, b=0),
        BTU_s = dict(a=1/1055.06, b=0),
        kcal_h = dict(a=1/1.163, b=0),
        kcal_min = dict(a=1/69.78, b=0),
        kcal_s = dict(a=1/4186.8, b=0),
    )
