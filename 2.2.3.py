from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child) #只打印子标签tr标签
print("-------------------------------------------------")

for descendant in bsObj.find("table", {"id":"giftList"}).descendants:
    print(descendant) #打印所有后代标签tr、th 、td、 img
print("++++++++++++++++++++++++++++++++++++++++++++++++++")

''''
for sibling in bsObj.find("table",{"id","giftList"}).tr.next_siblings:
    print(sibling) #打产品列表里的所有行的产品，打印列表中除第一行标题行以外的所有兄弟标签
'''
print("----------------------------------------------------")

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
#打印上一个父标签