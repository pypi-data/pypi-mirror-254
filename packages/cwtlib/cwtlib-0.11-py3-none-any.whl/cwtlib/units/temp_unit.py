from cwtlib.units.unit import Unit
class TempUnit(Unit):
    units = dict(
        default = dict(a=1, b=0),
        k = dict(a=1, b=0),
        c = dict(a=1, b=-273.15),
        f = dict(a=1.8, b=-459.67),
    )
