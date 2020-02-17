import unittest
from test_mathfunc import TsetMathFunc
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
# 把结果输出到控制台
    # suite = unittest.TestSuite()

    # tests = [TsetMathFunc("test_add"),TsetMathFunc("test_minus"),TsetMathFunc("test_divide")]
    # suite.addTests(tests)

    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
# 将结果输出到文件中
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TsetMathFunc))

    # """  
    # with open('UnittestTextReport.txt','a') as f:
    #     runner = unittest.TextTestRunner(stream=f,verbosity=2)
    #     runner.run(suite) 
    # unitest框架自带的测试报告
    # """
    with open ('HTMLReport.html','w') as f:
        runner = HTMLTestRunner(stream=f,
                                title='MathFunc Test Report',
                                description='优化后的测试报告',
                                verbosity=2,

                                )
        runner.run(suite)