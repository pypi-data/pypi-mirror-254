from cwtlib.units.unit import Unit
class TimeUnit(Unit):
    units = dict(
        default = dict(a=1, b=0),
        s = dict(a=1, b=0),
        m = dict(a=1/60, b=0),
        h = dict(a=1/3600, b=0),
        d = dict(a=1/86400, b=0),
        w = dict(a=1/604800, b=0),
        y = dict(a=1/31557600, b=0),
    )
