import unittest
if __name__ == '__main__':
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cwtlib.measure_units.param import Param
from cwtlib.measure_units.temp import TempP
from cwtlib.measure_units.humidity import HumidityP
from cwtlib.measure_units.pressure import PressureP
from cwtlib.measure_units.conc import *
from cwtlib.measure_units.volumes import *
from tower import Tower, Air
from water import Water

class TestVolume(unittest.TestCase):
    def test_time(self):
        time = TimeP("h").set_value(1)
        self.assertEqual(time.s, 3600)
        self.assertEqual(time.m, 60)
        self.assertEqual(time.h, 1)
        self.assertEqual(time.d, 1/24)
    def test_volume(self):
        vol = VolumeP("l").set_value(1000)
        self.assertEqual(vol.m3, 1)
        self.assertEqual(vol.l, 1000)
    def test_volume_rate(self):
        vol = VolumeRate(1, "m3_h")
        self.assertEqual(vol.m3_h, 1)
        self.assertEqual(vol.l_s, 1000/3600)
class TestTempParam(unittest.TestCase):
    def setUp(self):
        self.temp = TempP()
        self.temp.C = 100

    def test_set_farenheit(self):
        self.temp.unit = "F"
        self.temp.F = 212
        self.assertEqual(self.temp.C, 100)
        self.assertEqual(self.temp.K, 373.15)

    def test_multiply_5(self):
        self.temp.C = self.temp.F * 5
        self.assertEqual(self.temp.C, 1060)

    def test_sum_diff(self):
        temp2 = TempP()
        temp2.C = 100
        temp2 = self.temp + temp2
        self.assertEqual(temp2.C, 200)

    def test_divide(self):
        self.temp.C = 100
        self.temp = self.temp / 2
        self.assertEqual(self.temp.C, 50)

class TestHumidityParam(unittest.TestCase):
    def setUp(self):
        self.hum = HumidityP()
        self.hum.proc = 50

    def test_set_ratio(self):
        self.assertEqual(self.hum.ratio, 0.5)

    def test_ratio_to_proc(self):
        self.hum.ratio = 0.5
        self.assertEqual(self.hum.proc, 50)

class TestPressureParam(unittest.TestCase):
    def setUp(self):
        self.press = PressureP()
        self.press.kpa = 101.325

    def test_pa(self):
        self.assertAlmostEqual(self.press.pa, 101325, 1)
        self.press.pa = 101325
        self.assertAlmostEqual(self.press.kpa, 101.325, 1)

    def test_kpa(self):
        self.assertAlmostEqual(self.press.kpa, 101.325, 1)

    def test_atm(self):
        self.assertAlmostEqual(self.press.atm, 1, 1)
        self.press.atm = 1
        self.assertAlmostEqual(self.press.kpa, 101.325, 1)

    def test_bar(self):
        self.assertAlmostEqual(self.press.bar, 1.01325, 1)
        self.press.bar = 1.01325
        self.assertAlmostEqual(self.press.kpa, 101.325, 1)

    def test_hg(self):
        self.assertAlmostEqual(self.press.hg, 760, 1)
        self.press.hg = 760
        self.assertAlmostEqual(self.press.kpa, 101.325, 1)

    def test_water(self):
        self.assertAlmostEqual(self.press.water, 10332.274527, 0)
        self.press.water = 10332.274527
        self.assertAlmostEqual(self.press.kpa, 101.325, 1)

    def test_psi(self):
        self.assertAlmostEqual(self.press.psi, 14.695948775513, 1)
        self.press.psi = 14.695948775513
        self.assertAlmostEqual(self.press.kpa, 101.325, 1)

    def test_heksa(self):
        self.assertAlmostEqual(self.press.heksa, 1013.25, 1)
        self.press.heksa = 1013.25
        self.assertAlmostEqual(self.press.kpa, 101.325, 1)

class TestIon(unittest.TestCase):
    def setUp(self):
        self.ion = Ion("po4")
    def test_ion(self):
        self.assertAlmostEqual(self.ion.molar_weight, 95, 0)
        self.assertAlmostEqual(self.ion.charge, -3, 0)
        self.assertAlmostEqual(self.ion.equiv_weight, 31.6666666666667, 0)

