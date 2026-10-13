import math
import unittest

def negyzetgyok(szam):
    if szam < 0:
        return f"Negativ szambol nem vonunk negyzetgyokot!"
    return math.sqrt(szam)

class Test(unittest.TestCase):

    def test_pos(self):
        self.assertGreater(negyzetgyok(26), 0)
    def test_neg(self):
        self.assertEqual(negyzetgyok(-1), "Negativ szambol nem vonunk negyzetgyokot!")

if __name__ == "__main__":
    unittest.main()