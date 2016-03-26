#!/usr/bin/env python
# coding=utf-8
import numpy as np
import time
class EuclideanDistance(object):
    def __init__(self,dataset,layerName,orignalDim,CompressedDim):
        self.dataset=dataset
        self.layerName=layerName
        self.orignalDim=orignalDim
        self.CompressedDim=CompressedDim
    def LoadCompressedFeature(self):
        f = file("../data/"+self.dataset+"compressedFeature_"+self.layerName+"_"+str(self.orignalDim)+" to "+str(self.CompressedDim)+".npy", "a+b")        
        self.CompressedFeature=np.load(f)
        f.close()
        print "Load Compressed feature is OK!"    
    def CalEuclideanDistance(self):    
        self.isAboveZero=self.CompressedFeature>=0
        self.isAboveZero.dtype='int8'
        dim=self.CompressedFeature.shape[0]
        self.Distance=np.ones((dim,dim),dtype='int')*(-1)
        i=0
        while i<dim:
            j=0
            while j<i:
                self.Distance[(i,j)]=np.sum(self.isAboveZero[i]^self.isAboveZero[j])
                j=j+1      
            i=i+1 
    def WriteEuclideanDistance(self):
        np.savetxt("../data/"+self.dataset+"compressed_EuclideanDistance_"+self.layerName+"_"+str(self.orignalDim)+" to "+str(self.CompressedDim)+".txt", self.Distance, fmt="%d" ) #改为保存为整数
#         f = file("EuclideanDistance_"+self.layerName+".npy", "a+b")
#         np.save(f,self.Distance)
#         f.close()
        print "The Euclidean Distance of (%s) has been write to disk"  %(self.layerName)


# conv3Hamming=EuclideanDistance('CityCenter','pool5',9216,1024)
# conv3Hamming.LoadCompressedFeature()
# start=time.clock()
# conv3Hamming.CalEuclideanDistance()
# end=time.clock()
# print "Caculate Euclidean distance is (%f)s!"  %(end-start)
# conv3Hamming.WriteEuclideanDistance()

