#############################################################################
# realtime.py 
# Nicolas Brochec, TOKYO UNIVERSITY OF THE ARTS
# ブロシェック・ニコラ、東京藝術大学　音楽音響創造科　博士課程一年生
# GPL-3.0 license
#############################################################################
# Code description:
# Load a MLP model and predict class and values from audio input in real-time. 
#############################################################################


import pyaudio, os, librosa, time, pythonosc, math, time, glob
import tensorflow as tf
import numpy as np
import pandas as pd
from pythonosc import udp_client, osc_message_builder
from pythonosc.dispatcher import Dispatcher
import resampy

# =========================================================================================
# LOAD TRAINED MODEL
# It was trained previously

pathModels = os.path.abspath(os.path.join(os.path.dirname(__file__)))
lastModel = 'mss23_hyperas.h5'

loadModel = tf.keras.models.load_model(pathModels+'/'+lastModel)
print("M O D E L", lastModel  ,"H A S   B E E N   L O A D E D!")

# =========================================================================================
# GLOBAL FUNCTION DECLARATIONS

# Get Spectrogram
def get_spectrogram(x):
    melSpec = librosa.feature.melspectrogram(y=x, sr=sampleRate, n_fft=n_fft, hop_length=hop_length)
    melSpec = librosa.power_to_db(melSpec)
    spectrogram = scale_minmax(melSpec, 0, 1.).astype("float32")
    return spectrogram

# Normalize spectrogram
def scale_minmax(X, min=0.0, max=1.0):
    if ((X.max()-X.min()) == 0):
        upsilon = 0.00001
        X_std = (X - X.min()) / ((X.max()-X.min())+upsilon)
        X_scaled = X_std * (max - min) + min
    else:
        X_std = (X - X.min()) / (X.max()-X.min())
        X_scaled = X_std * (max - min) + min
    return X_scaled

# Resample Sound
def resample_sound(X, srate, sampleRate):
    return resampy.resample(X, srate, sampleRate)

# =========================================================================================
# GLOBAL VARIABLE DECLARATIONS
sampleRate = 48000
n_fft = 2048
hop_length = 512
buffer = 512
buffer_size = buffer*2

# Instantiate PyAudio
audioFlux = pyaudio.PyAudio() 

# =======================================================================
# SEND OSC MESSAGE TO MAX PATCH

def send_OSC(classProb, predictedClass):
    ipAddress = "127.0.0.1"
    port = 5005

    client = udp_client.SimpleUDPClient(ipAddress, port)

    classProbability = classProb.flatten()

    probabilityMSG = osc_message_builder.OscMessageBuilder(address = '/percentage')
    classMSG = osc_message_builder.OscMessageBuilder(address= '/class')

    # -------
    for i in range(len(classProbability)):
        probabilityMSG.add_arg(classProbability[i], arg_type='f')

    # -------
    classMSG.add_arg(predictedClass, arg_type='i')

    # -------
    probabilityMSG = probabilityMSG.build()
    classMSG = classMSG.build()
    client.send(probabilityMSG)
    client.send(classMSG)

# =========================================================================
# PROCESS INCOMING AUDIO SIGNAL

cumulativeAudio = np.zeros(6656,)

def callback(in_data, frame_count, time_info, flag):
    global cumulativeAudio
    
    audioSamples = np.frombuffer(in_data, dtype='float32')
    audioSamples = resample_sound(audioSamples, sampleRate, 24000)
    concate = np.concatenate((cumulativeAudio, audioSamples), axis=0)
    
    samples_to_process = math.floor(14*buffer)
    if concate.shape[0] >= samples_to_process:
        # Ensure we use the most recent samples
        concate = concate[-samples_to_process:]
        
        realtimeSpec = get_spectrogram(concate).flatten().reshape(1, 1920)
    
        audioOn = np.sum(np.abs(audioSamples))

        # Verify that audio is present
        if audioOn > 0 :
            print('Now running!')
            # Assuming loadModel is a pre-trained model
            pred = loadModel.predict_on_batch(realtimeSpec)
            predictedClass = int(np.argmax(pred[0]))
            classProb = pred[0]
            
            send_OSC(classProb, predictedClass)
        else:
            print('Waiting for audio...')
            time.sleep(0.25)
    
    # Update cumulativeAudio with the latest audio samples
    cumulativeAudio = concate[-samples_to_process:]
    
    return None, pyaudio.paContinue

# =======================================================================
# OPEN THE AUDIO STREAM
audioStream = audioFlux.open(format=pyaudio.paFloat32,
                 channels=1,
                 rate=sampleRate,
                 output=False,
                 input=True,
                 input_device_index=1,
                 stream_callback=callback,
                 frames_per_buffer=buffer_size)

audioStream.start_stream()

# =======================================================================
# RELATIF AU FLUX ENTRANT
while audioStream.is_active():
	time.sleep(0.25)
audioStream.close()
pa.terminate()

