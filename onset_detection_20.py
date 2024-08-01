# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:58:31 2019

@author: nstefana
"""
import numpy as np
from scipy.signal import find_peaks

def onset_detection(aux,sampleIdxs,frameEn,detectParams):
  

    sJump=detectParams['hopSize']
    onsetDistance=np.ceil(detectParams['minOnsetDiff']*detectParams['Fs']/sJump)
    N=np.shape(aux)[0]
    
    aux[frameEn<detectParams['energyThreshold']]=0
    peaks, _ = find_peaks(aux, height=(detectParams['threshold'],None), distance=onsetDistance)
    onsetSamples=sampleIdxs[peaks]
    onsetEnergy=frameEn[peaks]
    
    return onsetSamples.astype(int), peaks, onsetEnergy 
