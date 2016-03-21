#!/usr/bin/env python
# coding=utf-8


import matplotlib.pylab as plt
import numpy as np    
import scipy.io as sio  


def result(D_array,layer_name):    
    
    D_len=len(D_array)

    TP=np.zeros(D_len)
    FP=np.zeros(D_len)
    FN=np.zeros(D_len)
    TN=np.zeros(D_len)
    Precison=np.zeros(D_len)
    Recall=np.zeros(D_len)

    
    matfn="/home/bdd/Desktop/src_code2/CityCentreGroundTruth.mat"
    data=sio.loadmat(matfn)  
    groudtruth=data['truth']
    groudtruth=np.array(groudtruth)
    print groudtruth
    f = file("DIS"+layer_name+".npy", "a+b")
    DIS=np.load(f)
    H=DIS.shape
    dim=H[0]
     
    
    
    
    
    
    D_index=0
    for D in D_array:
#         print D_index
        correspondence=np.zeros(H)
        j=11
        while j<dim:
            temp=DIS[j][0:j-10].argsort()
            if DIS[j][temp[0]]<D:
                correspondence[j][temp[0]]=1
            j=j+1
            
        corre_ground=correspondence*groudtruth
        i=0
        while i<dim:
            
            if corre_ground[i].sum()>0:
                TP[D_index]=TP[D_index]+1
                
                
            else:
                if correspondence[i].sum()>0:
                    FP[D_index]=FP[D_index]+1
                else:
                    if groudtruth[i].sum()>0:
                        FN[D_index]=FN[D_index]+1
                    else:
                        TN[D_index]=TN[D_index]+1
                           
                        
                        
            
#             else: 
#                 if groudtruth[i].sum()>0:
#                     FN[D_index]=FN[D_index]+1
#                 else:
#                     if correspondence[i].sum()>0:
#                         FP[D_index]=FP[D_index]+1
#                     else:
#                         TN[D_index]=TN[D_index]+1
                        
                                    
            i=i+1
        if TP[D_index]==0:
            Precison[D_index]=0
            Recall[D_index]=0
        else:   
            Precison[D_index]=float(TP[D_index])/(TP[D_index]+FP[D_index])*100
            Recall[D_index]=float(TP[D_index])/(TP[D_index]+FN[D_index])*100
        D_index=D_index+1
        
      
      
      
      
      
    plt.title(layer_name)  
    plt.plot(Recall,Precison) 
    plt.savefig('/home/bdd/recall_precision'+layer_name+'.png', dpi=120)
    plt.show()


