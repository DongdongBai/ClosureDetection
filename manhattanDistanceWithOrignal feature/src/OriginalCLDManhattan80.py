#!/usr/bin/env python
# coding=utf-8
import time
import matplotlib.pylab as plt
import OriginalCalManhattan
import OriginalPlotPresicionRecall




if __name__=='__main__':
    
    Start=time.clock()
    Recall=[]
    Precision=[]
    titles=[]
    lines=[]
    
    
    



#--------------------------------------------------------------------------------------------------------------------------------------    
    
    
#     conv3Hamming=OriginalCalManhattan.ManhattanDistance('CityCenter','pool1')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalManhattanDistance()
#     end=time.clock()
#     print "Caculate manhattan distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteManhattanDistance()
 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','pool1',69984,80)
    conv3Plot.LoadManhattanDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)   
        
    
#--------------------------------------------------------------------------------------------------------------------------------------    
    
    
#     conv3Hamming=OriginalCalManhattan.ManhattanDistance('CityCenter','conv2')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalManhattanDistance()
#     end=time.clock()
#     print "Caculate manhattan distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteManhattanDistance()
 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','conv2',186624,80)
    conv3Plot.LoadManhattanDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)   
    
    
    
    
    
#--------------------------------------------------------------------------------------------------------------------------------------    
    
    
#     conv3Hamming=OriginalCalManhattan.ManhattanDistance('CityCenter','pool2')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalManhattanDistance()
#     end=time.clock()
#     print "Caculate manhattan distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteManhattanDistance()
 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','pool2',43264,80)
    conv3Plot.LoadManhattanDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
    
#--------------------------------------------------------------------------------------------------------------------------------------    
    
    
#     conv3Hamming=OriginalCalManhattan.ManhattanDistance('CityCenter','conv3')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalManhattanDistance()
#     end=time.clock()
#     print "Caculate manhattan distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteManhattanDistance()
# 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','conv3',64896,80)
    conv3Plot.LoadManhattanDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
 
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
#     
#     
#     conv3Hamming=OriginalCalManhattan.ManhattanDistance('CityCenter','conv4')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalManhattanDistance()
#     end=time.clock()
#     print "Caculate manhattan distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteManhattanDistance()
# 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','conv4',64896,80)
    conv3Plot.LoadManhattanDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
 
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
#     
#     
#     conv3Hamming=OriginalCalManhattan.ManhattanDistance('CityCenter','conv5')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalManhattanDistance()
#     end=time.clock()
#     print "Caculate manhattan distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteManhattanDistance()
 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','conv5',43264,80)
    conv3Plot.LoadManhattanDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
# 
#  
#     conv3Hamming=OriginalCalManhattan.ManhattanDistance('CityCenter','pool5')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalManhattanDistance()
#     end=time.clock()
#     print "Caculate manhattan distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteManhattanDistance()
 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','pool5',9216,80)
    conv3Plot.LoadManhattanDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
     
#     
# #--------------------------------------------------------------------------------------------------------------------------------------    
# 
#      
#     conv3Hamming=OriginalCalManhattan.ManhattanDistance('CityCenter','fc6')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalManhattanDistance()
#     end=time.clock()
#     print "Caculate manhattan distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteManhattanDistance()
     
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','fc6',4096,80)
    conv3Plot.LoadManhattanDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
# 
  
#     conv3Hamming=OriginalCalManhattan.ManhattanDistance('CityCenter','fc7')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalManhattanDistance()
#     end=time.clock()
#     print "Caculate manhattan distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteManhattanDistance()
#     
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','fc7',4096,80)
    conv3Plot.LoadManhattanDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
# 
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
# 
  
#     conv3Hamming=OriginalCalManhattan.ManhattanDistance('CityCenter','fc8')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalManhattanDistance()
#     end=time.clock()
#     print "Caculate manhattan distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteManhattanDistance()
    
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('CityCenter','fc8',205,80)
    conv3Plot.LoadManhattanDistance()
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
