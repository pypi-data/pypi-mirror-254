from cwtlib.units.unit import Unit

class FlowRateUnit(Unit):
    units = dict(
        default = dict(a=1, b=0),
        m3_s = dict(a=1, b=0),
        m3_h = dict(a = 3600, b=0),
        m3_d = dict(a=86400, b=0),
        l_s = dict(a=1000, b=0),
        l_h = dict(a=60000, b=0),
        l_d = dict(a=3600*24*1000, b=0),
        l_m = dict(a=60000, b=0),
        ml_s = dict(a=1000000, b=0),
        ml_h = dict(a=3600000000, b=0),
        ml_d = dict(a=86400000000, b=0),
        cm3_s = dict(a=1000000, b=0),
        cm3_h = dict(a=3600000000, b=0),
        cm3_d = dict(a=86400000000, b=0),
        gal_h = dict(a=951019.38848933, b=0),
        gal_d = dict(a=22820000, b=0),
        gal_m = dict(a=15850.323140625002, b=0),)

    def __init__(self, value, unit='default'):
        super().__init__(value, unit)
