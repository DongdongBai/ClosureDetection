#!/usr/bin/env python
# coding=utf-8
import extract_feature2
image_root= '/home/bdd/closure_loop_detect_data/City Center/Images/'
locate='/home/bdd/closure_loop_detect_data/City Center/Images/pic_list.txt'
F=open(locate)
for i in F:
    #num=len(i)
    s=i[0:8]
    print s
    extract_feature2.extract_feature(image_root+s)



