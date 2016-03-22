#!/usr/bin/env python
# coding=utf-8
import time
import matplotlib.pylab as plt
import CompressFeature
import CompressedCalHamming
import CompressedPlotPresicionRecall


if __name__=='__main__':
    
    
    Recall=[]
    Precision=[]
    titles=[]
    lines=[]

#--------------------------------------------------------------------------------------------------------------------------------------    
    
    Conv3_compress=CompressFeature.CompressFeature("conv3",8192)    
    Conv3_compress.FeatureCompress()
    Conv3_compress.WriteCompressedFeature()  
    
    conv3Hamming=CompressedCalHamming.HammingDistance('conv3',64896,8192)
    conv3Hamming.LoadCompressedFeature()
    start=time.clock()
    conv3Hamming.CalHammingDistance()
    end=time.clock()
    print "Caculate hamming distance is (%f)s!"  %(end-start)
    conv3Hamming.WriteHammingDistance()
    
    conv3Plot=CompressedPlotPresicionRecall.PlotPrecisionRecall('conv3',64896,8192,40)
    conv3Plot.LoadHammingDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)

#--------------------------------------------------------------------------------------------------------------------------------------    
    
    Conv3_compress=CompressFeature.CompressFeature("conv4",8192)    
    Conv3_compress.FeatureCompress()
    Conv3_compress.WriteCompressedFeature()  
    
    conv3Hamming=CompressedCalHamming.HammingDistance('conv4',64896,8192)
    conv3Hamming.LoadCompressedFeature()
    start=time.clock()
    conv3Hamming.CalHammingDistance()
    end=time.clock()
    print "Caculate hamming distance is (%f)s!"  %(end-start)
    conv3Hamming.WriteHammingDistance()
    
    conv3Plot=CompressedPlotPresicionRecall.PlotPrecisionRecall('conv4',64896,8192,40)
    conv3Plot.LoadHammingDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
    

#--------------------------------------------------------------------------------------------------------------------------------------    
    
    Conv3_compress=CompressFeature.CompressFeature("conv5",8192)    
    Conv3_compress.FeatureCompress()
    Conv3_compress.WriteCompressedFeature()  
    
    conv3Hamming=CompressedCalHamming.HammingDistance('conv5',43264,8192)
    conv3Hamming.LoadCompressedFeature()
    start=time.clock()
    conv3Hamming.CalHammingDistance()
    end=time.clock()
    print "Caculate hamming distance is (%f)s!"  %(end-start)
    conv3Hamming.WriteHammingDistance()
    
    conv3Plot=CompressedPlotPresicionRecall.PlotPrecisionRecall('conv5',43264,8192,40)
    conv3Plot.LoadHammingDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)    
    
#--------------------------------------------------------------------------------------------------------------------------------------    
    
    Conv3_compress=CompressFeature.CompressFeature("pool5",9216)    
    Conv3_compress.FeatureCompress()
    Conv3_compress.WriteCompressedFeature()  
    
    conv3Hamming=CompressedCalHamming.HammingDistance('pool5',9216,1536)
    conv3Hamming.LoadCompressedFeature()
    start=time.clock()
    conv3Hamming.CalHammingDistance()
    end=time.clock()
    print "Caculate hamming distance is (%f)s!"  %(end-start)
    conv3Hamming.WriteHammingDistance()
    
    conv3Plot=CompressedPlotPresicionRecall.PlotPrecisionRecall('pool5',9216,1536,40)
    conv3Plot.LoadHammingDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)    



#--------------------------------------------------------------------------------------------------------------------------------------    
    
    Conv3_compress=CompressFeature.CompressFeature("fc6",1536)    
    Conv3_compress.FeatureCompress()
    Conv3_compress.WriteCompressedFeature()  
    
    conv3Hamming=CompressedCalHamming.HammingDistance('fc6',4096,1536)
    conv3Hamming.LoadCompressedFeature()
    start=time.clock()
    conv3Hamming.CalHammingDistance()
    end=time.clock()
    print "Caculate hamming distance is (%f)s!"  %(end-start)
    conv3Hamming.WriteHammingDistance()
    
    conv3Plot=CompressedPlotPresicionRecall.PlotPrecisionRecall('fc6',4096,1536,40)
    conv3Plot.LoadHammingDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
    
    
    
    
#--------------------------------------------------------------------------------------------------------------------------------------    

    plt.figure(0)
    plt.title("Precision_Recall")  
    plt.xlabel("recall")
    plt.ylabel("precision")
    plt.xlim(0,100)
    plt.ylim(0,100)
    i=0
    for x in Recall:
        line,=plt.plot(Recall[i],Precision[i]) 
        lines.append(line)
        i=i+1
    plt.legend(lines,titles)    
    plt.savefig('../plot/Compressed_Precision_Recall_L='+str(conv3Plot.L)+'.eps')

    
    
    
    
    
    
    
    
    
    
    