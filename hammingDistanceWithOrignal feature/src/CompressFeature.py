#!/usr/bin/env python
# coding=utf-8
import numpy as np
import time

class CompressFeature(object):
    
    
    def __init__(self,layerName,CompressedDim):
        self.layerName=layerName
        self.CompressedFeature=None
        self.CompressedDim=CompressedDim
        
    def FeatureCompress(self):
        f = file("/home/bdd/Desktop/ClosureDetectionProject/EuclideanDistanceWithOrignialFeature/data/"+self.layerName+".npy", "a+b")
        originalFeature=np.load(f)
        getFeatureTimes=1
        while getFeatureTimes<2474:
            tmpFeature=np.load(f)
            originalFeature=np.vstack((originalFeature,tmpFeature))
            getFeatureTimes=getFeatureTimes+1;
        self.orignalDim=originalFeature.shape[1]
        f.close()
        print "The original feature of (%s) has been read!Ths shape is %s" %(self.layerName,str(originalFeature.shape))
                
        randomArray=np.random.normal(0.0,1,(self.orignalDim,self.CompressedDim))
        
        start=time.clock()
        self.CompressedFeature=originalFeature.dot(randomArray)
        end=time.clock()
        print "The Time to compress (%s) feature from (%d) to (%d)  is (%f)s!"  %(self.layerName,self.orignalDim,self.CompressedDim,end-start)

        print "The compressed feature's shape of (%s) is (%s)"  %(self.layerName,str(self.CompressedFeature.shape))
    def WriteCompressedFeature(self):
            f = file("../data/compressedFeature_"+self.layerName+"_"+str(self.orignalDim)+" to "+str(self.CompressedDim)+".npy", "a+b")
            np.save(f,self.CompressedFeature)
            f.close()
            print "The compressed feature of (%s) has been write to disk"  %self.layerName




# Conv3_compress=CompressFeature("pool5",1024)    
# Conv3_compress.FeatureCompress()
# Conv3_compress.WriteCompressedFeature()
