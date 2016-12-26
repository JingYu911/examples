from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='localhost',unix_socket='/tmp/mysql.sock',user='root',password='94911',db='mysql',charset='utf-8')

cur = conn.cursor()
cur.execute("USE scraping")

random.seed(datetime.datetime.now())
def store(title, content):
    cur.execute("INSERT INTO pages (title,content) VALUES (\"%s\", \"%s\")",(title,content))
    # 提交，不然无法保存新建或者修改的数据
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div",{"id":"mw-content-text"}).find("p").get_text()
    store(title,content)
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",herf=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
try:
    while len(links)>0:
        newArticle = links[random.randint(0, len(links)-1)].attr["href"]
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()