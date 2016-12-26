#-*- coding:utf-8
s = input("请输入一段字符： ")
str =''.join(s)
def  fun(str):
    endstr = str[-2:]
    if endstr == 'PY':
        print ('YES')
    else:
        print ('NO')
fun(str)
print (str[:-5:-2])
print (str[::-1])
