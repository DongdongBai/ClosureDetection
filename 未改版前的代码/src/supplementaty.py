#!/usr/bin/env python
# coding=utf-8
f1=open('result.py','r+')
f2=open('result2.py','w+')
for i in f1:
        s='    '+i
        f2.write(s)
f2.close()
