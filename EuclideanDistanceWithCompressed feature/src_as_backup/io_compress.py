#!/usr/bin/env python
# coding=utf-8
import numpy as np


def write_array(array,layer_name):
    f = file("Compressed"+layer_name+".npy", "a+b")
    np.save(f, array)
    f.close()
