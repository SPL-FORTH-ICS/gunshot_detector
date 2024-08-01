# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:58:31 2019
child of onset reduction cough, 
calculates without overlap
@author: nstefana
"""
import numpy as np

def onset_reduction(s,params):

    hopSize=params['hopSize']
    Ns=np.shape(s)[0]
    NsFrame=int(np.round(params['frameDuration']*params['Fs']))
    NsFrame =int(np.round(NsFrame/2))*2 # Enforce evenness of the frame's length
    frameDur = int(NsFrame)
    ffAll=np.arange(0,NsFrame,1,dtype=float)*params['Fs']/NsFrame
    lowFreqIdx=np.argmin(np.abs(ffAll-params['freqLimits'][0]))
    highFreqIdx=np.argmin(np.abs(ffAll-params['freqLimits'][1]))
    ffUse=np.arange(lowFreqIdx,highFreqIdx)
    
    hanwin=np.hanning(NsFrame)
    sampleIdxs=np.arange(frameDur,Ns-frameDur,hopSize,dtype=int)  
    N = len(sampleIdxs)
    frameOutput=np.zeros(N,dtype=float)
    frameEn=np.zeros(N,dtype=float)
    for n in range(0,N):
        frameIN = hanwin*s[sampleIdxs[n]:sampleIdxs[n]+frameDur]#-1]
#        frameIN=np.multiply(frameIN,hanwin)
        framePRE= hanwin*s[sampleIdxs[n]-frameDur:sampleIdxs[n]]
        fftIN=np.fft.fft(frameIN,n=NsFrame,axis=0)
        fftPRE=np.fft.fft(framePRE,n=NsFrame,axis=0)
        tmpIN = np.abs(fftIN)
        tmpPRE= np.abs(fftPRE)
        freqResponse=tmpIN[lowFreqIdx:highFreqIdx]
        previousFreqResponse=tmpPRE[lowFreqIdx:highFreqIdx]
        frameEn[n]=np.sum(freqResponse)
            
        freqEnergyRatio=np.log2(np.divide(freqResponse,previousFreqResponse))
        binaryRatio=(freqEnergyRatio>params['percTresh'])
        

        frameOutput[n]=np.sum(binaryRatio)
    ## Create window matrix and apply to frames
    return frameOutput, sampleIdxs, frameEn
    