#!/usr/bin/env python
# coding=utf-8
import numpy as np
class CompressFeature(object):
    def __init__(self,layerName):
        self.layerName=layerName
        self.compressedFeature=None
    def CompressFeature(self):
        f = file("/home/bdd/Desktop/src_code2/"+self.layerName+".npy", "a+b")
        originalFeature=np.load(f)
        getFeatureTimes=1
        while getFeatureTimes<2474:
            tmpFeature=np.load(f)
            originalFeature=np.vstack((originalFeature,tmpFeature))
            getFeatureTimes=getFeatureTimes+1;
        f.close()
        print "The original feature of (%s) has been read!" %(self.layerName)
        randomArray=np.random.normal(0.0,1,(64896,8192))
        self.compressedFeature=originalFeature.dot(randomArray)
        print "The compressed feature's shape is %s"  %(str(self.compressedFeature.shape))
    def WriteCompressedFeature(self):
            f = file("compressedFeature_"+self.layerName+".npy", "a+b")
            np.save(f,self.compressedFeature)
            f.close()
            print "The compressed feature of (%s) has been write to disk"  %self.layerName





Conv3_compress=CompressFeature("conv3")    
Conv3_compress.CompressFeature()
Conv3_compress.WriteCompressedFeature()