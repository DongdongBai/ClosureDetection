#!/usr/bin/env python
# coding=utf-8
import numpy as np
import time
class EuclideanDistance(object):
    def __init__(self,dataset,layerName):
        self.layerName=layerName
        self.dataset=dataset
        
    def LoadOriginFeature(self):
        f = file("/home/bdd/Desktop/ClosureDetectionProject/"+self.dataset+"Feature/"+self.layerName+".npy", "a+b")
        self.originalFeature=np.load(f)
        getFeatureTimes=1
        while getFeatureTimes<2474:
            tmpFeature=np.load(f)
            self.originalFeature=np.vstack((self.originalFeature,tmpFeature))
            getFeatureTimes=getFeatureTimes+1;
        f.close()
        self.orignalDim = self.originalFeature.shape[1]
        print "The original feature of (%s) has been read!Ths shape is %s" %(self.layerName,str(self.originalFeature.shape))
        print "Load Original feature is OK!"    
        
    def CalEuclideanDistance(self):    
#         self.isAboveZero=self.originalFeature>=0
#         self.isAboveZero.dtype='int8'
        dim=self.originalFeature.shape[0]
        self.Distance=np.ones((dim,dim))*(-1)
        i=0
        while i<dim:
            j=0
            while j<i:
                self.Distance[(i,j)]=np.sum((self.originalFeature[i]-self.originalFeature[j])**2)
                j=j+1      
            i=i+1 
    def WriteEuclideanDistance(self):
        np.savetxt("../data/"+self.dataset+"Original_EuclideanDistance_"+self.layerName+"_"+str(self.orignalDim)+".txt", self.Distance ,fmt="%f") #改为保存为整数
#         f = file("EuclideanDistance_"+self.layerName+".npy", "a+b")
#         np.save(f,self.Distance)
#         f.close()
        print "The Euclidean Distance of (%s) has been write to disk"  %(self.layerName)


# conv3Hamming=EuclideanDistance('CityCenter','pool5')
# conv3Hamming.LoadOriginFeature()
# start=time.clock()
# conv3Hamming.CalEuclideanDistance()
# end=time.clock()
# print "Caculate hamming distance is (%f)s!"  %(end-start)
# conv3Hamming.WriteEuclideanDistance()

