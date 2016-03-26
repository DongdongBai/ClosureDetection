#!/usr/bin/env python
# coding=utf-8
import time
import matplotlib.pylab as plt
import OriginalCalCosine
import OriginalPlotPresicionRecall




if __name__=='__main__':
    
    Start=time.clock()
    Recall=[]
    Precision=[]
    titles=[]
    lines=[]
    
    
    



#--------------------------------------------------------------------------------------------------------------------------------------    
    
    
#     conv3Hamming=OriginalCalCosine.CosineDistance('CityCenter','pool1')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalCosineDistance()
#     end=time.clock()
#     print "Caculate Cosine distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteCosineDistance()
#   
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','pool1',69984,40)
    conv3Plot.LoadCosineDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)   
#          
    
#--------------------------------------------------------------------------------------------------------------------------------------    
    
    
#     conv3Hamming=OriginalCalCosine.CosineDistance('CityCenter','conv2')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalCosineDistance()
#     end=time.clock()
#     print "Caculate Cosine distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteCosineDistance()
 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','conv2',186624,40)
    conv3Plot.LoadCosineDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)   
    
    
    
    
    
#--------------------------------------------------------------------------------------------------------------------------------------    
    
    
#     conv3Hamming=OriginalCalCosine.CosineDistance('CityCenter','pool2')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalCosineDistance()
#     end=time.clock()
#     print "Caculate Cosine distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteCosineDistance()
 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','pool2',43264,40)
    conv3Plot.LoadCosineDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
    
#--------------------------------------------------------------------------------------------------------------------------------------    
    
    
#     conv3Hamming=OriginalCalCosine.CosineDistance('CityCenter','conv3')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalCosineDistance()
#     end=time.clock()
#     print "Caculate Cosine distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteCosineDistance()
 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','conv3',64896,40)
    conv3Plot.LoadCosineDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
 
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
#     
#     
#     conv3Hamming=OriginalCalCosine.CosineDistance('CityCenter','conv4')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalCosineDistance()
#     end=time.clock()
#     print "Caculate Cosine distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteCosineDistance()
 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','conv4',64896,40)
    conv3Plot.LoadCosineDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
# 
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
#     
#     
#     conv3Hamming=OriginalCalCosine.CosineDistance('CityCenter','conv5')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalCosineDistance()
#     end=time.clock()
#     print "Caculate Cosine distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteCosineDistance()
 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','conv5',43264,40)
    conv3Plot.LoadCosineDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
# 
 
#     conv3Hamming=OriginalCalCosine.CosineDistance('CityCenter','pool5')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalCosineDistance()
#     end=time.clock()
#     print "Caculate Cosine distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteCosineDistance()
 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','pool5',9216,40)
    conv3Plot.LoadCosineDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
     
#     
# #--------------------------------------------------------------------------------------------------------------------------------------    
# 
#      
#     conv3Hamming=OriginalCalCosine.CosineDistance('CityCenter','fc6')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalCosineDistance()
#     end=time.clock()
#     print "Caculate Cosine distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteCosineDistance()
     
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','fc6',4096,40)
    conv3Plot.LoadCosineDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
# 
  
#     conv3Hamming=OriginalCalCosine.CosineDistance('CityCenter','fc7')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalCosineDistance()
#     end=time.clock()
#     print "Caculate Cosine distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteCosineDistance()
     
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','fc7',4096,40)
    conv3Plot.LoadCosineDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
# 
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
# 
  
#     conv3Hamming=OriginalCalCosine.CosineDistance('CityCenter','fc8')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalCosineDistance()
#     end=time.clock()
#     print "Caculate Cosine distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteCosineDistance()
    
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','fc8',205,40)
    conv3Plot.LoadCosineDistance()
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
    plt.legend(lines,titles,loc='lower left')    
    plt.savefig('../plot/'+conv3Plot.dataset+'Orignal_Precision_Recall_L='+str(conv3Plot.L)+'.eps')
    
    End=time.clock()
    print "The TOTAL TIME is (%f)s!"  %(End-Start)
