import requests
import threading
import xlwt
from bs4 import BeautifulSoup
import json
import time

datalit = []
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]

def download_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    return r.text


def get_bt(html):
    soup = BeautifulSoup(html, 'html.parser')
    bt_list = soup.find('div', class_='body threadlist').find_all('table')
    for table in bt_list:
        info = table.find('a', class_='subject_link thread-new')
        if info is not None:
            link = info.get('href')
            open_info(link)


def open_info(link):
    html = download_page(link)
    time.sleep(2)
    soup = BeautifulSoup(html, 'html.parser')
    if soup.find('div', class_='attachlist') is not None:
        td_list = soup.find('div', class_='attachlist').findAll('td')
        for td in td_list:
            ajax = td.find('a', class_='ajaxdialog')
            if ajax is not None:
                ajax_url = ajax.get('href')
                print(ajax_url)
                open_result(ajax_url)


# 此处需要调用接口
def open_result(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    rsp = requests.get(url, headers=headers)
    dic = json.loads(rsp.content.decode('utf-8'))
    html = str(dic['message']['body'])
    result = BeautifulSoup(html, 'html.parser')
    dds = result.findAll('dd')
    data = []
    data.append(str(dds[0].text))
    data.append(str(dds[6].find('a').get('href')))
    datalit.append(data)
    time.sleep(2)


def writeExcel(datalist):
    print("save.....")
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = workbook.add_sheet(sheetname="movie", cell_overwrite_ok=True)  # 创建sheet对象
    row = ("电影名称", "BT下载地址")
    for i in range(0, len(row)):
        sheet.write(0, i, row[i])
    for i in range(0, len(datalist)):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 2):
            sheet.write(i + 1, j, data[j])
    workbook.save("test.xls")


def execute(url, datalist):
    page_html = download_page(url)
    get_bt(page_html)
    writeExcel(datalist)


# 主函数
def main():
    queue = [i for i in range(1, 10)]
    threads = []
    while len(queue) > 0:
        cur_page = queue.pop(0)
        url = 'http://www.33btjia.com/forum-index-fid-1-page-{}.htm'.format(cur_page)
        print(url)
        execute(url, datalit)
        print('{}正在下载{}页'.format(threading.current_thread().name, cur_page))


if __name__ == '__main__':
    main()
