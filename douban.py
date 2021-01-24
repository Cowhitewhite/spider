# coding = utf-8

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定url，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作


def main():
    baseUrl = "https://movie.douban.com/top250?start="
    dataList = getData(baseUrl)
    # savePath = ".\\top250.xls"
    # saveData(dataList, savePath)
    dbPath = "movie.db"
    saveDb(dataList, dbPath)


# 影片详情
findlink = re.compile(r'<a href="(.*?)">')  # 正则表达式对象规则
# 影片图片链接
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S 让换行符包含在字符中
# 影片片面
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findScore = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findReview = re.compile(r'<span>(\d*)人评价</span>')
# 概况
findInfo = re.compile(r'<span class="inq">(.*)</span>')
# 影片相关类容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(baseUrl):
    dataList = []
    for i in range(0, 10):  # 调用获取页面信息函数10次
        url = baseUrl + str(i * 25)
        html = askUrl(url)  # 保存获取到的网页源码
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):  # 查找符合要求字符串，形成列表
            data = []  # 电影信息
            item = str(item)
            # 影片详情
            link = re.findall(findlink, item)[0]
            data.append(link)
            # 影片图片链接
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            # 影片标题
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
                cnTitle = titles[0]
                data.append(cnTitle)
                enTitle = titles[1].replace("/", "")
                data.append(enTitle)
            else:
                data.append(titles[0])
                data.append(" ")
            # 评价分数
            score = re.findall(findScore, item)[0]
            data.append(score)
            # 评价人数
            review = re.findall(findReview, item)[0]
            data.append(review)
            # 概况
            infos = re.findall(findInfo, item)
            if len(infos) != 0:
                info = infos[0].replace("。", "")
                data.append(info)
            else:
                data.append(" ")
            # 影片相关类容
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', "", bd)  # 去掉<br/>
            bd = re.sub("/", "", bd)
            data.append(bd.strip())  # 去掉前后空格

            dataList.append(data)
    return dataList


# 保存数据
def saveData(datalist, path):
    print("save.....")
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = workbook.add_sheet(sheetname="top250", cell_overwrite_ok=True)  # 创建sheet对象
    row = ("详情链接", "图片链接", "影片中文名", "影片外文名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, len(row)):
        sheet.write(0, i, row[i])
    for i in range(0, len(datalist)):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
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
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveDb(datalist, dbpath):
    # init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
              insert into movie(info_link,pic_link,cn_name,en_name,score,rated,introduction,info)
              values (%s)'''%",".join(data)
        print(sql)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()

def init_db(dbpath):
    sql = '''
       create table movie(
         id integer primary key autoincrement,
         info_link text,
         pic_link text,
         cn_name varchar,
         en_name varchar ,
         score numeric,
         rated numeric,
         introduction text,
         info text
       );
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # 调用函数
    main()
    print("complete!!!")
