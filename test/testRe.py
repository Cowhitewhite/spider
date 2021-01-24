import re

# re库正则表达式

# pat = re.compile("AA") # 此处AA是正则表达式，用来验证其他的字符串
# m = pat.search("ASAABRAAAA") # search字符串是被校验的内容

# 没有模式对象
# m = re.search("asd","Aasd")
# print(m)
# print(re.findall("[A-Z]","ASDaDDDa"))

# sub函数
print(re.sub("a","A","aaaAAAAAvs")) # 找到a用A替换，在第三个字符串中查找"A"

# 建议在正则表达式中，被比较的字符串前面加上r,不用担心转义字符的问题
print(r"\aa\'")