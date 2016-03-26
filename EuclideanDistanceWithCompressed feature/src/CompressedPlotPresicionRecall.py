#!/usr/bin/env python
# coding=utf-8

import numpy as np
import matplotlib.pylab as plt
import scipy.io as sio  


class PlotPrecisionRecall(object):
    def __init__(self,dataset,layerName,orignalDim,CompressedDim,L):
        self.dataset=dataset
        self.layerName=layerName
        self.orignalDim=orignalDim
        self.CompressedDim=CompressedDim
        self.L=L
    def LoadEuclideanDistance(self):
        self.Distance=np.loadtxt("../data/"+self.dataset+"compressed_EuclideanDistance_"+self.layerName+"_"+str(self.orignalDim)+" to "+str(self.CompressedDim)+".txt",dtype='int') 
#         f = file("EuclideanDistance_"+self.layerName+".npy", "a+b")
#         self.Distance=np.load(f)
#         f.close()
        print "Load Euclidean distance of (%s) is OK!" %self.layerName
    def FindMaxAndMinDistance(self):
        DistanceCopy = self.Distance.copy()  
        self.MaxDistance=DistanceCopy.max()
        print "max distance is (%d)"  %self.MaxDistance
        Index=DistanceCopy<0
        DistanceCopy[Index]=1000000
        self.MinDistance=DistanceCopy.min()
        print "min distance is (%d)"  %self.MinDistance

    def PlotPrecisionRecall(self):
        matfn="/home/bdd/Desktop/ClosureDetectionProject/"+self.dataset+"Feature/CityCentreGroundTruth.mat"
        data=sio.loadmat(matfn)  
        groudtruth=data['truth']
        groudtruth=np.array(groudtruth)
    
        threshold=np.arange(self.MinDistance,self.MaxDistance,10)
    
        samplePointNum=len(threshold)

        TP=np.zeros(samplePointNum)
        FP=np.zeros(samplePointNum)
        FN=np.zeros(samplePointNum)
        TN=np.zeros(samplePointNum)
        Precison=np.zeros(samplePointNum)
        Recall=np.zeros(samplePointNum)

    
#     matfn="/home/bdd/Desktop/src_code2/CityCentreGroundTruth.mat"
#     data=sio.loadmat(matfn)  
#     groudtruth=data['truth']
#     groudtruth=np.array(groudtruth)
#     print groudtruth

        dim=self.Distance.shape[0]
        samplePointIndex=0
        erroTPIndex=0
        for D in threshold:
#             print samplePointIndex
            correspondence=np.zeros(self.Distance.shape)
            j=self.L+1
            while j<dim:
                temp=self.Distance[j][0:j-self.L].argsort()
                if self.Distance[j][temp[0]]<=D:
                    correspondence[j][temp[0]]=1
                j=j+1
            
            corre_ground=correspondence*groudtruth
            i=0
            while i<dim:
            
                if corre_ground[i].sum()>0:
                    TP[samplePointIndex]=TP[samplePointIndex]+1
                
                
                else:
                    if correspondence[i].sum()>0:
                        FP[samplePointIndex]=FP[samplePointIndex]+1
                    else:
                        if groudtruth[i].sum()>0:
                            FN[samplePointIndex]=FN[samplePointIndex]+1
                        else:
                            TN[samplePointIndex]=TN[samplePointIndex]+1         
                i=i+1
            if TP[samplePointIndex]==0:
                Precison[samplePointIndex]=0
                Recall[samplePointIndex]=0
                erroTPIndex=erroTPIndex+1
            else:   
                Precison[samplePointIndex]=float(TP[samplePointIndex])/(TP[samplePointIndex]+FP[samplePointIndex])*100
                Recall[samplePointIndex]=float(TP[samplePointIndex])/(TP[samplePointIndex]+FN[samplePointIndex])*100
            samplePointIndex=samplePointIndex+1
        
        
        
        self.precision=Precison[erroTPIndex:]
        self.recall=Recall[erroTPIndex:]        
        PrecisonRecall=np.vstack((Precison,Recall))
        PrecisonRecall=PrecisonRecall.T
        np.savetxt("../data/"+self.dataset+"compressed_precison_recall"+self.layerName+"_"+str(self.orignalDim)+" to "+str(self.CompressedDim)+"L="+str(self.L)+".txt", PrecisonRecall, fmt="%d") #改为保存为整数
        
        plt.figure(0)
        plt.title(self.layerName+"_compress"+str(self.orignalDim)+" to "+str(self.CompressedDim))  
        plt.xlabel("recall")
        plt.ylabel("precision")
        plt.xlim(0,100)
        plt.ylim(0,100)
        plt.plot(Recall[erroTPIndex:],Precison[erroTPIndex:]) 
        plt.savefig('../plot/'+self.dataset+'Compressed_Precision_Recall_'+self.layerName+"_"+str(self.orignalDim)+" to "+str(self.CompressedDim)+"L="+str(self.L)+'.png', dpi=240)
#         plt.show()
        plt.close()
# conv3Plot=PlotPrecisionRecall('CityCenter','pool5',9216,1024,40)
# conv3Plot.LoadEuclideanDistance()
# conv3Plot.FindMaxAndMinDistance()
# conv3Plot.PlotPrecisionRecall()       
         
        
        
