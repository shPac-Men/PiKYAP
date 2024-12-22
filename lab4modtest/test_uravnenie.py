import unittest
from lab4 import uravnenie

class TestUravnenie(unittest.TestCase):

    def test_discriminant_positive(self):
        eq = uravnenie()
        eq.get_coef(1, -3, 2)
        self.assertGreater(eq.discriminant(), 0)
        
    def test_1(self):
        eq = uravnenie()
        with self.assertRaises(ValueError):
            eq.get_coef('a','b','c')

    def test_2(self):
        eq = uravnenie()
        eq.get_coef(1,-3,2)
        self.assertEqual(eq.solve(),[1,2])

if __name__ == '__main__':
    unittest.main()