class TestConc(unittest.TestCase):
    def setUp(self):
        self.po4 = ConcP(1, "meq", "po4")
        self.ca = ConcP(2, "meq", "ca")
        self.mg = ConcP(3, "meq", "mg")

    def test_ppm(self):
        self.assertAlmostEqual(self.po4.ppm, 31.6666666666667, 0)
        self.po4.ppm = 31.6666666666667
        self.assertAlmostEqual(self.po4.meq, 1, 0)

    def test_mol(self):
        self.assertAlmostEqual(self.po4.mol, 0.001/3, 3)
        self.po4.mol = 0.001/3
        self.assertAlmostEqual(self.po4.meq, 1, 0)

    def test_mmol(self):
        self.assertAlmostEqual(self.po4.mmol, 1/3, 3)
        self.po4.mmol = 1/3
        self.assertAlmostEqual(self.po4.meq, 1, 0)

    def test_caco3(self):
        self.assertAlmostEqual(self.po4.caco3, 50, 3)
        self.po4.caco3 = 50
        self.assertAlmostEqual(self.po4.meq, 1, 0)

    def test_add_one_ions(self):
        self.po4 = self.po4*2
        self.assertEqual(self.po4.meq, 2)
        self.po4 = self.po4 - 1
        self.assertEqual(self.po4.meq, 1)

    def test_add_two_ions(self):
        self.assertRaises(Exception, lambda: self.po4 + self.ca)
        self.assertRaises(Exception, lambda: self.po4 - self.ca)
        x = self.mg + self.ca
        y = self.mg - self.ca
        self.assertEqual(x.meq, 5)
        self.assertEqual(y.meq, 1)

class TestTDS(unittest.TestCase):
    def setUp(self):
        self.tds = TDSP()
        self.tds.ppm = 1000
    def test_us(self):
        self.assertAlmostEqual(self.tds.usm, 2000, 0)
        self.tds.usm = 1000
        self.assertAlmostEqual(self.tds.ppm, 500, 0)

class TestAir(unittest.TestCase):
    def setUp(self):
        self.air = Air()

    def test_air(self):
        self.assertAlmostEqual(self.air.evaporation_snip(), 0.0016, 3)
        self.assertAlmostEqual(self.air.evaporation_kurita(), 0.0016, 3)
        self.assertAlmostEqual(self.air.wet_bulb().C, 18, 1)

class TestTower(unittest.TestCase):
    def setUp(self):
        self.tower = Tower()

    def test_evaporation(self):
        self.assertAlmostEqual(self.tower.evaporation().m3_h, 16.6, 0)

    def test_cycling(self):
        self.tower.set_cycles(2)
        self.assertAlmostEqual(self.tower.ev.m3_h, self.tower.bd.m3_h, 0)
    def test_efficiency(self):
        self.assertAlmostEqual(self.tower.efficacy(), 0.41, 1)

class TestWater(unittest.TestCase):
    def setUp(self):
        self.water = Water(ph=8.0, ca=ConcP(5, "meq", "ca"),
                           alk=ConcP(4, "meq", "alk"),
                           temp=TempP("C").set_value(30),
                           tds=TDSP("ppm").set_value(1000))

    def test_init_values(self):
        self.assertAlmostEqual(self.water.ph, 8.0, 1)
        self.assertAlmostEqual(self.water.alk.meq, 4, 0)
        self.assertAlmostEqual(self.water.ca.meq, 5, 0)
        self.assertAlmostEqual(self.water.temp.C, 30, 0)
        self.assertAlmostEqual(self.water.tds.ppm, 1000, 0)
        self.assertAlmostEqual(self.water.mg.meq, 5/3, 3)
        self.assertAlmostEqual(self.water.hrd.meq, 6.67, 1)

    def test_set_cycles(self):
        self.water.set_cycles(2)
        self.assertAlmostEqual(self.water.ph, 8.6, 1)
        self.assertAlmostEqual(self.water.alk.meq, 8, 0)
        self.assertAlmostEqual(self.water.ca.meq, 10, 0)
        self.assertAlmostEqual(self.water.temp.C, 30, 0)
        self.assertAlmostEqual(self.water.tds.ppm, 2000, 0)
        self.assertAlmostEqual(self.water.mg.meq, 10/3, 3)
        self.assertAlmostEqual(self.water.hrd.meq, 13.33, 1)

    def test_calc_lsi(self):
        self.assertAlmostEqual(self.water.lsi(), 1.02, 1)
        self.water.set_cycles(2)
        self.water.po4 = ConcP(3, "ppm", "po4")
        self.assertAlmostEqual(self.water.po4_si(), 0, 1)



if __name__ == '__main__':
    unittest.main()