import unittest

def szamologep(szam1, szam2, muveletiJel):
    if muveletiJel == "+":
        return szam1 + szam2
    elif muveletiJel == "-":
        return szam1 - szam2
    elif muveletiJel == "*":
        return szam1 * szam2
    elif muveletiJel == "/":
        if szam2 == 0:
            return "Ejnye, nullaval nem osztunk"
        return szam1 / szam2

    return "Rossz muveleti jel"

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(szamologep(10, 100, "*"), 1000)
    def test_2(self):
        self.assertGreater(szamologep(0.12414, 65, "*"), 0)
    def test_3(self):
        self.assertLess(szamologep(-2412, 0.214, "*"), 0)
    def test_4(self):
        self.assertGreater(szamologep(-412, -2.52, "*"), 0)
    def test_5(self):
        self.assertEqual(szamologep(5, 0, "/"), "Ejnye, nullaval nem osztunk")
    def test_6(self):
        self.assertEqual(szamologep(5, 34, "%"), "Rossz muveleti jel")
    def test_7(self):
        self.assertLess(szamologep(50, -55, "+"), 0)
    def test_8(self):
        self.assertGreater(szamologep(-30, -55, "-"), 0)
    def test_9(self):
        self.assertLess(szamologep(10, 20, "-"), 0)
    def test_10(self):
        self.assertGreater(szamologep(35, 5, "+"), 0)
    def test_11(self):
        self.assertEqual(szamologep(10, 1, "/"), 10)
    def test_12(self):
        self.assertEqual(szamologep(10, 1, "+"), 11)
    def test_13(self):
        self.assertEqual(szamologep(10, 1, "-"), 9)

if __name__ == "__main__":
    unittest.main()