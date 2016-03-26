#!/usr/bin/env python
# coding=utf-8
import numpy as np
import time
class CosineDistance(object):
    def __init__(self,dataset,layerName):
        self.dataset=dataset
        self.layerName=layerName
        
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
        
    def CalCosineDistance(self):    
#         self.isAboveZero=self.originalFeature>=0
#         self.isAboveZero.dtype='int8'
        dim=self.originalFeature.shape[0]
        self.Distance=np.ones((dim,dim))*(-2)
        i=0
        while i<dim:
            j=0
            while j<i:
                self.Distance[(i,j)]=np.dot(self.originalFeature[i],self.originalFeature[j])/(np.linalg.norm(self.originalFeature[i])*np.linalg.norm(self.originalFeature[j]))
                j=j+1      
            i=i+1 
    def WriteCosineDistance(self):
        np.savetxt("../data/"+self.dataset+"Original_CosineDistance_"+self.layerName+"_"+str(self.orignalDim)+".txt", self.Distance ,fmt="%f") #改为保存为整数
#         f = file("CosineDistance_"+self.layerName+".npy", "a+b")
#         np.save(f,self.Distance)
#         f.close()
        print "The Cosine Distance of (%s) has been write to disk"  %(self.layerName)


# conv3Hamming=CosineDistance('CityCenter','pool5')
# conv3Hamming.LoadOriginFeature()
# start=time.clock()
# conv3Hamming.CalCosineDistance()
# end=time.clock()
# print "Caculate hamming distance is (%f)s!"  %(end-start)
# conv3Hamming.WriteCosineDistance()

