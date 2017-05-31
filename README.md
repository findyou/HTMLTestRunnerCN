[#说明]
=========================
python输出的报告真的很丑,于是找了一圈没有我自已想要的html，所以自己动手进行了美化<br>
原作者文件下载地址：http://tungwaiyip.info/software/HTMLTestRunner.html<br>
我基于其Version 0.8.2进行了修改美化具体内容如下：<br>
```python
Version 0.8.2.1 -Findyou
* 支持中文，汉化
* 调整样式，美化（需要连入网络，使用的百度的Bootstrap.js）
* 增加 通过的分类显示、测试人员、通过率的展示
* 增加“详细”与“收起”状态效果的变换
* 增加返回顶部的锚点
```
[#如何使用]
=========================
##一、HTMLTestRunnerEN 使用
--------------------------
有时大伙会觉得英语会有莫名的逼格（感叹,沉默），所以保留了英文显示，满足大家的需要，报告内容支持中文显示。
<br>
* 编写test_HTMLTestRunnerEN.py<br>
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

* 执行test_HTMLTestRunnerEN.py<br>
```python
python test_HTMLTestRunnerEN.py
```

* 执行结果：Report.html
![](https://github.com/findyou/python/blob/master/Report_EN.gif "测试结果") 

##二、HTMLTestRunnerCN 使用
--------------------------
使用同HTMLTestRunnerEN，无区别<br>
* 执行结果：Report.html
![](https://github.com/findyou/python/blob/master/Report_CN.gif "测试结果") 
