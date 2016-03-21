#!/usr/bin/env python
# coding=utf-8
import time
import CompressFeature
import CompressedCalHamming
import CompressedPlotPresicionRecall




if __name__=='__main__':
    
    Conv3_compress=CompressFeature.CompressFeature("pool5",2048)    
    Conv3_compress.FeatureCompress()
    Conv3_compress.WriteCompressedFeature()
    
    
    
    conv3Hamming=CompressedCalHamming.HammingDistance('pool5',9216,2048)
    conv3Hamming.LoadCompressedFeature()
    start=time.clock()
    conv3Hamming.CalHammingDistance()
    end=time.clock()
    print "Caculate hamming distance is (%f)s!"  %(end-start)
    conv3Hamming.WriteHammingDistance()
    
    
    conv3Plot=CompressedPlotPresicionRecall.PlotPrecisionRecall('pool5',9216,2048)
    conv3Plot.LoadHammingDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()