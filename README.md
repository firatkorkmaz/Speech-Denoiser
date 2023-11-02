# Speech Denoiser
A simple program to denoise speech audio samples from multiple audio files by using the **noisereduce** library.

## General Information
This program denoises speech audio samples by asking users to enter either audio filename(s) in (.wav) format or audio folder name from the input and saves the new denoised audio files in (.wav) format. The program also detects stereo/mono channel information of the audio samples automatically and denoises them accordingly.
	
## Technologies
This project is created with:
* Python
* Jupyter Notebook

## Setup & Run
Although an automatic installation command is placed in the source code for the **noisereduce** library, it can also be manually installed by:
```
pip install noisereduce
```
There are 2 different files to run the program in different ways:
1. **Speech_Denoiser.ipynb** can be run with Jupyter Notebook:
```
pip install jupyter
```
```
jupyter notebook
```
2. **Speech_Denoiser.py** can be run directly with Python:
```
python Speech_Denoiser.py
```
There are also 2 different audio samples given as input file examples: **sample1.wav**, **sample2.wav** with their saved results: **sample1_denoised.wav**, **sample2_denoised.wav**
