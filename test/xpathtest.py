from lxml import etree

if __name__ == '__main__':
    tree = etree.parse('test/baidu.html')
    # r = tree.xpath('/html/body/div')
    # r = tree.xpath('/html//div')
    # r = tree.xpath('//div')
    # r = tree.xpath('//div[@id = "u1"]') # 属性定位
    # r = tree.xpath('//div[@id = "u1"]/a[@class = "bri"]') # 属性定位
    # r = tree.xpath('//div[@id = "u1"]/a[7]/text()')[0] # 获取标签中的文本
    r = tree.xpath('//div[@id = "u1"]/a[@class = "bri"]/@href') # 取属性
    print(r)