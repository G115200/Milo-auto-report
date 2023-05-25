from docxtpl import DocxTemplate
def vul_input():
    vul_name = input("请输入漏洞名称：")
    accesspoint = input("请输入测试接入点：3（互联网）、4（内网）")
    addr = input("漏洞URL:")
    level = input("请输入漏洞评级：")
    process = input("请输入利用过程：")
    image_url = input("请输入漏洞验证图片地址：")
    return vul_name,accesspoint,addr,level,process,image_url

def ceshi_input():
    ceshi_name = input("请输入测试项名称：")
    accesspoint = input("请输入测试接入点：3（互联网）、4（内网）")
    addr = input("测试项URL:")
    image_url = input("请输入漏洞验证图片地址：")
    return ceshi_name,accesspoint,addr,image_url

def match(vul_name):
    blog = 0
    match = []
    m = ''
    new_name = vul_name
    vul_template_ku = []
    with open('demo/漏洞模板库.txt', 'r',encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line_list = line.split()
            vul_template_ku.append(line_list)
    matches = []
    for row in vul_template_ku:
        vul_name = str(vul_name).lower()
        m = row[0]
        m = str(m).lower()
        if vul_name in m:
                matches.append(row)
    if len(matches) > 0:
        print("以下数组与您的输入相似：")
        for match in matches:
            print(match[0])
        i = int(input("请输入您需要的选项"))
        match = matches[i-1]
        new_name = match[0]
    else:
        blog = 1
    return match,new_name,blog

def zhuan(level):
    if level == 1:
        level = '低危'
    elif level == 2:
        level = '中危'
    elif level == '3':
        level = '互联网'
    elif level == '4':
        level = '内网'
    else:
        level = '高危'
    return level

# def output_report(data):
#     doc_file = 'demo/1.docx'
#     doc = Document(doc_file)
#     for k in data.keys():  # 遍历字典中所有键
#         s = '{{' + k + '}}'
#         for paragraph in doc.paragraphs:
#             text = paragraph.text
#             if s in text:
#                 paragraph.text = text.replace(s, str(data[k]))
#
#         for table in doc.tables:
#             # 遍历表格中的每一行
#             for row in table.rows:
#                 # 遍历每一列
#                 for cell in row.cells:
#                     # 输出单元格中的内容
#                     if s in cell.text:
#                         cell.text = cell.text.replace(s, str(data[k]))
#
#     doc.save('1.docx')

def xin_zhuan(data):
    doc = DocxTemplate('demo/1.docx')
    # 创建字典,key与模版文件中的模版变量一一对应,value为要写入到末班中{{key}}处的值.

    # 模版文件读取写入字典
    doc.render(data)
    # 保存结果到新的docx文件
    doc.save('2023xxxx-等保-XXXXXX-XXXX系统-渗透测试报告.docx')
