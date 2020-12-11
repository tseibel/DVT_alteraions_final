from __future__ import division
from PIL import Image
from os import listdir
from os.path import isfile, join
from numpy.lib.stride_tricks import as_strided
from heapq import nlargest

import SPM_DVT as sd
import itertools
import csv
import numpy as np
import data_pull as dp



def run_SPM(filter,full_dir):
    #directory
    dir = '/home/tseibel/deep-visualization-toolbox/data_pull/auto'

    #imported 2D arrays

    with open('Array_1.txt') as a:
        thresh_val = a.readline()
    name_1 = thresh_val

    with open('Array_2.txt') as a:
        thresh_val = a.readline()
    name_2 = thresh_val

    #array augmentation
    array_1 = sd.resize_array(dp.open(dir + '/' + filter + '/' + name_1,'')[:,:,:,0])
    array_2 = sd.resize_array(dp.open(dir + '/' + filter + '/' + name_2,'')[:,:,:,0])
    #degree
    degree = sd.degree(array_1)


    answers_dict, diff_dict = sd.pyr_all(array_1, array_2, degree)

    final_dict = {}
    for key in answers_dict:
        if answers_dict[key] > [0]:
            final_dict[key] = answers_dict[key]

 
    res, avg_filter = dp.k_largest(20, final_dict,'y')

    return avg_filter
