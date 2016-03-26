#!/usr/bin/env python
# coding=utf-8 

import caffe
import os
import sys

import matplotlib.pyplot as plt
import numpy as np


# Make sure that caffe is on the python path:
caffe_root = '/home/bdd/caffe-master/'  # this file is expected to be in {caffe_root}/examples
sys.path.insert(0, caffe_root + 'python')



if not os.path.isfile(caffe_root + 'models/scene_recongition/placesCNN_upgraded/places205CNN_iter_300000_upgraded.caffemodel'):
    print("Downloading pre-trained CaffeNet model...")

caffe.set_mode_cpu()
net = caffe.Net(caffe_root + 'models/scene_recongition/placesCNN_upgraded/places205CNN_deploy_upgraded.prototxt',
                               caffe_root + 'models/scene_recongition/placesCNN_upgraded/places205CNN_iter_300000_upgraded.caffemodel',caffe.TEST)

# input preprocessing: 'data' is the name of the input blob == net.inputs[0]
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
transformer.set_mean('data', np.load(caffe_root + 'models/scene_recongition/placesCNN_upgraded/places205CNN_mean.npy').mean(1).mean(1)) # mean pixel
transformer.set_raw_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
transformer.set_channel_swap('data', (2,1,0))  # the reference model has channels in BGR order instead of RGB


net.blobs['data'].reshape(10,3,227,227)

net.blobs['data'].data[...] = transformer.preprocess('data', caffe.io.load_image(caffe_root + 'examples/images/20.jpg'))
out = net.forward()
print("Predicted class is #{}.".format(out['prob'][0].argmax()))


imagenet_labels_filename = caffe_root + 'models/scene_recongition/placesCNN_upgraded/categoryIndex_places205.csv'
try:
        labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')
except:
        labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')

        # sort top k predictions from softmax output
top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
print labels[top_k]


