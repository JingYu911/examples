#-*- coding:utf-8 *-

s = input("请输入字符: ")
str =''.join(s)
print(str)

def fun(s):
    for i in range(0,len(str)):
        print (str[i])

fun(str)
