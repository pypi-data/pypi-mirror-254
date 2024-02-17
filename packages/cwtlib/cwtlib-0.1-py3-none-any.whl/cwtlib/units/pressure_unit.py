from cwtlib.units.unit import Unit
class PressureUnit(Unit):
    units = dict(
        default = dict(a=1, b=0),
        pa = dict(a=1, b=0),
        kpa = dict(a=1000, b=0),
        mpa = dict(a=1000000, b=0),
        bar = dict(a=100000, b=0),
        mbar = dict(a=100, b=0),
        psi = dict(a=6894.757293168, b=0),
        ksi = dict(a=6894757.293168, b=0),
        atm = dict(a=101325, b=0),
        mmhg = dict(a=133.3223684211, b=0),
        torr = dict(a=133.3223684211, b=0),
    )

    def __init__(self, value, unit='default'):
        super().__init__(value, unit)