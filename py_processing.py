import pyfirmata
import time                         
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

board=pyfirmata.Arduino('COM13')      #connect to arduino

data=pd.read_csv('eeg.csv')         #open the file
Y1=data.iloc[:,0]                     #to select only 1st column

arr=np.array(Y1)                      #convert EEG raw signal as array
l=np.array_split(arr,10)              #convert array into 10 equal parts
l1=np.array(l)                        #casting l1 from list to array

for x in range(0,len(l1),1):          #for every sub-array in l1 array
    freqs,psd = signal.welch(l1[x],window='hann',fs=1000)
    plt.figure(figsize=(5, 4))
    plt.plot(freqs, psd)
    plt.title('PSD: power spectral density')
    plt.xlabel('Frequency')
    plt.ylabel('Power')
    plt.xlim(8,12)
    plt.tight_layout()                
    plt.show()                          #plot the power spectral density vs freq
    result = np.where(np.logical_and(freqs>= 8, freqs<= 12)) #for freq in range of 8-12 hz
    for x in freqs[result]:        
        if (psd[result] > 1000):          #if power > threshold
              board.digital[12].write(1)#motor runs
              time.sleep(2)
              board.digital[12].write(1)

        else:
              board.digital[12].write(0)#if power< threshold
              time.sleep(0.1)           #motor stops

board.digital[13].write(0)           #to stop motor after completion of loop


