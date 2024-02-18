from copy import deepcopy
class Unit:
    units = dict(
        default = dict(a=1, b=0),
    )
    _value = 0
    def __setattr__(self, key, value):
        if key in self.units:
            self._value = (value - self.units[key]['b'])/self.units[key]['a']
        else:
            super().__setattr__(key, value)
    def __getattr__(self, key):
        if key in self.units:
            return self._value*self.units[key]['a'] + self.units[key]['b']
        else:
            return super().__getattr__(key)
    def __init__(self, value, unit='default'):
        self.__setattr__(unit, value)

    def __str__(self):
        return f"{self.__class__} {self._value}"
    def __int__(self):
        return int(self._value)
    def __float__(self):
        return float(self._value)
    def __add__(self, other):
        u = deepcopy(self)
        u._value = self._value + float(other)
        return u
    def __sub__(self, other):
        u = deepcopy(self)
        u._value = self._value - float(other)
        return u
    def __mul__(self, other):
        u = deepcopy(self)
        u._value = self._value * float(other)
        return u
    def __truediv__(self, other):
        u = deepcopy(self)
        u._value = self._value / float(other)
        return u