import unittest

def parosSzamokOsszege(szam1, szam2):
    osszeg = 0

    for i in range(szam1, szam2+1):
        if i%2 == 0:
            osszeg += i
    
    return osszeg

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(parosSzamokOsszege(42, 100), 2130)
    def test_2(self):
        self.assertEqual(parosSzamokOsszege(0, 0), 0)
    def test_3(self):
        self.assertEqual(parosSzamokOsszege(-2, 10), 28)
    def test_4(self):
        self.assertEqual(parosSzamokOsszege(-10, 0), -30)
    def test_5(self):
        self.assertGreater(parosSzamokOsszege(32, 521), 0)
    def test_5(self):
        self.assertLess(parosSzamokOsszege(-153, 41), 0)

if __name__ == "__main__":
    unittest.main()