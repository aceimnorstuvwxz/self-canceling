#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
(C) 2016 unicall

'''


import sys
from pydub import AudioSegment
from pydub.silence import split_on_silence


LENGTH_MIN = 20.0
CUT_START = 60000
CUT_TAIL = 20000
EFFECT_MIN = 2500
EFFECT_MAX = 5600


def xcut(wavfn, outfd):
    cnt = 0
    sound = AudioSegment.from_wav(wavfn)
    print len(sound)

    nck = sound.set_frame_rate(16000)
    nck = nck.set_channels(1)
    nck.export(outfd, format='wav')

    

if __name__ == "__main__":
    
    usage = 'USAGE  wav-format.py f-in f-out'
    if len(sys.argv) != 3:
        print usage
        exit()

    xcut(sys.argv[1], sys.argv[2])