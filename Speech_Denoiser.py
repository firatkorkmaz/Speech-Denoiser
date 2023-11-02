# Speech Denoiser #

import os
import glob
import numpy as np
from scipy.io import wavfile

try:
    import noisereduce as nr
except:
    os.system("pip install noisereduce")
    import noisereduce as nr


def Denoiser(in_path):
    if not os.path.isfile(in_path):
        print(f"{in_path} does Not Exist!\n")
        return
    
    try:
        rate, data = wavfile.read(in_path)
    except:
        print(f"{in_path} is Not A Wave File!\n")
        return
    
    datashape = data.shape
    
    stereo = False
    if len(datashape) == 1:    # 1 Channel
        data = np.reshape(data, (1, -1))
    else:                      # Multi Channel
        data = np.reshape(data, (datashape[1], -1))
        stereo = True
    
    # Noise Reduction
    reduced_noise = nr.reduce_noise(y=data, sr=rate, stationary=True)
    
    # Writing the New File
    out_path = in_path[:in_path.rfind(".")] + "_denoised.wav"
    wavfile.write(out_path, rate, reduced_noise.reshape(datashape))
    
    # Printing Process Information
    print(f"Source File: {in_path}")
    if stereo:
        print(f"Audio Info : Stereo, {rate}Hz")
    else:
        print(f"Audio Info : Mono, {rate}Hz")
    print(f"Saved File : {out_path}")
    print()


def main():
    exit_main = False
    while True:
        inputMode = input("File Name(s): 1\nFolder Name : 2\nExit Program: *\nSelect Input Mode: ")
        if inputMode == "*":
            exit_main = True
            break
        
        try:
            inputMode = int(inputMode.strip())
            if inputMode != 1 and inputMode != 2:
                print("Enter 1 or 2!\n")
                continue
        except:
            print("Enter 1 or 2!\n")
            continue
        
        break
    
    
    if not exit_main:
        if inputMode == 1:
            # Example: sample1.wav, sample2.wav
            inputString = input("\nExample: sample1.wav, sample2.wav\nEnter Audio File Name(s): ")
            splitString = [x.strip() for x in inputString.split(',')]
            in_paths = [f for f in splitString]

        else:
            # Example: audio
            inputString = input("\nExample: audio\nEnter Audio Folder Name: ")
            splitString = inputString.strip()
            if not os.path.isdir(splitString):
                print("\nFolder does Not Exist!")
            in_paths = glob.glob(splitString+'/*.*')

        if len(in_paths) > 0:
            print()
            for file in in_paths:
                Denoiser(file)


if __name__ == '__main__':
    
    main()