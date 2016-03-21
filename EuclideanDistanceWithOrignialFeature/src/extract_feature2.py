#!/usr/bin/env python
# coding=utf-8
import io_numpy
import normalize

def extract_feature(name):    
    import numpy as np
    
    # Make sure that caffe is on the python path:
    caffe_root = '/home/bdd/caffe-master/'  # this file is expected to be in {caffe_root}/examples
    import sys
    sys.path.insert(0, caffe_root + 'python')
    
    import caffe

    caffe.set_device(0)
    caffe.set_mode_gpu()
    net = caffe.Net(caffe_root + 'models/scene_recongition/placesCNN_upgraded/places205CNN_deploy_upgraded2.prototxt',
                                   caffe_root + 'models/scene_recongition/placesCNN_upgraded/places205CNN_iter_300000_upgraded.caffemodel',caffe.TEST)
    
    # input preprocessing: 'data' is the name of the input blob == net.inputs[0]
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2,0,1))
    transformer.set_mean('data', np.load(caffe_root + 'models/scene_recongition/placesCNN_upgraded/places205CNN_mean.npy').mean(1).mean(1)) # mean pixel
    transformer.set_raw_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
    transformer.set_channel_swap('data', (2,1,0))  # the reference model has channels in BGR order instead of RGB
    
    
    net.blobs['data'].reshape(1,3,227,227)
    
    net.blobs['data'].data[...] = transformer.preprocess('data', caffe.io.load_image(name))
    out = net.forward()
    #print("Predicted class is #{}.".format(out['prob'][0].argmax()))
    
    
#     imagenet_labels_filename = caffe_root + 'models/scene_recongition/placesCNN_upgraded/categoryIndex_places205.csv'
#     try:
#             labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')
#     except:
#             labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')
#      
#             # sort top k predictions from softmax output
#     top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
#     print labels[top_k]
    P1 = net.blobs['pool1'].data[0]
    P1=normalize.normalize(P1)
    io_numpy.write_array(P1,'pool1')
 
    C2 = net.blobs['conv2'].data[0]
    C2=normalize.normalize(C2)
    io_numpy.write_array(C2,'conv2')
  
    P2 = net.blobs['pool2'].data[0]
    P2=normalize.normalize(P2)
    io_numpy.write_array(P2,'pool2')
  
    C3 = net.blobs['conv3'].data[0]
    C3=normalize.normalize(C3)
    io_numpy.write_array(C3,'conv3')
  
    C4 = net.blobs['conv4'].data[0]
    C4=normalize.normalize(C4)
    io_numpy.write_array(C4,'conv4')
#     return C4
  
    C5 = net.blobs['conv5'].data[0]
    C5=normalize.normalize(C5)
    io_numpy.write_array(C5,'conv5')
   
    P5 = net.blobs['pool5'].data[0]
    P5=normalize.normalize(P5)
    io_numpy.write_array(P5,'pool5')
   
    F6 = net.blobs['fc6'].data[0]
    F6=normalize.normalize(F6)
    io_numpy.write_array(F6,'fc6')
   
    F7 = net.blobs['fc7'].data[0]
    F7=normalize.normalize(F7)
    io_numpy.write_array(F7,'fc7')
   
    F8 = net.blobs['fc8'].data[0]
    F8=normalize.normalize(F8)
    io_numpy.write_array(F8,'fc8')
