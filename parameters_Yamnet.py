# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 11:20:05 2022
parameters used with the Yamnet classifier
@author: nstefana
"""
import numpy as np
#%% GLOBAL PARAMETERS
params = {'Fs0':24000 , 'Fs':16000, 'durationInSeconds' : 0.96, 'ftrSize': 0, 'hopSize':0, 'Nclasses':4} 

params['ftrSize'] = int(params['durationInSeconds']*params['Fs'])   
params['hopSize']=int(params['Fs']*0.3)

# modelPath = '../models/retyam_4classes_15Nov.hdf5'
modelPath = '../models/retyam_4classes_22Nov.hdf5'
# modelPath = '../models/retyam.hdf5'

classificationMatrix = np.array([[0, 0, 0, 0], [0, 1, 3, 1], [0, 3, 2, 2], [0, 1, 2, 3]])
# classificationMatrix = np.array([[0, 1, 2, 3], [1, 1, 3, 1], [2, 3, 2, 2], [3, 1, 2, 3]]) #less strict