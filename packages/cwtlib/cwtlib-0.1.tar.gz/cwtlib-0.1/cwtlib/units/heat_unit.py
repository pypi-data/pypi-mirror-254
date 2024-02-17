from cwtlib.units.unit import Unit

class HeatUnit(Unit):
    units = dict(
        default = dict(a=1, b=0),
        J = dict(a=1, b=0),
        kJ = dict(a=1e3, b=0),
        MJ = dict(a=1e6, b=0),
        GJ = dict(a=1e9, b=0),
        cal = dict(a=4.184, b=0),
        kcal = dict(a=4184, b=0),
        Wh = dict(a=3600, b=0),
        kWh = dict(a=3.6e6, b=0),
        MWh = dict(a=3.6e9, b=0),
        GWh = dict(a=3.6e12, b=0),
        BTU = dict(a=1055.06, b=0),
        ft_lbf = dict(a=1.35582, b=0),
        in_lbf = dict(a=0.112985, b=0),
        hp_h = dict(a=2.68452e6, b=0),
        hp_s = dict(a=745.7, b=0),
        ton_ref = dict(a=3.51685e6, b=0),
        ton_h = dict(a=1.163e5, b=0),
        ton_s = dict(a=3.41214e8, b=0),
        toe = dict(a=4.1868e7, b=0),
        boe = dict(a=6.12e9, b=0),
        tce = dict(a=4.1868e10, b=0),
        ktoe = dict(a=4.1868e10, b=0),
        kboe = dict(a=6.12e12, b=0),
        ktce = dict(a=4.1868e11, b=0),
        Mtoe = dict(a=4.1868e13, b=0),
        Mboe = dict(a=6.12e15, b=0),
        Mtce = dict(a=4.1868e14, b=0),
        Gtoe = dict(a=4.1868e16, b=0),
        Gboe = dict(a=6.12e18, b=0),
        Gtce = dict(a=4.1868e17, b=0),)
    def __init__(self, value, unit='default'):
        super().__init__(value, unit)