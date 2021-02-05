from lxml import etree
import requests

if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    html = requests.get(url=url, headers=headers).text
    tree = etree.HTML(html)
    # hot_list = tree.xpath('//div[@class = "bottom"]/ul/li')
    # all_citys = []
    # for li in hot_list:
    #     name = li.xpath('./a/text()')[0]
    #     all_citys.append(name)
    # all_list = tree.xpath('//div[@class = "bottom"]/ul/div[2]/li')
    # for i in all_list:
    #     name_ = i.xpath('./a/text()')[0]
    #     all_citys.append(name_)
    # print(all_citys)
    citys = tree.xpath('//div[@class = "bottom"]/ul/li | //div[@class = "bottom"]/ul/div[2]/li')
    for city in citys:
        name = city.xpath('./a/text()')[0]
        print(name)