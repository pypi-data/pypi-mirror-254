from cwtlib.units.unit import Unit
class HumidityUnit(Unit):
    units = dict(
        default = dict(a=1, b=0),
        percent = dict(a=1, b=0),
        ratio = dict(a=1/100, b=0),
    )
