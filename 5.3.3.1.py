import pymysql

# 创建连接
conn = pymysql.connect('host=127.0,0,1', unix_socket='mysql.sock',user='root',password='94911',db='mysql')
# 创建游标
cur = conn.cursor()
cur.execute("USE scraping")

cur.execute("SELECT * FROM pages where id = 1")
print(cur.fetchone)
cur.close()
conn.close()