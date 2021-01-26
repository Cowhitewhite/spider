'''
 BeautifulSoup4将复杂html文档转换成一个复杂的树形结构，每个节点都是一个python对象，大致分为
 - Tag
 - NavigableString
 - BeautifulSoup
 - Comment
'''
from bs4 import BeautifulSoup
import re

reName = re.compile("")

file = open("./test.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")
print(bs.findAll('dd')[0].text)
print(bs.findAll('dd')[6].find('a').get('href'))
# print(bs.title)
# print(bs.a)
# print(bs.head)
# print(type(bs.head))
# print(bs.title.string)
# print(type(bs.title.string))
# print(bs.a.attrs)
# print(bs.name)
# print(bs.a.string)


# 1.Tag 标签及其内容：拿到它所找到的第一个内容
# 2.NavigableString 标签里边的内容(字符串)
# 3.BeautifulSoup 表示整个文档
# 3.Comment 是一个特殊的NavigableString,输出的内容不包含注释符号

# --------------------------------------------

# 文档的遍历
# print(bs.head.contents[1])
# for i in bs.head.contents:
#     print(i)

# 文档的搜索
# 1. find_all() 字符转过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")
# for i in t_list:
#     print(i)

# search() 正则表达式搜索
# t_list = bs.find_all(re.compile("a"))
# 方法： 传入一个函数（方法）,根据函数的要求搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)
# for item in t_list:
#     print(item)

# 2. kwargs参数
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_=True)
# for item in t_list:
#     print(item)

# 3. text参数
# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123","地图","贴吧"])
# t_list = bs.find_all(text= re.compile("\d"))
# for item in t_list:
#     print(item)

# 3. limit参数
# t_list = bs.find_all(text="a",limit=3)


# CSS选择器
# print(bs.select("title")) # 通过标签来查找
# print(bs.select(".mnav")) # 通过class雷鸣查找
# print(bs.select("#u1")) # 通过id查找
# print(bs.select("a[class = 'bri']")) # 通过属性查找
# print(bs.select("head > title")) # 通过子标签查找
# print(bs.select(".mnav ~ .bri")[0].get_text())


