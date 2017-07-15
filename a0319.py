# coding:utf-8
#引用unittest框架
import unittest

#功能函数，制作hello測試案例
def hello():
    return 'Hello Word!'
def name():
    return 'Eva'

#进行验证案例是否符合预期要求
#继承自unittest.TestCase
class test(unittest.TestCase):
    def testHello(self):
        #assertEqual两个值是否相等
        self.assertEqual('Hello Word',hello())
    def testName(self):
        self.assertEqual('Eva1',name())

#执行
if __name__ == '__main__':
    unittest.main()