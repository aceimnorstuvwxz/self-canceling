#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
处理.conv 文件，变成纯粹的 txt 文件 ，无行头。
'''

import sys
import re
import chardet
import random
from pydub import AudioSegment
import wave
import audioop


reload(sys)
sys.setdefaultencoding("utf-8")


SCOP = 1000



def canceling(fn_origin, fn_record):
    s_origin = AudioSegment.from_wav(fn_origin)
    s_recorded = AudioSegment.from_wav(fn_record)
    
    # make it same loud
    print s_origin.rms, s_recorded.rms, (s_recorded + 0.3).rms
    s_recorded = s_recorded + 0.3

    s_recorded.export("recorded-loud.wav", format='wav')


def combineChannelAndFramerate(pseg):
    ret = pseg.set_frame_rate(16000)
    ret = ret.set_channels(1)
    return ret

def combineThings(fn):
    s = AudioSegment.from_wav(fn)
    ret = combineChannelAndFramerate(s)
    ret.export(fn, format="wav")

def byte2val(twob):
    a = twob[0]
    b = twob[1]
    v = ord(b)*256 + ord(a) - 65536/2
    return v

def val2byte(val):
    v = val + 65536/2
    b = v/256
    a = v - 256*b
    # print val, a, b
    ret = ''
    ret = ret + str(chr(a))
    ret = ret + str(chr(b))
    
    # if len(ret) != 2:
            # print val, "fuck", len(ret)
    # else:
            # print len(ret)
    return ret    

def fuck(seg_record, seg_other):
    ret = ''
    for x in xrange(len(seg_record)/2):
        v_rec = byte2val(seg_record[x*2:x*2+2])
        v_oth = byte2val(seg_other[x*2:x*2+2])

        ser = val2byte(int((v_rec - v_oth)/2)) #/2 for keeping in scope
        ret = ret + ser
    
    return ret

def judge(fn_orig, fn_record):
    s_orig = wave.open(fn_orig, 'r')
    s_recd = wave.open(fn_record, 'r')

    print s_orig.getnframes(), s_orig.getnframes()/s_orig.getframerate(), \
            s_recd.getnframes(), s_recd.getnframes()/s_recd.getframerate()

    
    data_orig = s_orig.readframes(s_orig.getnframes())
    data_record = s_recd.readframes(s_recd.getnframes())

    print len(data_orig)/2, len(data_record)/2

    seg_record = data_record[3*s_recd.getframerate()*2 : 3*s_recd.getframerate()*2 + SCOP *2]
    seg_comment = data_orig[0*s_recd.getframerate()*2 : 10*s_recd.getframerate()*2]

    print len(seg_record), len(seg_comment)

    x = 0
    x_max = 9*s_recd.getframerate()
    min_rms = 100000
    while True:
        
        seg_other = seg_comment[x*2 : 2*(x+SCOP)]

        

        seg_ret = fuck(seg_record, seg_other)

        
        rms = audioop.rms(seg_ret, 2)
        if rms < min_rms:
            min_rms = rms
        
        print 'judge', len(seg_record), len(seg_other), len(seg_ret), x, x_max, rms, min_rms


        x = x + 1
        if x >= x_max:
            break






def shifter(seq):
    '''shift a string '''
    ret = ''
    pos = random.randint(1, len(seq) - 1)

    rd = random.randint(0, 2)
    if rd == 0:
        ret = seq[:pos] + seq[pos+1:]
    elif rd == 1:
        ret = seq[:pos] + seq[pos-1:]
    else:
        ret = seq
    
    return ret



if __name__ == "__main__":
    # canceling("origin.wav", "recorded.wav")
    judge('origin.wav', 'recorded-loud.wav')
    # combineThings("recorded-loud.wav")
    # combineThings("origin.wav")
    # print byte2val('1b')
    # print val2byte(byte2val('1b'))