from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
#.findAll(tag, attributes, recursive, text, limit, keywords)
#.find(tag, attributes, recursive, text, keywords)等价于limit = 1的findAll()

namelist = bsObj.findAll({"h1","h2","h3"})
print(namelist) #打印标签"h1","h2","h3"中的内容
# 输出： [<h1>War and Peace</h1>, <h2>Chapter 1</h2>]

namelist = bsObj.findAll("span", {"class":"green"})
for name in namelist:
    print(name.get_text())  #打印标签内的纯文本

namelist = bsObj.findAll(text = "the prince")
print(len(namelist))   #打印文本内容为"the price"的标签的个数

#递归参数recursive是个布尔变量，Flase只查找文档的一级标签，默认True为查找所有子标签
#关键字keywords选择具有指定属性(id)的标签