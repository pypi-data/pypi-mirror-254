from cwtlib.units.unit import Unit
class AreaUnit(Unit):
    units = dict(
        m2 = dict(a=1, b=0),
        km2 = dict(a=1e-6, b=0),
        ha = dict(a=1e-4, b=0),
        acre = dict(a=1/4046.8564224, b=0),
        sqft = dict(a=1/0.09290304, b=0),
        sqin = dict(a=1/0.00064516, b=0),
        sqmi = dict(a=1/2589988.110336, b=0),
    )
    def __init__(self, value, unit='m2'):
        super().__init__(value, unit)
