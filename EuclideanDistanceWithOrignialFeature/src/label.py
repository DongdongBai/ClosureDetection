#!/usr/bin/env python
# coding=utf-8
import distance
import io_dis
import io_label
import numpy as np


def label(layer_name):
    f = file(layer_name+".npy", "a+b")

    A=np.load(f)
#     tmp=B**2
#     A=B/np.sqrt(tmp.sum())

#     i=1
#     condtion=True
#     while condtion:
#         try:
#             a=np.load(f)
# #             tmp=a**2
# #             a=a/np.sqrt(tmp.sum())
#             A=np.vstack((A,a))
# #             print """i=%d,""" %(i)
#             i=i+1;
#         except:
#             condtion=False
#             print "error"



    i=1
    while i<2474:
        a=np.load(f)
        A=np.vstack((A,a))
#       print """i=%d,""" %(i)
        i=i+1;
    print "OK"


    H=A.shape
    dim=H[0]
#     print dim
#     return A
    DIS=np.zeros((dim,dim))
    i=0
    while i<dim:
        j=0
        while j<i:
            DIS[(i,j)]=distance.distance(A[i],A[j])
#             print "i=%d,j=%d" %(i,j)
            j=j+1      
        i=i+1 
        
        
#     i=0
#     while i<dim:
#         j=i+1
#         while j<dim:
#             DIS[j,i]=DIS[i,j]
#             j=j+1
#         i=i+1
#     print DIS.shape
       
    io_dis.write_array(DIS,layer_name)
    
    
    
#     index=np.zeros((2474,5))
#     i=5
#     while i<2474:
#         row=DIS[i,0:i]
#         index_temp=row.argsort()
#         index[i]=index_temp[0:5]
#         i=i+1
#     
   
   
#    
#     b=DIS.argsort()
#     print b
       
#     index=b[:,1:6]
#     print index 
#        
#     io_label.write_array(index,layer_name)
