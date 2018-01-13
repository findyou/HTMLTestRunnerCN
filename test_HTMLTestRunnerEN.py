# -*- coding:utf-8 -*-

import unittest
import HTMLTestRunnerEN



#测试用例

class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testCase1(self):
        self.assertEqual(2,2,"testCase_Pass")

    def testCase2(self):
        self.assertEqual(2,3,"testCase_Fail")

    def testCase3(self):
        self.assertEqual(2,5,"测试错误")
        test_error

    def testCase4(self):
        self.assertEqual(2,2,"测试错误")
        findyou

    def testCase5(self):
        pass

class APITestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCase1(self):
        self.assertEqual(2, 2, "testCase_Pass")
        print("测试打印日志～")

    def testCase2(self):
        self.assertEqual(3, 3, "testCase_Pass")
        print("测试打印日志～")

    def testCase3(self):
        self.assertEqual(5, 5, "testCase_Pass")

    def testCase4(self):
        self.assertEqual(2, 1, "testCase_Error")
        findyou

    def testCase5(self):
        self.assertEqual(2, 6, "testCase_Fail")

    def testCase6(self):
        pass

#添加Suite
def Suite():
    #定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    #将测试用例加入到容器
    suiteTest.addTest(MyTestCase("testCase1"))
    suiteTest.addTest(MyTestCase("testCase2"))
    suiteTest.addTest(MyTestCase("testCase3"))
    suiteTest.addTest(MyTestCase("testCase4"))
    suiteTest.addTest(MyTestCase("testCase5"))
    suiteTest.addTest(APITestCase("testCase1"))
    suiteTest.addTest(APITestCase("testCase2"))
    suiteTest.addTest(APITestCase("testCase3"))
    suiteTest.addTest(APITestCase("testCase4"))
    suiteTest.addTest(APITestCase("testCase5"))
    suiteTest.addTest(APITestCase("testCase6"))
    return suiteTest

if __name__ == '__main__':
    #确定生成报告的路径
    filePath = '/Users/albert/PycharmProjects/HTMLTestRunnerCN/ReportCN.html'
    # filePath = 'F:\\ReportEN.html'
    fp = open(filePath,'wb')
    #生成报告的Title,描述
    runner = HTMLTestRunnerEN.HTMLTestReportEN(
        stream=fp,
        title='{ Test Report }',
        #description='详细测试用例结果',
        tester='Findyou'
        )
    #运行测试用例
    runner.run(Suite())
    # 关闭文件，否则会无法生成文件
    #fp.close()