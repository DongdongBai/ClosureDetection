import numpy as np
def normalize(feat):
#     sh=feat.shape
#     i=0
#     while i<sh[0]:
    temp=feat**2
    S=np.sqrt(temp.sum())
    test=0
    if S==0:
        feat=np.zeros(feat.shape)
        print test
    else:
        feat=feat/S
        test=(feat**2).sum()
        print test
    return feat
#     i=i+1

        
        
    