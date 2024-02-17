import math
import requests
import os
from cwtlib.units.temp_unit import TempUnit
from cwtlib.units.flow_rate_unit import FlowRateUnit
from cwtlib.units.time_unit import TimeUnit
from cwtlib.units.pressure_unit import PressureUnit
from cwtlib.units.volume_unit import VolumeUnit
from cwtlib.units.temp_unit import TempUnit
from cwtlib.units.humidity_unit import HumidityUnit
import numpy as np

class Air:
    def __init__(self, tair=TempUnit(26, "c"),
                 hair=HumidityUnit(50, "percent"),
                 pair=PressureUnit(748, "mmhg"), api_key=None):
        self.tair, self.hair, self.pair = tair, hair, pair
        if api_key is None:
            try:
                self.api_key = os.environ["OPENWEATHERMAP_API_KEY"]
            except:
                self.api_key = None
    def load_weather_conditions(self, loc):
        if self.api_key is not None:
            weather = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={loc}&APPID={self.api_key}&units=metric").json()
            self.tair.c = weather["main"]["temp"]
            self.hair.percent = weather["main"]["humidity"]
            self.pair.heksa = weather["main"]["pressure"]*100
        else:
            raise Exception("PLEASE set openweathermap API  token as an environmental variable OpenWeatherMap")
    def evaporation_snip(self):
        self.ev_coeff = (0.0009971 + 0.00002357 * (self.tair.c) - 0.0000002143 * (self.tair.c))
        return self.ev_coeff
    def evaporation_kurita(self):
        self.ev_coeff = (0.575 + 0.011 * self.tair.c) / 580
        return self.ev_coeff
    def wet_bulb(self):
        wb = self.tair.c * np.arctan(0.151977 * (self.hair.percent + 8.313659) ** 0.5) + \
             np.arctan(self.tair.c + self.hair.percent) - np.arctan(self.hair.percent - 1.676331) + \
             0.00391838 * self.hair.percent ** 1.5 * np.arctan(0.023101 * self.hair.percent) - 4.686035
        return TempUnit(wb, "c")
class Tower:
    def __init__(self, rr=FlowRateUnit(2100, "m3_h"),
                 vol=VolumeUnit(650, "m3"),
                 thot=TempUnit(30, "c"),
                 tcold=TempUnit(25, "c"), air=Air()):
        self.air = air
        self.rr = rr
        self.vol = vol
        self.thot = thot
        self.tcold = tcold
    def evaporation(self, tip="snip"):
        if tip == "snip":
            self.ev = self.rr*self.air.evaporation_snip()*(self.thot.c - self.tcold.c)
        else:
            self.ev = self.rr*self.air.evaporation_kurita()*(self.thot.c - self.tcold.c)
        return self.ev
    def set_cycles(self, cycles):
        self.cycles = cycles
        self.evaporation()
        self.mu = self.ev*cycles/(cycles-1)
        self.bd = self.mu/cycles
        self.hti = TimeUnit(self.vol.m3/self.bd.m3_h*math.log(2), "h")

    def efficacy(self):
        wb = self.air.wet_bulb()
        self.eff = (self.thot.c - self.tcold.c)/(self.thot.c - wb.c)
        return self.eff
