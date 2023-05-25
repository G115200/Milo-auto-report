# Milo自动化出报告系统



## 前言:

各位安全工程师每天总是有出不完的报告(本人:渗透五分钟,报告两小时)

从自己记录的文档查到出报告模板,漏洞模板,极其麻烦

而这个系统(先说缺点,纯命令行,图片不好插,本人不会前端,纯粹狗屎),可以帮助各位在出报告时更据需求自定义模板,并且快速的输出所需要的内容

![image-20230524154123321](D:\代码\python\图集\README\image-20230524154123321.png)

```shell
-demo # 模板文件夹
	-1.docx # 目前选用的模板
	-漏洞模板库.txt #漏洞相关信息都写进这个文件就可以(千万不要有空格!!!!!!!!!!)
-venv # 虚拟环境
-function.py # 被调用的方法文件夹
-main.py # 主函数文件
```

## 环境

```shell
pip install docxtpl
```



## 用户输入

```python
# 需要用户输入的内容(图片一类的之前是想着输入绝对路径读取的,后来想想太麻烦了,有那功夫直接复制粘贴好了)
vul_name = input("请输入漏洞名称：")
    accesspoint = input("请输入测试接入点：3（互联网）、4（内网）")
    addr = input("漏洞URL:")
    level = input("请输入漏洞评级：")
    process = input("请输入利用过程：")
    image_url = input("请输入漏洞验证图片地址：")
ceshi_name = input("请输入测试项名称：")
    accesspoint = input("请输入测试接入点：3（互联网）、4（内网）")
    addr = input("测试项URL:")
    image_url = input("请输入漏洞验证图片地址：")
```



## 模板制作

```python
# jinjia2是支持用户自定义模板的,本质还是关键字匹配只需要{{变量}}(用的库是docxptl,这个库集成了jinjia2,单纯用jinjia2,一直有编码问题无法解决。)
vuls = {
            'vul_name':vul[0],
            'vul_accesspoint':vul_accesspoint,
            'vul_url':vul[2],
            'vul_level':level,
            'vul_describe':vul[4],
            'vul_image':vul[5],
            'vul_details':vul[7],
            'vul_harm':vul[8],
            'vul_repair':vul[9],
ceshis = {
            'ceshi_name':ceshi[0],
            'ceshi_accesspoint':ceshi_accesspoint,
            'ceshi_url':ceshi[2],
            'ceshi_image':ceshi[3],
        }
data = {
        'report_center':report_center,
        'report_systemname':report_systemname,
        'report_test_url':report_test_url,
        'high_all':high_all,
        'middle_all':middle_all,
        'low_all':low_all,
        'ceshi_all': ceshi_all,
        'count_addr':len(report_test_url),
        'count_vuls': len(vuls_list),
        'count_high': len(high_all),
        'count_middle': len(middle_all),
        'count_low': len(low_all),
        'level_result':level_result,
        'vuls':vuls_result,
        'ceshis':ceshi_result
        }
 # data段可以使用{{key}}的方式直接写进模板，ceshi以及vul段是数组，里面包含了字典，一个字典就是一个漏洞（测试项），要用到for这样一段的jinjia2模板语法，具体可以参照1.docx
```

