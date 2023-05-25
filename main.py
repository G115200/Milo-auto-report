from functions import *

def main():
    report_center = input("客户单位名称：")
    report_systemname = input("测试系统名称：")
    report_test_url = list(input("请输入测试目标:").split())
    flag = input("是否需要输入漏洞？1（输入漏洞）、2（跳过漏洞，输入测试项）")
    vuls = {}
    ceshi = {}
    vul_list = [] #input的结果还要放进match中比对
    vuls_list = [] #最终漏洞进入列表
    ceshi_list = [] #最终测试项进入列表
    while flag == '1':
        vul_list = list(vul_input())
        match_result = match(vul_list[0])
        if match_result[2] == 0:
            vul_list[0] = list(vul_list[0])
            vul_list[0] = match_result[1]
            for i in match_result[0]:
                vul_list.append(i)
        while match_result[2] == 1:
            new_name = input("没有匹配到相似的数组,请重新输入漏洞名称:")
            match_result = match(new_name)
            if match_result[2] == 0:
                vul_list[0] = list(vul_list[0])
                vul_list[0] = match_result[1]
                for i in match_result[0]:
                    vul_list.append(i)
                break
        vuls_list.append(vul_list)
        flag_continue = input("还要继续输入吗？1（继续）2（停止）")

        if flag_continue == '2':
            print("漏洞输入结束，请输入测试项")
            flag = '2'
            break
    while flag == '2':
        ceshi_result = list(ceshi_input())
        ceshi_list.append(ceshi_result)
        flag_continue = input("还要继续输入吗？1（继续）2（停止）")

        if flag_continue == '2':
            print("测试项输入结束，请等待报告生成")
            break
    # print(vuls_list)
    vuls_result = []
    for vul in vuls_list:
        vul_accesspoint = zhuan(vul[1])
        level= zhuan(vul[3])
        # print("漏洞名称:{}\n测试接入点:{}\n漏洞URL:{}\n漏洞评级:{}\n利用过程:{}\n漏洞图片地址:{}\n漏洞详情:{}\n漏洞危害:{}\n修复建议:{}\n".format(vul[0], vul[1], vul[2],vul[3],vul[4],vul[5],vul[7],vul[8],vul[9]))
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
        }
        vuls_result.append(vuls)
    ceshi_result = []
    for ceshi in ceshi_list:
        ceshi_accesspoint = zhuan(ceshi[1])
        # print("测试项名称:{}\n测试接入点{}\n测试URL\n测试项图片地址:{}\n".format(ceshi[0], ceshi[1], ceshi[2],ceshi[3]))
        ceshis = {
            'ceshi_name':ceshi[0],
            'ceshi_accesspoint':ceshi_accesspoint,
            'ceshi_url':ceshi[2],
            'ceshi_image':ceshi[3],
        }
        ceshi_result.append(ceshis)
    high_all = [x[0] for x in vuls_list if x[3] == '3']
    middle_all = [x[0] for x in vuls_list if x[3] == '2']
    low_all = [x[0] for x in vuls_list if x[3] == '1']
    ceshi_all = [x[0] for x in ceshi_list]
    if len(high_all) == 0:
        high_all = '无'
    elif len(high_all) > 1:
        for i in range(len(high_all)):
            high_all[i] = str(i + 1) + '.' + high_all[i]

    if len(middle_all) ==0:
        middle_all = '无'
    elif len(middle_all) > 1:
        for i in range(len(middle_all)):
            high_all[i] = str(i + 1) + '.' + middle_all[i]
    if len(low_all) ==0:
        low_all = '无'
    elif len(low_all) > 1:
        for i in range(len(high_all)):
            low_all[i] = str(i + 1) + '.' + low_all[i]
    level_result = '安全系统'
    if int(len(high_all)) >= 3:
        level_result = '严重-不安全系统'
    elif int(len(high_all)) >= 1 or len(middle_all) >= 5:
        level_result = '高危-不安全系统'
    elif int(len(middle_all)) >= 1:
        level_result = '中危-不安全系统'
    elif int(len(low_all)) >= 5:
        level_result = '低危-不安全系统'
    else:
        level_result = '安全系统'
    highs = []
    middles = []
    lows = []
    ceshis = []
    report_test_urls = []
    for url in high_all:
        dict = {'high': url}
        highs.append(dict)
    for url in middle_all:
        dict = {'middle': url}
        middles.append(dict)
    for url in low_all:
        dict = {'low': url}
        lows.append(dict)
    for url in report_test_url:
        dict = {'url': url}
        report_test_urls.append(dict)
    data = {
        'report_center':report_center,
        'report_systemname':report_systemname,
        'report_test_url':report_test_urls,
        'high_all':highs,
        'middle_all':middles,
        'low_all':lows,
        'ceshi_all': ceshis,
        'count_addr':len(report_test_url),
        'count_vuls': len(vuls_list),
        'count_high': len(high_all),
        'count_middle': len(middle_all),
        'count_low': len(low_all),
        'level_result':level_result,
        'vuls':vuls_result,
        'ceshis':ceshi_result
        }

    # print(data)
    # output_report(data)
    xin_zhuan(data)
if __name__ == '__main__':
    main()


