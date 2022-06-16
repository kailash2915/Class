import unittest
from prog import sum,sub,fact

class testMyFunc(unittest.TestCase):
    def test_sum(self):
        o1=sum(5,2)
        self.assertEqual(o1,7)
    def test_fact(self):
        o2=fact(5)
        self.assertEqual(o2,120)