import unittest
from mathfunc import *


class TsetMathFunc(unittest.TestCase):
    """ Test mathfunc.py """

    """ 
  
    def setUp(self):
        print("测试之前到一些准备")
  
    def tearDown(self):
        print('测试之后到清理工作')
    这样每执行一条case均会进行准备和清理到工作
    """
    #  下面到方法执行每一条case时只是开始执行第一条case之前进行准备工作，执行完所有case进行清理工作。
    @classmethod  
    def setUpClass(l):
        print("测试之前到一些准备")
    @classmethod
    def tearDownClass(l):
        print('测试之后到清理工作')

    def test_add(self):
        """ Test method add(a,b) """
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(4,add(4,2))

    def test_minus(self):
        """ Test method minus(a,b) """
        self.assertEqual(1,minus(3,2))

    def test_multi(self):
        """ Test method multi(a,b) """
        self.assertEqual(6,multi(3,2))

    # def test_divide(self):
    #     """ Test method divide(a,b) """
    #     self.assertEqual(2,divide(6,3))
    #     self.assertEqual(2,divide(5,2))
    @unittest.skip("我不想执行此case")
  
    def test_divide(self):
        """ Test method divide(a,b) """
        print(divide)
        self.assertEqual(2,divide(6,3))
        self.assertEqual(2,divide(5,2))

if __name__ == '__main__':
    unittest.main(verbosity=2)
