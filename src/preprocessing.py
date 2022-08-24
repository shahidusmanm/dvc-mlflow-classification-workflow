import pandas as pd
import numpy as np
import os
import glob, librosa
import IPython.display as ipd
from tqdm import tqdm


def getPitch(x, fs, winLen=0.02):
    #winLen = 0.02 
    p = winLen*fs
    frame_length = int(2**int(p-1).bit_length())
    hop_length = frame_length//2
    f0, voiced_flag, voiced_probs = librosa.pyin(y=x, fmin=80, fmax=450, sr=fs, frame_length=frame_length,hop_length=hop_length)
    
    tempogram = librosa.feature.tempogram (y=x, sr = fs)
    return f0,voiced_flag, tempogram

def getXy(files, labels, scale_audio=False, onlySingleDigit=False):

    X,y =[],[]
    for file in tqdm(files):
        print (file)
        fileID = file.split('/')[-1]
        file_name = file.split('/')[-1]
        yi = labels
        fs = None # if None, fs would be 22050
        x, fs = librosa.load(file,sr=fs)
        if scale_audio: x = x/np.max(np.abs(x))
        f0, voiced_flag, tempogram = getPitch(x,fs,winLen=0.02)

        power = np.sum(x**2)/len(x)
        pitch_mean = np.nanmean(f0) if np.mean(np.isnan(f0))<1 else 0
        pitch_std  = np.nanstd(f0) if np.mean(np.isnan(f0))<1 else 0
        voiced_fr = np.mean(voiced_flag)
        tempogram = np.nanmean(tempogram) if np.mean(np.isnan(tempogram))<1 else 0

        xi = [power,pitch_mean,pitch_std,voiced_fr, tempogram]
        X.append(xi)
        y.append(yi)
    
    return np.array(X),np.array(y)


def preprocessing(data_path):
    sample_path = data_path + '/raw/Potter/*.wav'
    harry_files = glob.glob(sample_path)

    sample_path = data_path + '/raw/Starwars/*.wav'
    starwars_files = glob.glob(sample_path)

    print ('Processing Starwars audios into features')
    X_starwars, y_starwars = getXy(starwars_files, labels = "Starwars", scale_audio=True, onlySingleDigit=True)

    print ('Processing Harry audios into features')
    X_harry, y_harry = getXy(harry_files, labels = "Harry", scale_audio=True, onlySingleDigit=True)

    X = np.concatenate((X_harry, X_starwars), axis = 0)
    y = np.concatenate((y_harry, y_starwars), axis = 0)

    np.savetxt('features_X.npy', X)
    np.savetxt('features_y.npy', y, fmt="%s")

    features_df = pd.DataFrame(data = X, columns = ['power','pitch_mean','pitch_sd','voiced_fr', 'tempogram'])
    features_df['label'] = y

    features_df.to_csv(data_path + '/features/features.csv', index = False)

    return features_df


path = 'C:/Users/Usman/dvc-mlflow-classification-workflow/data'
print (path)
