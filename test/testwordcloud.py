import jieba                        # 分词
from matplotlib import pyplot       # 绘图，数据可视化
from wordcloud import WordCloud     # 词云
from PIL import Image               # 图片处理
import numpy                        # 矩阵运算
import sqlite3

# 数据准备
conn = sqlite3.connect("../movie.db")
cur = conn.cursor()
sql = "select introduction from movie"
data = cur.execute(sql)
text = ""
for i in data:
    text += i[0]
cur.close()
conn.close()

# 分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))

img = Image.open(r'tree.jpg')
img_array = numpy.array(img) # 图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='simkai.ttf'
)
wc.generate_from_text(string)

# 绘制图片
fig = pyplot.figure(1)
pyplot.imshow(wc)
pyplot.axis('off') # 是否显示坐标轴
# pyplot.show()  # 显示生成的词云
pyplot.savefig(".\word.jpg")