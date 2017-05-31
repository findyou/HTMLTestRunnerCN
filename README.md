"# python" 

一、HTMLTestRunnerEN 使用
有时大伙会觉得英语会有莫名的逼格（感叹,沉默），所以保留了英文显示，满足大家的需要，报告内容支持中文显示。
```python
import HTMLTestRunnerEN
...
if __name__ == '__main__':
    filePath ='F:\\Report.html'
    fp = file(filePath,'wb')
    runner = HTMLTestRunnerEN.HTMLTestRunner(
        stream=fp,
        title='{ Test Report }',
        #description='',
        #tester="Findyou"
        )
    runner.run(Suite())
```


二、HTMLTestRunnerCN 使用

```python
import HTMLTestRunnerCN
...
if __name__ == '__main__':
    #确定生成报告的路径
    filePath ='F:\\Report.html'
    fp = file(filePath,'wb')
    #生成报告的Title,描述
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告',
        #description='详细测试用例结果',
        tester=u"Findyou"
        )
    #运行测试用例
    runner.run(Suite())

```
