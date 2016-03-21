#!/usr/bin/env python
# coding=utf-8
import numpy as np
import time

class HammingDistance(object):
    def __init__(self,layerName):
        self.layerName=layerName
    def LoadCompressedFeature(self):
        f = file("compressedFeature_"+self.layerName+".npy", "a+b")
        self.compressedFeature=np.load(f)
        f.close()
        print "Load Compressed feature is OK!"    
    def CalHammingDistance(self):    
        self.isAboveZero=self.compressedFeature>=0
        self.isAboveZero.dtype='int8'
        dim=self.compressedFeature.shape[0]
        self.Distance=np.ones((dim,dim),dtype='int')*(-1)
        i=0
        while i<dim:
            j=0
            while j<i:
                self.Distance[(i,j)]=np.sum(self.isAboveZero[i]^self.isAboveZero[j])
                j=j+1      
            i=i+1 
    def WriteHammingDistance(self):
        np.savetxt("hammingDistance_"+self.layerName+".txt", conv3Hamming.Distance, fmt="%d" ) #改为保存为整数
#         f = file("hammingDistance_"+self.layerName+".npy", "a+b")
#         np.save(f,self.Distance)
#         f.close()
        print "The Hamming Distance of (%s) has been write to disk"  %(self.layerName)



conv3Hamming=HammingDistance('conv3')
conv3Hamming.LoadCompressedFeature()
start=time.clock()
conv3Hamming.CalHammingDistance()
end=time.clock()
print "Caculate hamming distance is (%f)s!"  %(end-start)
conv3Hamming.WriteHammingDistance()
