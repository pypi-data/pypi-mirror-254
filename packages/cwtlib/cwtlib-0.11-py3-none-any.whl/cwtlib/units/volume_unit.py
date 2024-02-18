from cwtlib.units.unit import Unit
class VolumeUnit(Unit):
    units = dict(
        default = dict(a=1, b=0),
        m3 = dict(a=1, b=0),
        km3 = dict(a=1/1e9, b=0),
        l = dict(a=1/0.001, b=0),
        ml = dict(a=1/1e-6, b=0),
        gal = dict(a=1/0.00378541, b=0),
        qt = dict(a=1/0.000946353, b=0),
        pt = dict(a=1/0.000473176, b=0),
        cup = dict(a=1/0.000236588, b=0),
        oz = dict(a=1/2.95735e-5, b=0),
        ft3 = dict(a=1/0.0283168, b=0),
        barrel = dict(a=1/0.158987, b=0),
    )

    def __init__(self, value, unit='default'):
        super().__init__(value, unit)
