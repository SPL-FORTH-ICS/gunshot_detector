# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:08:14 2020
consistent to ICASSP paper (chainsaw20)
@author: Nikolaos Stefanakis
"""
import pickle
import os
import librosa
import numpy as np
import tensorflow as tf
from trainable_yamnet import get_retrained_yamnet
from onset_reduction_20 import onset_reduction
from onset_detection_20 import onset_detection

#%%
def bp_process_segment(wavNames,outputFilePath,allAccumulativeDurations,timeBorders,partitionIdx,modelFilePath, threshold):    

    ftrParams={'Fs':8000, 'samplesBefore':3600, 'samplesAfter':12000, 'ftrSize':0, 'duration':0.975, 'Nclasses': 2, 'batchSize4inference':32}
    ftrParams['ftrSize'] = ftrParams['samplesBefore'] + ftrParams['samplesAfter']
    
    detectionParams={'Fs':ftrParams['Fs'], 'hopSize':160, 'freqLimits':(120, 3200), 'minOnsetDiff':0.1, 
                  'frameDuration':0.04, 'threshold':26, 'percTresh':1.5, 'energyThreshold':0.01}
    

#%%    
    partitionIdx, Npartitions = partitionIdx  
    tStart=timeBorders[partitionIdx][0]
    fullwavName=wavNames[partitionIdx].split(os.sep)[-1]
    recName=fullwavName.split('.wav')[0]
    name2save=(outputFilePath + '/detections/' + recName + '_start_' + format(int(tStart),'05d') + '.obj')
    partitionOffsetInSamples = int(detectionParams['Fs']*tStart)
#%%
    if os.path.exists(name2save) == False:
        run_segment=True
    else:
        with open(name2save,'rb') as fid:
            dataIN = pickle.load(fid,encoding='latin1')  
        if dataIN['onsetThreshold']==detectionParams['threshold']:
            run_segment=False
            print('Detections for file ' + name2save + ' already extracted, will not re-calculate them')
        else:
            run_segment=True    
            print('Detections for file ' + name2save + ' already extracted, but will overwritten due to onset threshold change')
#%%        
    if run_segment:    
        
        detectionsList=np.zeros((0,2),dtype=float)        
        graph = tf.Graph()
        with graph.as_default():
            model = get_retrained_yamnet(modelFilePath, input_duration = ftrParams['duration'], num_classes = ftrParams['Nclasses'])        
        
            localFtrMtx = np.zeros((ftrParams['batchSize4inference'],ftrParams['ftrSize']),dtype=float)
            partitionDur=timeBorders[partitionIdx][1]-timeBorders[partitionIdx][0]
            
            print(f'running now partition {partitionIdx+1} of {Npartitions} associated to {recName}.')
            sig0, sr = librosa.load(wavNames[partitionIdx], sr=ftrParams['Fs'], offset=tStart,duration=partitionDur)
            Ns=len(sig0)
            dcOffset = np.mean(sig0)
            aux,sampleIdxs,frameEn = onset_reduction(sig0,detectionParams)
            onsetSamples,onsetPoints,onsetEnergy = onset_detection(aux,sampleIdxs,frameEn,detectionParams)
            classProbs = np.zeros((0,2))
            segmentStartInSamples = np.zeros((0,))
            batchIdx = 0
            Nonsets = 0
            for o in onsetSamples:
                if  Ns-o>ftrParams['samplesAfter'] and o-ftrParams['samplesBefore']>0:
                    sig=sig0[o-ftrParams['samplesBefore']:o+ftrParams['samplesAfter']]
                    sig=sig-dcOffset
                    sig=10*sig/np.linalg.norm(sig) 
                    segmentStartInSamples = np.append(segmentStartInSamples,[o-ftrParams['samplesBefore']+partitionOffsetInSamples], axis=0)
                    Nonsets+=1
    
                    if batchIdx != ftrParams['batchSize4inference']:
                        localFtrMtx[batchIdx,:]=sig.reshape((1,ftrParams['ftrSize']))              
                        batchIdx+=1
                    else:
                        classProbs= np.append(classProbs, model.predict(localFtrMtx),axis=0)
                        localFtrMtx[0,:]=sig.reshape((1,ftrParams['ftrSize']))              
                        batchIdx=1
                        
            NeventsLeft = Nonsets - np.shape(classProbs)[0]
            if NeventsLeft > 0:
                classProbs= np.append(classProbs,model.predict(localFtrMtx[:NeventsLeft,:]),axis=0)
                
            detectionsList = np.array([segmentStartInSamples, classProbs[:,1]])
            Ndetections = np.shape(detectionsList)[1]                
            
            with open(name2save , 'wb') as fid:        
                pickle.dump({ 'detectionsList':detectionsList.T,'Nw': wavNames[partitionIdx],
                             'Nr':recName,'Ndetections':Ndetections,'accumulativeDuration':allAccumulativeDurations[partitionIdx],
                             'onsetThreshold':detectionParams['threshold'],'dcOffset':dcOffset,
                             'timeBordersInSeconds': [timeBorders[partitionIdx],timeBorders[partitionIdx+1]]}, fid) #, 'probs':sawProbs