import functions
import unittest

class check_armstromg_number(unittest.TestCase):
    def setUp(self):
        self.num1=153
        self.num2=154

    def tearDown(self):
        self.num1=0
        self.num2=0

    def test_armstrong(self):
        result=functions.armstrong_number(self.num1)
        self.assertEqual("Armstrong number",result)

    def test_not_armstrong(self):
        result=functions.armstrong_number(self.num2)
        self.assertEqual("not an Armstrong number",result)

class check_disible_or_not(unittest.TestCase):
    def setUp(self):
        self.num1 = 15
        self.num2 = 11

    def tearDown(self):
        self.num1 = 0
        self.num2 = 0

    def test_divisible(self):
        result=functions.divisible(self.num1)
        self.assertTrue(result)

    def test_not_divisible(self):
        result=functions.divisible(self.num2)
        self.assertTrue(result)

class check_largest_of_3num(unittest.TestCase):
    def setUp(self):
        self.x = 19
        self.y = 15
        self.z = 10

    def tearDown(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def test_largest_num(self):
        result=functions.Largest_of_3num(self.x,self.y,self.z)
        self.assertEqual(self.x,result)


class check_even_odd(unittest.TestCase):
    def setUp(self):
        self.x1 = 14
        self.x2 = 15


    def tearDown(self):
        self.x1 = 0
        self.x2 = 0

    def test_even(self):
        result=functions.even_odd(self.x1)
        self.assertEqual("even",result)

    def test_odd(self):
        result=functions.even_odd(self.x2)
        self.assertEqual("odd",result)

if __name__=="__main__":
    unittest.main()
