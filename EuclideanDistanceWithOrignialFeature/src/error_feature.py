#!/usr/bin/env python
# coding=utf-8
import distance
import io_dis
import io_label
import numpy as np


def label(layer_name):
    f = file(layer_name+".npy", "rb")

    A=np.load(f)
#     tmp=B**2
#     A=B/np.sqrt(tmp.sum())

    i=1
    condtion=True
    while condtion:
        try:
            a=np.load(f)
            if np.isnan(a.sum()):
                dim =a.shape
                j=0
                while j<dim[0]:
                    if np.isnan(a[j]):
                        print i,j
                    j=j+1
                
#             tmp=a**2
#             a=a/np.sqrt(tmp.sum())
            A=np.vstack((A,a))
#             print """i=%d,""" %(i)
            i=i+1;
        except:
            condtion=False
            print "error"
#     H=A.shape
#     dim=H[0]
# #     print dim
# #     return A
#     DIS=np.zeros((dim,dim))
#     i=0
#     while i<dim:
#         j=i+1
#         while j<dim:
#             DIS[(i,j)]=distance.distance(A[i],A[j])
# #             print "i=%d,j=%d" %(i,j)
#             j=j+1      
#         i=i+1 
#     i=0
#     while i<dim:
#         j=i+1
#         while j<dim:
#             DIS[j,i]=DIS[i,j]
#             j=j+1
#         i=i+1
# #     print DIS.shape
#        
#     io_dis.write_array(DIS,layer_name)
#    
#    
#    
#     b=DIS.argsort()
#     print b
#        
#     index=b[:,1:6]
#     print index 
#        
#     io_label.write_array(index,layer_name)
