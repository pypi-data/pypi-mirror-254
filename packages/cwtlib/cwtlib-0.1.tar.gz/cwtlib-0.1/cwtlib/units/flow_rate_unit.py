from cwtlib.units.unit import Unit

class FlowRateUnit(Unit):
    units = dict(
        default = dict(a=1, b=0),
        m3_s = dict(a=1, b=0),
        m3_h = dict(a=1/3600, b=0),
        m3_d = dict(a=1/86400, b=0),
        l_s = dict(a=1e-3, b=0),
        l_h = dict(a=1/3.6, b=0),
        l_d = dict(a=1/86.4, b=0),
        ml_s = dict(a=1e-6, b=0),
        ml_h = dict(a=1/3.6e6, b=0),
        ml_d = dict(a=1/86.4e6, b=0),
        cm3_s = dict(a=1e-6, b=0),
        cm3_h = dict(a=1/3.6e6, b=0),
        cm3_d = dict(a=1/86.4e6, b=0),
        mm3_s = dict(a=1e-9, b=0),
        mm3_h = dict(a=1/3.6e9, b=0),
        mm3_d = dict(a=1/86.4e9, b=0),
        ft3_s = dict(a=0.0283168, b=0),
        ft3_h = dict(a=1.013e-5, b=0),
        ft3_d = dict(a=1.185e-7, b=0),
        in3_s = dict(a=1.6387e-5, b=0),
        in3_h = dict(a=5.899e-8, b=0),
        in3_d = dict(a=6.886e-10, b=0),
        gal_s = dict(a=4.546e-3, b=0),
        gal_h = dict(a=1.64e-5, b=0),
        gal_d = dict(a=1.91e-7, b=0),)

    def __init__(self, value, unit='default'):
        super().__init__(value, unit)