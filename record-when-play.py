#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
在放音的同时录音。
'''

import sys
import time
# import re
# import chardet
# import random
# from pydub import AudioSegment
# import wave
# import audioop
import pygame  #for paly sound

import pyglet

import numpy as np  
from pyaudio import PyAudio,paInt16  
from datetime import datetime  
import wave  
from Tkinter import *  

reload(sys)
sys.setdefaultencoding("utf-8")



def paly_sound():
    pygame.mixer.init(frequency=16000)  #
    track1=pygame.mixer.music.load(gFn)
    pygame.mixer.music.play()
    # time.sleep(1000)


  
#define of params  
NUM_SAMPLES = 2000
framerate = 16000  
channels = 1  
sampwidth = 2  
#record time  
TIME = 100  

gFn = ''
  
def save_wave_file(filename, data):  
    '''''save the date to the wav file'''  
    wf = wave.open(filename, 'wb')  
    wf.setnchannels(channels)  
    wf.setsampwidth(sampwidth)  
    wf.setframerate(framerate)  
    wf.writeframes("".join(data))  
    wf.close()  
  
def my_button(root,label_text,button_text,button_func):    
    '''''''function of creat label and button'''    
    #label details    
    label = Label(root)    
    label['text'] = label_text    
    label.pack()    
    #label details    
    button = Button(root)    
    button['text'] = button_text    
    button['command'] = button_func    
    button.pack()     
      
def record_wave():  
    #open the input of wave  
    paly_sound()
    pa = PyAudio()  
    stream = pa.open(format = paInt16, channels = 1,  
                    rate = framerate, input = True,  
                    frames_per_buffer = NUM_SAMPLES)  
    save_buffer = []  
    count = 0  
    while count < TIME*4:  
        #read NUM_SAMPLES sampling data  
        string_audio_data = stream.read(NUM_SAMPLES)  
        save_buffer.append(string_audio_data)  
        count += 1  
        print '.',
  
    filename = gFn + '.rec.wav'#datetime.now().strftime("%Y-%m-%d_%H_%M_%S")+".wav"  
    save_wave_file(filename, save_buffer)  
    save_buffer = []  
    print filename, "saved"  
  
def main():  
    root = Tk()  
    my_button(root,"Record a wave","clik to record",record_wave)  
    root.mainloop()  
      
if __name__ == "__main__":
    global gFn
    gFn = sys.argv[1]
    main()  


# if __name__ == "__main__":
    # canceling("origin.wav", "recorded.wav")
    # judge('origin.wav', 'recorded-loud.wav')
    # combineThings("recorded-loud.wav")
    # combineThings("origin.wav")
    # print byte2val('1b')
    # print val2byte(byte2val('1b'))
