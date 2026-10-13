import unittest

def pontszam_ell(pontszam):
    if pontszam < 0:
        return("Ervenytelen ertek!")
    elif pontszam > 100:
        return("Ervenytelen ertek!")
    elif pontszam >= 85:
        return("Az érdemjegyed: 5")
    elif pontszam >= 70:
        return("Az érdemjegyed: 4")
    elif pontszam >= 55:
        return("Az érdemjegyed: 3")
    elif pontszam >= 40:
        return("Az érdemjegyed: 2")
    elif pontszam >= 0:
        return("Az érdemjegyed: 1")
    else:
        return("Ervenytelen ertek!")

class TesztFunction(unittest.TestCase):

    def test_pontszam_minusz(self):
        self.assertEqual(pontszam_ell(-1), "Ervenytelen ertek!")
    def test_pontszam_over(self):
        self.assertEqual(pontszam_ell(101), "Ervenytelen ertek!")
    def test_pontszam_5_1(self):
        self.assertEqual(pontszam_ell(100), "Az érdemjegyed: 5")
    def test_pontszam_5_2(self):
        self.assertEqual(pontszam_ell(85), "Az érdemjegyed: 5")
    def test_pontszam_4_1(self):
        self.assertEqual(pontszam_ell(84), "Az érdemjegyed: 4")
    def test_pontszam_4_2(self):
        self.assertEqual(pontszam_ell(70), "Az érdemjegyed: 4")
    def test_pontszam_3_1(self):
        self.assertEqual(pontszam_ell(69), "Az érdemjegyed: 3")
    def test_pontszam_3_2(self):
        self.assertEqual(pontszam_ell(55), "Az érdemjegyed: 3")
    def test_pontszam_2_1(self):
        self.assertEqual(pontszam_ell(54), "Az érdemjegyed: 2")
    def test_pontszam_2_2(self):
        self.assertEqual(pontszam_ell(40), "Az érdemjegyed: 2")
    def test_pontszam_1_1(self):
        self.assertEqual(pontszam_ell(39), "Az érdemjegyed: 1")
    def test_pontszam_1_2(self):
        self.assertEqual(pontszam_ell(0), "Az érdemjegyed: 1")
    

if __name__ == '__main__':
    unittest.main()