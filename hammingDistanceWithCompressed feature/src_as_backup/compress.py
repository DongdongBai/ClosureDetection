#!/usr/bin/env python
# coding=utf-8
import numpy as np
import io_compress
def compress(layer_name):
    f = file("/home/bdd/Desktop/src_code2/"+layer_name+".npy", "a+b")
    A=np.load(f)
    i=1
    while i<2474:
        a=np.load(f)
        A=np.vstack((A,a))
        i=i+1;
    print "OK"
    R=np.random.normal(0.0,1,(64896,8192))
    R_A=A.dot(R)
    print R_A.shape
    io_compress.write_array(R_A,layer_name)
    print 'WRITE OK!'
