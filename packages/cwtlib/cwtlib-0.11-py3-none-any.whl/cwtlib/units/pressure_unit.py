from cwtlib.units.unit import Unit
class PressureUnit(Unit):
    units = dict(
        default = dict(a=1, b=0),
        pa = dict(a=1, b=0),
        kpa = dict(a=1/1000, b=0),
        bar = dict(a=1/100000, b=0),
        mbar = dict(a=1/100, b=0),
        psi = dict(a=1/6894.757293168, b=0),
        atm = dict(a=1/101325, b=0),
        mmhg = dict(a=1/133.3223684211, b=0),
        torr = dict(a=1/133.3223684211, b=0),
        heksa = dict(a=1/100, b=0),
        hekta = dict(a=1/100, b=0),
    )
    def __init__(self, value, unit='default'):
        super().__init__(value, unit)
