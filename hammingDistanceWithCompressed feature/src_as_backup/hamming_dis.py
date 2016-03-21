#!/usr/bin/env python
# coding=utf-8
import numpy as np
import io_hamming_dis

def label(layer_name):
    f = file("Compressed"+layer_name+".npy", "a+b")
    R_A=np.load(f)

    print "Load Compressed feature is OK"    
    Z=np.zeros(R_A.shape, dtype='int') 
    Index=(R_A>=0)
    Z[Index]=1

    H=R_A.shape
    dim=H[0]
    Distance=np.zeros((dim,dim))
    i=0
    while i<dim:
        j=0
        while j<i:
            Distance[(i,j)]=np.sum(Z[i]^Z[j])
#             print "i=%d,j=%d" %(i,j)
            j=j+1      
        i=i+1 
    io_hamming_dis.write_array(Distance,layer_name)