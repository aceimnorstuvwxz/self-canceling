#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
录音直接播放。
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
      
def mic2speaker():  

    #open output stream
    po = PyAudio()
    ostream  = po.open(format = paInt16, channels = 1,  
                    rate = framerate, output = True)

    #open the input of wave  
    pa = PyAudio()  
    stream = pa.open(format = paInt16, channels = 1,  
                    rate = framerate, input = True,  
                    frames_per_buffer = NUM_SAMPLES)  
    save_buffer = []  
    count = 0  
    while True:  
        #read NUM_SAMPLES sampling data  
        string_audio_data = stream.read(NUM_SAMPLES)  
        ostream.write(string_audio_data)

  
def main():  
    root = Tk()  
    my_button(root,"Record a wave","clik to record",record_wave)  
    root.mainloop()  
      
if __name__ == "__main__":
    mic2speaker()
