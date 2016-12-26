#-*- coding:utf-8 -*-

s = input("请输入蔬菜名：")
s2 = s.split('，')
def Veg(s):
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if j != i:
                print (s[i],end='')
                print (s[j])

Veg(s2)