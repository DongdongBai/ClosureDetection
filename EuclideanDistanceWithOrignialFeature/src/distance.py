#!/usr/bin/env python
# coding=utf-8
import numpy as np


def distance(A,B):
    C=(A-B)**2
    S=np.sqrt(C.sum())
    return S

