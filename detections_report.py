# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 12:31:52 2023

@author: psar
"""

import pickle
import glob
import numpy as np
import pandas as pd
import pdb
import librosa
import soundfile as sf
import os
import datetime
import time

def save_check_dup(fname, ext):
    """
    Small helper function to check if a filename exists 
    and if yes, then it adds a number (1, 2, 3) in the end
    of the filename until a non existing filename is found 
    and returns it

    Parameters
    ----------
        fname : str 
            Full Filename (with extension)
        ext : str
            Extension of the file 
    Returns
    -------
        str 
            New filename 
        
    """
    
    import os
    i=1
    if os.path.exists(fname):
        fname = fname.replace(ext, f"_{i}{ext}")
        while os.path.exists(fname):
            i+=1
            fname = fname.replace(f"_{i-1}{ext}", f"_{i}{ext}")
    return fname   


def create_timestamp(eventTime):
    """Creates timestamp of a given time (in seconds) or a list of times

    Parameters
    ----------
        eventTime : int 
            Time of an event in seconds

    Returns
    -------
        tuple 
            tuple with 3 elements which contain (hours, minutes, seconds) with 2 decimal numbers each
            e.g. ('16', '04', '52')
        or
        list
            If a list of event times was given as input, then a list of tuples is returned
            e.g. [('16', '04', '52'), ('05', '34', '07'), ('11', '23', '20')]
    """
    if type(eventTime)==int: 
        minutes,seconds=divmod(eventTime,60)  
        hours, minutes=divmod(minutes,60) 
        
        s=format(int(seconds), '02d')
        m=format(int(minutes), '02d')
        h=format(int(hours), '02d')
                
        # return f"{hours:02d}h{minutes:02d}m{seconds:02d}s"  
        return h, m, s
    elif type(eventTime)==list:
        results = []
        for elem in eventTime:
            results.append(create_timestamp(elem))
        return results        
    
def normalize_single_segment(seg):
    # Normalize by a factor sqrt(Ns)/norm(segment) where Ns is the length of the segment
    return seg*np.sqrt(len(seg))/np.linalg.norm(seg)/10.0


def merge_overlapping(start_end_times):
    """
    Function to merge overlapping intervals.
    
    Parameters
    ----------
        start_end_times : ndarray
            Nx2 array, where N is the number of intervals to be examined
    
    Returns
    -------
        new_intervals : ndarray
            new Mx2 array, where M<=N, with the new merged intervals whenever there was an overlap
        interval_idxs : list
                list with N elements, which indicates where each old interval falls in.
                
    e.g. if 5 intervals are given as input (5x2 array) and the 2nd, 3rd and 4th are overlapping, then
    a 3x2 array will be returned as new_intervals and interval_idxs will be equal to [0, 1, 1, 1, 2].    
    
    """
    if len(start_end_times)==0:
        return start_end_times, []
    new_intervals = [start_end_times[0, :]]
    interval_idxs = [0]
    i=1
    ii=0
    while i < len(start_end_times):
        if new_intervals[-1][1]>start_end_times[i, 0]: 
            new_intervals[-1][1] = start_end_times[i,1]
            interval_idxs.append(ii)
        else:
            new_intervals.append(start_end_times[i, :])
            ii+=1
            interval_idxs.append(ii)
        i+=1
    new_intervals = np.stack(new_intervals)
    return new_intervals, interval_idxs

def separate_dfs(df):
    separated = {}
    for file in df['Begin File'].unique():
        df_current = df[df['Begin File']==file]
        df_current['Selection']-=(df_current['Selection'].min()-1) 
        df_current['Begin Time (s)'] = df_current['File Offset (s)'] 
        df_current['End Time (s)'] = df_current['File Offset (s)']+df_current['dur']

        separated[file] = df_current

    return separated

def detections_report(pathIN, pathOUT, probabilityThreshold = 0.5, filesScanned = [], extract_wavs=True, cpus_used = None, export_separated_dfs=False):
    """
    Function to load files exported from the onset detection and claddification algorithm in the folder 'pathOUT'/detections
    and do the following procedures:
      * Find positive classified segments regarding the probabilityThreshold
      * Merge overlapping segments 
      * Extract segments as wav files
      * Export a Detection Table in txt file format (raven compatible) and in xlsx file format
      * Export an "Analysis_report" file which contain info about the current analysis         

    Parameters
    ----------
        pathIN : str 
            The input path that contains the initial files that where analyzed from the previous step of the tool
        pathOUT : str
            The same as pathIN of another desired path to save results
        probabilityThreshold : float, default 0.5
            Probability Threshold used to classify a segment as positive. If probability>=probabilityThreshold for a segment,
            then it is classified as positive (gunshot).
        
    Returns
    -------
        all_data : DataFrame
            DataFrame of the Detection Table 
        analysis_report : list
            List with lines to be saved in the analysis report file, to be used in the main script of the tool to edit this file
        tmstmp : str    
            Timestamp of the Analysis_report file, used in its filename, in order to access it again through the main script of the tool 
    
    e.g. of a function's call: 
        all_data = detections_report(pathIN = r'C:/Users/user/Desktop/inputs', pathOUT = r'C:/Users/user/Desktop/outputs', probabilityThreshold = 0.5)    
    """
    extracted_wavs_path = f"{pathOUT}/extracted_segments"
    if os.path.exists(extracted_wavs_path):
        from shutil import rmtree 
        rmtree(extracted_wavs_path)           


    folder = f'{pathOUT}/detections'
    segments_extracted = []
    onsetThreshold=-1
    segment_duration = int(0.975*16000)
    dfs=[]
    accumulative_dur = 0
    accumulative_sel = 1
    accumulative_Ndetections=0
    accumulative_Npositives=0

    all_part_filenames = glob.glob(f"{folder}/*.obj")
    # original_filenames = sorted(list(set([fname.split("_start")[0].split("\\")[-1] for fname in all_part_filenames])))
    original_filenames = sorted(list(set([os.path.basename(fname.split("_start")[0]) for fname in all_part_filenames])))

    for (i, original_filename) in enumerate(original_filenames):
        all_parts_filenames = sorted(glob.glob(f"{folder}/{original_filename}*.obj"))

        positives_start_samples_per_part=[]
        positives_probabilities_per_part = []
        for part_filename in all_parts_filenames:
            with open(part_filename, "rb") as fid:
                dataIN = pickle.load(fid,encoding='latin1')  
            detectionsList = dataIN['detectionsList']
            Ndetections = dataIN['Ndetections']
            accumulativeDuration = dataIN['accumulativeDuration']
            onsetThreshold = dataIN['onsetThreshold']
            # Nw = dataIN['Nw']
            # Nr = dataIN['Nr']
            # timeBordersInSeconds = dataIN['timeBordersInSeconds']

            # Find detections classified as positive to keep only these for the next steps 
            probabilities = np.array(detectionsList)[:,1]
            start_samples = np.array(detectionsList)[:,0]
            indexes_of_positives = probabilities>=probabilityThreshold
            accumulative_Ndetections+=Ndetections
            accumulative_Npositives+=indexes_of_positives.sum()
            positives_start_samples_per_part.append(start_samples[indexes_of_positives])
            positives_probabilities_per_part.append(probabilities[indexes_of_positives])
            
        all_positives_probabilities = np.concatenate(positives_probabilities_per_part)
        all_positives_start_samples =  np.concatenate(positives_start_samples_per_part)
        start_end_samples = np.stack([all_positives_start_samples, all_positives_start_samples+segment_duration]).T 
        
        # Merge overlapping segments and calculate average probability of merged segment groups
        new_intervals_out, interval_idxs_out = merge_overlapping(start_end_samples)
        averaged_probs = []
        for idx in range(len(new_intervals_out)):
            current = all_positives_probabilities[np.where(np.array(interval_idxs_out)==idx)]    
            avg = current.sum()/len(current)
            averaged_probs.append(avg.round(5))
        new_intervals_start_times = new_intervals_out[:,0]/8000
        new_intervals_end_times = new_intervals_out[:,1]/8000
        durs = new_intervals_end_times-new_intervals_start_times
        
        #%% Prepare Raven compatible dataFrame to be exported                        
        wavFile = glob.glob(f"{pathIN}/{original_filename}*")[0]            
        timestamps = create_timestamp(new_intervals_start_times.astype(int).tolist())
        instanceTimes = [f'{tmsp[0]}:{tmsp[1]}:{tmsp[2]}' for tmsp in timestamps] 
        indexes = list(range(accumulative_sel,len(new_intervals_out)+accumulative_sel))
        if len(indexes)>0: accumulative_sel = indexes[-1]+1
        dc = {'Selection': indexes, 'View': 'spectrogram', 'Channel': 1, 'Low Frequency (Hz)':0,'High Frequency (Hz)': 8000/2, 'Pattern': 'gunshot',
                'Begin Time (s)': new_intervals_start_times+accumulative_dur,'End Time (s)': new_intervals_end_times+accumulative_dur, 'Begin File': wavFile, 'File Offset (s)': new_intervals_start_times, 
                'TOD': instanceTimes, 'Probability':averaged_probs, 'dur':durs}
        
        df_raven = pd.DataFrame(data=dc)
        dfs.append(df_raven)        
        accumulative_dur=accumulativeDuration

        #%% Prepare filenames, load audio, extract segments
        if extract_wavs:
            exported_filename = [f"{original_filename}_instance_{l[0]}h{l[1]}m{l[2]}s.wav" for l in timestamps] 
                    
            sig0, dum = librosa.load(wavFile, sr=8000, mono=True)
            dcOffset = np.mean(sig0)

            
            os.makedirs(extracted_wavs_path, exist_ok=True)

            for fidx in range(len(new_intervals_out)):
                start_, stop_ = new_intervals_out[fidx, :].astype(int)
                current_segment = sig0[start_:stop_] - dcOffset
                current_segment = normalize_single_segment(current_segment)
                output_filename = f"{extracted_wavs_path}/{exported_filename[fidx]}".replace("\\", "/")
                try:
                    sf.write(output_filename,current_segment,8000)  
                    segments_extracted.append(output_filename)
                except:
                    print("Error extracting file", output_filename)
        

    dt = datetime.datetime.now()
    dt1 = dt.strftime("%d/%m/%Y %H:%M:%S") 
    tmstmp = dt.strftime("%d%m%y_%H%M%S")

    #temporary dataframe used from the UI to present the results     
    all_data = pd.concat(dfs, ignore_index=True).astype({"Selection":int}) 
    fname_xlsx_tmp = f"{pathOUT}/results_raven_tmp.xlsx"
    all_data.to_excel(fname_xlsx_tmp, index=False)

    analysis_report = ["Analysis report:", "---------------", f"Analysis ended: {dt1}", "", f"Directory analyzed: {pathIN}", "", "Paremeters used:", f"\tOnset Threshold: {onsetThreshold}", f"\tprobabilityThreshold: {probabilityThreshold}", f"\tCPUs used: {cpus_used}", "", "Stats:", f"\t# of detected segments: {accumulative_Ndetections}", f"\t# of positive classified segments: {accumulative_Npositives}", f"\t# of segments after merging overlaps: {len(all_data)}", "", "Analysis Files extracted:"]

    #Export dataframe as excel/txt raven compatible
    files_extracted = []
    if export_separated_dfs:
        extracted_results_path = f"{pathOUT}/separated_results"
        os.makedirs(extracted_results_path, exist_ok=True)

        dfs = separate_dfs(all_data)

        for fl in dfs.keys():
            flname = fl.split("\\")[-1].rstrip(".wav")
            fname_txt = f"{extracted_results_path}/{flname}_results_raven_{tmstmp}.txt"
            fname_xlsx = f"{extracted_results_path}/{flname}_results_raven_{tmstmp}.xlsx"
            dfs[fl].to_csv(fname_txt, index=False, sep='\t')
            dfs[fl].to_excel(fname_xlsx, index=False)
            files_extracted.extend([fname_txt, fname_xlsx])
            
    else:
        fname_txt = save_check_dup(f"{pathOUT}/results_raven_{tmstmp}.txt", ".txt")
        fname_xlsx = save_check_dup(f"{pathOUT}/results_raven_{tmstmp}.xlsx", ".xlsx")
        all_data.to_csv(fname_txt, index=False, sep='\t')
        all_data.to_excel(fname_xlsx, index=False)
        files_extracted.extend([fname_txt, fname_xlsx])

    # print("export", export_separated_dfs, files_extracted)
    analysis_report.extend(files_extracted)
    analysis_report.extend(["", f"List of wav files processed ({len(filesScanned)}):"])
    analysis_report.extend(filesScanned)

    #%% Analysis report file

    # analysis_report = ["Analysis report:", "---------------", f"Analysis ended: {dt1}", "", f"Directory analyzed: {pathIN}", "", "Paremeters used:", f"\tOnset Threshold: {onsetThreshold}", f"\tprobabilityThreshold: {probabilityThreshold}", "", "Stats:", f"\t# of detected segments: {accumulative_Ndetections}", f"\t# of positive classified segments: {accumulative_Npositives}", f"\t# of segments after merging overlaps: {len(all_data)}", "", "Analysis Files extracted:", fname_txt, fname_xlsx, "", f"List of wav files extracted ({len(segments_extracted)}):"]
    # analysis_report.extend(segments_extracted)

    with open(f"{pathOUT}/Analysis_report_{tmstmp}.txt", "w+") as fout:
        fout.writelines([line+'\n' for line in analysis_report])
        
    return all_data, analysis_report, tmstmp
