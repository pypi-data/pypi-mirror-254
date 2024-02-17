from cwtlib.units.unit import Unit
class RateUnit(Unit):
    units = dict(
        default = dict(a=1, b=0),
        km_s = dict(a=1, b=0),
        m_s = dict(a=1e-3, b=0),
        cm_s = dict(a=1e-5, b=0),
        mm_s = dict(a=1e-6, b=0),
        km_h = dict(a=1/3.6, b=0),
        m_h = dict(a=1/3.6e3, b=0),
    )
    def __init__(self, value, unit='default'):
        super().__init__(value, unit)