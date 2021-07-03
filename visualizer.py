#import calls
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import pathlib
from scipy.io import wavfile
import os

#Audio File Names
filenames = []
#Image File Names
filesaves = []
#Initialising Directories
audiodir = "./Audio/"
imgdir = "./img/"
#story the name of files
for file in os.listdir('Audio'):
    if file.endswith(".wav") :
        filenames.append(audiodir+file)
        filesaves.append(imgdir+file.replace('wav','png'))
   
#creating img directory if it does not exist
pathlib.Path(f'img/').mkdir(parents=True, exist_ok=True)
#length = Total number of Audio Files
length = len(filesaves)

for i in range(length):
        #Plotting waveform subplot
    samplingFrequency, signalData = wavfile.read(filenames[i])
    plt.subplot(211)
    plt.title('Wave Diagram')
    plt.plot(signalData)
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')

        #Create a gap
    plt.subplots_adjust(left=0.2,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

        #Plotting spectogram subplot
    plt.subplot(212)
    plt.title('Spectogram')
    plt.specgram(signalData,Fs=samplingFrequency)
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.savefig(filesaves[i])
    plt.close()


