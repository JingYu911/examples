file = open('test.txt', "rb")   #以二级制方式读取文件
s = file.read()
print(s)
# 输出 b'\xe4\xbc\x9f\xe5\xa4\xa7\xe7\x9a\x84\xe4\xb8\xad\xe5\x9b\xbd\r\n'
file = open('test.txt', "rb")
s = file.read().decode('utf-8')
print(s)
# 输出 伟大的中国