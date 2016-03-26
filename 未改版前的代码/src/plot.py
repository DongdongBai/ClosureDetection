#!/usr/bin/env python
# coding=utf-8
import result
import numpy as np

D_array=np.linspace(0.344344049692,1.35239160061,500)
result.result(D_array,"pool1")
 
D_array=np.linspace(0.374729394913,1.34376788139,500)
result.result(D_array,"conv2")
 
D_array=np.linspace(0.301110446453,1.29882144928,500)
result.result(D_array,"pool2")
 
D_array=np.linspace(0.311531066895,1.29718482494,500)
result.result(D_array,"conv3")
 
D_array=np.linspace(0.301401376724,1.32344532013,500)
result.result(D_array,"conv4")
 
D_array=np.linspace(0.353400379419,1.40551733971,500)
result.result(D_array,"conv5")
 
D_array=np.linspace(0.300964653492,1.38409125805,500)
result.result(D_array,"pool5")
 
D_array=np.linspace(0.274265795946,1.40312755108,500)
result.result(D_array,"fc6")
 
D_array=np.linspace(0.172954037786,1.38578188419,500)
result.result(D_array,"fc7")
 
D_array=np.linspace(0.0751659572124,1.82714474201,500)
result.result(D_array,"fc8")
