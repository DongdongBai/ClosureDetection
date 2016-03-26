#!/usr/bin/env python
# coding=utf-8

import numpy as np


def write_array(array,layer_name):
    array.shape=-1
    f = file(layer_name+".npy", "a+b")
    np.save(f, array)
    f.close()

