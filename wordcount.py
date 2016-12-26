#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input("请输入一段字符: ")
str = s.lower()
lis = s.split(' ')
print(lis)
count = {}
def fun(s):
    lis = []
    for i in range(0,len(s)):
        if s[i] not in lis:
            lis.append(s[i])
            count = 1
        else:
            count += 1
fun(str)