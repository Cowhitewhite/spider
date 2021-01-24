# coding = utf-8

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定url，获取网页数据
import xlwt  # 进行excel操作
import json


def main(city, search):
    # 090200代表城市 000000代表区域  00行业领域 1代表页数 9发布日期类型 99代表薪酬范围（01-99 ）
    baseUrl = "https://search.51job.com/list/" + city + ",000000,0000,00,9,99," + search + ",2,{}.html"
    # baseUrl = "https://search.51job.com/list/090200,000000,0000,00,9,99,java,2,1.html"
    datalist = getData(baseUrl)
    print(datalist)
    savePath = ".\\51job.xls"
    saveData(datalist, savePath)


# 影片详情
searchInfo = re.compile(r'window.__SEARCH_RESULT__\s=\s(.*)(?=<\/script>)')  # 正则表达式对象规则


# 爬取网页
def getData(baseUrl):
    datalist = []
    diclist = []
    for i in range(1, 69):  # 调用获取页面信息函数10次
        url = baseUrl.format(i)
        html = askUrl(url)  # 保存获取到的网页源码
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('script', type='text/javascript'):  # 查找符合要求字符串，形成列表
            item = str(item)
            info = re.findall(searchInfo, item)
            if len(info) != 0:
                diclist.append(info[0])
    for data in diclist:
        # 转换为json
        jsonStr = json.dumps(data)
        # 转换为字典
        result = json.loads(json.loads(jsonStr))
        for r in result['engine_search_result']:
            value = [str(r['job_href']), str(r['job_name']), str(r['company_name']), str(r['providesalary_text']),
                     str(r['workarea_text']), '', str(r['jobwelf_list']), str(r['companytype_text']), str(r['companysize_text']),
                     str(r['attribute_text']),str(r['workyear'])]
            datalist.append(value)
    return datalist


# 保存数据
def saveData(datalist, path):
    print("save.....")
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = workbook.add_sheet(sheetname="job", cell_overwrite_ok=True)  # 创建sheet对象
    row = ("工作链接", "工作名称", "公司名称", "薪资", "区域", "学历", "详情", "公司类型", "规模", "工作清单", "工作年限")
    for i in range(0, len(row)):
        sheet.write(0, i, row[i])
    for i in range(0, len(datalist)):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 11):
            sheet.write(i + 1, j, data[j])
    workbook.save(path)


# 得到指定一个URL的网页内容
def askUrl(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('gbk')
        print(url)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


if __name__ == "__main__":
    # 调用函数
    main("090200", "java")
    print("complete!!!")
