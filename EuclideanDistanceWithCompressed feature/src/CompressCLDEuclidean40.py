#!/usr/bin/env python
# coding=utf-8
import time
import matplotlib.pylab as plt
import CompressFeature
import CompressedCalEuclidean
import CompressedPlotPresicionRecall


if __name__=='__main__':
    
    Start=time.clock()
    
    Recall=[]
    Precision=[]
    titles=[]
    lines=[]

#--------------------------------------------------------------------------------------------------------------------------------------    
    
#     Conv3_compress=CompressFeature.CompressFeature("CityCenter","conv3",8192)    
#     Conv3_compress.FeatureCompress()
#     Conv3_compress.WriteCompressedFeature()  
#     
#     conv3Hamming=CompressedCalEuclidean.EuclideanDistance("CityCenter",'conv3',64896,8192)
#     conv3Hamming.LoadCompressedFeature()
#     start=time.clock()
#     conv3Hamming.CalEuclideanDistance()
#     end=time.clock()
#     print "Caculate Euclidean distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteEuclideanDistance()
#     
#     conv3Plot=CompressedPlotPresicionRecall.PlotPrecisionRecall("CityCenter",'conv3',64896,8192,40)
#     conv3Plot.LoadEuclideanDistance()
#     conv3Plot.FindMaxAndMinDistance()
#     conv3Plot.PlotPrecisionRecall()
#     Recall.append(conv3Plot.recall)
#     Precision.append(conv3Plot.precision)
#     titles.append(conv3Plot.layerName)

#--------------------------------------------------------------------------------------------------------------------------------------    
#     
#     Conv3_compress=CompressFeature.CompressFeature("CityCenter","conv4",8192)    
#     Conv3_compress.FeatureCompress()
#     Conv3_compress.WriteCompressedFeature()  
#     
#     conv3Hamming=CompressedCalEuclidean.EuclideanDistance("CityCenter",'conv4',64896,8192)
#     conv3Hamming.LoadCompressedFeature()
#     start=time.clock()
#     conv3Hamming.CalEuclideanDistance()
#     end=time.clock()
#     print "Caculate Euclidean distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteEuclideanDistance()
    
#     conv3Plot=CompressedPlotPresicionRecall.PlotPrecisionRecall("CityCenter",'conv4',64896,8192,40)
#     conv3Plot.LoadEuclideanDistance()
#     conv3Plot.FindMaxAndMinDistance()
#     conv3Plot.PlotPrecisionRecall()
#     Recall.append(conv3Plot.recall)
#     Precision.append(conv3Plot.precision)
#     titles.append(conv3Plot.layerName)
    

#--------------------------------------------------------------------------------------------------------------------------------------    
    
#     Conv3_compress=CompressFeature.CompressFeature("CityCenter","conv5",5120)    
#     Conv3_compress.FeatureCompress()
#     Conv3_compress.WriteCompressedFeature()  
#     
#     conv3Hamming=CompressedCalEuclidean.EuclideanDistance("CityCenter",'conv5',43264,5120)
#     conv3Hamming.LoadCompressedFeature()
#     start=time.clock()
#     conv3Hamming.CalEuclideanDistance()
#     end=time.clock()
#     print "Caculate Euclidean distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteEuclideanDistance()
    
#     conv3Plot=CompressedPlotPresicionRecall.PlotPrecisionRecall("CityCenter",'conv5',43264,5120,40)
#     conv3Plot.LoadEuclideanDistance()
#     conv3Plot.FindMaxAndMinDistance()
#     conv3Plot.PlotPrecisionRecall()
#     Recall.append(conv3Plot.recall)
#     Precision.append(conv3Plot.precision)
#     titles.append(conv3Plot.layerName)    
    
#--------------------------------------------------------------------------------------------------------------------------------------    
#     
    Conv3_compress=CompressFeature.CompressFeature("CityCenter","pool5",2560)    
    Conv3_compress.FeatureCompress()
    Conv3_compress.WriteCompressedFeature()  
     
    conv3Hamming=CompressedCalEuclidean.EuclideanDistance("CityCenter",'pool5',9216,2560)
    conv3Hamming.LoadCompressedFeature()
    start=time.clock()
    conv3Hamming.CalEuclideanDistance()
    end=time.clock()
    print "Caculate Euclidean distance is (%f)s!"  %(end-start)
    conv3Hamming.WriteEuclideanDistance()
    
    conv3Plot=CompressedPlotPresicionRecall.PlotPrecisionRecall("CityCenter",'pool5',9216,2560,40)
    conv3Plot.LoadEuclideanDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)    



#--------------------------------------------------------------------------------------------------------------------------------------    
    
#     Conv3_compress=CompressFeature.CompressFeature("CityCenter","fc6",1536)    
#     Conv3_compress.FeatureCompress()
#     Conv3_compress.WriteCompressedFeature()  
#     
#     conv3Hamming=CompressedCalEuclidean.EuclideanDistance("CityCenter",'fc6',4096,1536)
#     conv3Hamming.LoadCompressedFeature()
#     start=time.clock()
#     conv3Hamming.CalEuclideanDistance()
#     end=time.clock()
#     print "Caculate Euclidean distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteEuclideanDistance()
    
#     conv3Plot=CompressedPlotPresicionRecall.PlotPrecisionRecall("CityCenter",'fc6',4096,1536,40)
#     conv3Plot.LoadEuclideanDistance()
#     conv3Plot.FindMaxAndMinDistance()
#     conv3Plot.PlotPrecisionRecall()
#     Recall.append(conv3Plot.recall)
#     Precision.append(conv3Plot.precision)
#     titles.append(conv3Plot.layerName)
    
    
    
    
    
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
    plt.legend(lines,titles,loc='lower left')    
    plt.savefig('../plot/'+conv3Plot.dataset+'Compressed_Precision_Recall_L='+str(conv3Plot.L)+'.eps')

    End=time.clock()
    print "The TOTAL TIME is (%f)s!"  %(End-Start)
    
    
    
    
    
    
    
    
    
    
    