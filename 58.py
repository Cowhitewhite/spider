from lxml import etree
import requests

if __name__ == '__main__':
    url = 'https://cd.58.com/ershoufang/'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    html = requests.get(url, headers).text
    #数据解析
    tree = etree.HTML(html)
    titles = tree.xpath('//h3[@class="property-content-title-name"]/text()')
    for title in titles:
        print(title)