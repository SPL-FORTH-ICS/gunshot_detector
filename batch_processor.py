# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:00:41 2020

@author: Nikolaos Stefanakis
"""
import argparse
import os
import numpy as np
import librosa
import glob
import pandas as pd
import datetime
import multiprocessing

from bp_process_segment import bp_process_segment as process_segment
from detections_report import detections_report 


import warnings
warnings.filterwarnings("ignore")
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def main():
        
    parser = argparse.ArgumentParser(description='batch_processor', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('pathIN', help='folder containing audio data')    
    parser.add_argument('-p', '--nopREQ', type=int, help='number of processing units employed')    
    parser.add_argument('-t', '--probThresh', type=float, help='Classification threshold, default=0.5') 
    parser.add_argument('-o', '--pathOUT', type=str, help='folder for the results to be saved, default={input path}/results') 
    parser.add_argument('-ext_audio', '--extract_wavs', action='store_true', help='Use this argument to extract audio segments for each detection.')     
    parser.add_argument('-sep_results', '--export_separated_dfs', action='store_true', help='Use this argument to export separated analysis files for each input .wav file')     
    
    parser.set_defaults(nopREQ=6, probThresh=0.5, pathOUT='', extract_wavs=False, export_separated_dfs=False)
    args = parser.parse_args()

    #%% Parameters
    maxDur=1204 #partition size in seconds
    nop=multiprocessing.cpu_count()
    print(str(int(nop)) + 'cpus found')
    nopMAX = np.max([1,nop-1])
    nopUSE = nopMAX
    if args.nopREQ<nopMAX:
        nopUSE=args.nopREQ
    else:
        nopUSE=nopMAX
    print(str(nopUSE) + 'cpus will be used')   
    if args.probThresh <= 0.99 and args.probThresh >= 0.01:
        probThresh=args.probThresh
        print('Setting threshold value to the requested value')        
    else:
        probThresh=0.5
        print('Threshold value is not accepted, setting it to 0.5')      
    inputWavPath=args.pathIN 
    outputDataPath=args.pathOUT
    if outputDataPath=='': outputDataPath = inputWavPath
#%% Choose classicication model    
    modelFilePath = 'model/model2run.hdf5'
#%% Check if outputDataPath exists and create it if not
    if os.path.exists(outputDataPath + '/detections') == False:
        # os.mkdir((outputDataPath + '/detections'))
        os.makedirs((outputDataPath + '/detections'))

#%% do the job  

    dt = datetime.datetime.now()
    dt1 = dt.strftime("%d/%m/%Y %H:%M:%S") 
    
    accumulativeDuration = 0
    allWavFilePaths = []
    allAccumulativeDurations = []
    allTimeBorders = []
    pool=multiprocessing.Pool(nopUSE)    
    folder_with_recordings=(inputWavPath + '/*.wav')
    all_files = glob.glob(folder_with_recordings)
    for wavFilePath in all_files:
        
        fileDuration=librosa.get_duration(filename=wavFilePath)
        accumulativeDuration +=fileDuration
        if fileDuration<maxDur:
            fileTimeBorders=np.array([0,fileDuration])
            allTimeBorders.append(fileTimeBorders)
            allWavFilePaths.append(wavFilePath)
            allAccumulativeDurations.append(accumulativeDuration)
        else:
            fileTimeBorders=np.arange(0,fileDuration,maxDur)

            if fileTimeBorders[-1]<(fileDuration - 2.0):
                fileTimeBorders = np.append(fileTimeBorders, fileDuration)
            Nsegments = len(fileTimeBorders)-1
            for s in range(Nsegments):
                allTimeBorders.append(np.array([fileTimeBorders[s],fileTimeBorders[s+1]]))  #added np.array
                allWavFilePaths.append(wavFilePath)
                allAccumulativeDurations.append(accumulativeDuration)          

    Npartitions=len(allAccumulativeDurations)
    # print('ste timeBorders ' + str(allTimeBorders[0]) + ' ' + str(allTimeBorders[1]))
    for partitionIdx in range(Npartitions): #range(0,Nsegm-1):       
        # process_segment(allWavFilePaths,outputDataPath,allAccumulativeDurations,allTimeBorders,partitionIdx,modelFilePath,probThresh)
        pool.apply_async(process_segment, args=(allWavFilePaths,outputDataPath,allAccumulativeDurations,allTimeBorders,(partitionIdx, Npartitions),modelFilePath,probThresh))

        
    pool.close()
    pool.join() 


    all_data, analysis_report, tmstmp = detections_report(pathIN = inputWavPath, pathOUT = outputDataPath, probabilityThreshold = probThresh, filesScanned = all_files, extract_wavs=args.extract_wavs, cpus_used = nopUSE, export_separated_dfs = args.export_separated_dfs)
    analysis_report.insert(2, f"Analysis started: {dt1}")
    with open(f"{outputDataPath}/Analysis_report_{tmstmp}.txt", "w+") as fout:
        fout.writelines([line+'\n' for line in analysis_report])
        
#%% waveFileNames    
    # d = {'wfn': wavFileNames }
    # df = pd.DataFrame(data=d)
    # df.to_csv((outputDataPath + '/wavFileNames.txt'), index=False, header=False) #, mode='a')    


if __name__ == "__main__":
    main()
