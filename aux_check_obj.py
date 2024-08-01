# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 12:42:44 2023

@author: user
"""
import pickle
import os
import glob
import numpy as np
import librosa
import sounddevice as sd

#%%
# name2load = 'F:/WCS/data/2020-2021/temp/detections/SWIFT4_20200730_143334_start_01200.obj'

# with open(name2load,'rb') as fid:
#     dataIN = pickle.load(fid,encoding='latin1')  
    
# detectionsList = dataIN['detectionsList']

#%%
probThreshold = 0.5
ftrParams={'Fs':8000, 'samplesBefore':3600, 'samplesAfter':12000, 'ftrSize':0, 'duration':0.975, 'Nclasses': 2, 'batchSize4inference':32}
ftrParams['ftrSize'] = ftrParams['samplesBefore'] + ftrParams['samplesAfter']

#%% 

segments2listen = np.zeros((0,))
ftrMtx = np.zeros((0,ftrParams['ftrSize']),dtype=float)
labels=[]
Npos = 0
# objFilesPath = 'F:/WCS/data/2020-2021/sensor_5/detections/'
objFilesPath = 'F:/WCS/data/Evros_raw/run/detections/'
folder_with_obj=(objFilesPath + '/*.obj')
for name2load in glob.glob(folder_with_obj):
    with open(name2load,'rb') as fid:
        dataIN = pickle.load(fid,encoding='latin1')  
    sig0, sr = librosa.load(dataIN['Nw'], sr=ftrParams['Fs'])
    Ns=len(sig0)
    dcOffset = np.mean(sig0)
    sig = sig0-dcOffset
    detectionsList = dataIN['detectionsList']            
    Npos += np.sum(detectionsList[:,1]>probThreshold)
    positiveIdxs = np.argwhere(detectionsList[:,1]>probThreshold)
    sampleStart = detectionsList[positiveIdxs,0].astype(int).flatten()
    for s in sampleStart:
        segm = sig[s:s+int(ftrParams['ftrSize'])]
        segm=10*segm/np.linalg.norm(segm)
        ftrMtx = np.append(ftrMtx,segm.reshape((1,ftrParams['ftrSize'])), axis=0)
        segments2listen = np.append(segments2listen, segm)
        labels.append('neg')
        
print(Npos)

#%%
path2saveFtrs='F:/WCS/segments/temp/renameME.obj'
if True:
    with open(os.path.join(path2saveFtrs) , 'wb') as fid:            
        pickle.dump({'X' : ftrMtx,'Y': labels}, fid) 
        
#%%
if False:
    sd.play(segments2listen,ftrParams['Fs'])        