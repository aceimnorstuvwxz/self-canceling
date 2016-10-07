#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
FFT 和 IFFT在音频上的测试
http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.ifft.html


wav >> fft >> ifft >> wav 
'''

import matplotlib.pyplot as plt
import numpy as np
import wave
import pylab as pl
import struct
import math
# t = np.arange(400)
# n = np.zeros((400,), dtype=complex)
# n[40:60] = np.exp(1j*np.random.uniform(0, 2*np.pi, (20,)))
# s = np.fft.ifft(n)
# plt.plot(t, s.real, 'b-', t, s.imag, 'r--')

# plt.legend(('real', 'imaginary'))

# plt.show()


FFT_WIDTH = 512 # 0.02sec


def a():
    wav = wave.open('anpb.wav', 'rb')
    wavdata = wav.readframes(wav.getnframes())
    wav.close()

    realdata = []
    for i in xrange(len(wavdata)/2):
        d = wavdata[i*2:i*2+2]
        # v = ord(d[0]) + ord(d[1])*256 #先传低位 #这是unsigned short的时候的方法
        v = struct.unpack('h', d) #而实际上是short类型，string 到其它类型的转换可以用struct里面的函数
        realdata.append(v)

    print realdata[0:200]
    datalen = len(realdata)/10
    plt.plot(range(datalen), realdata[0:datalen])
    plt.show()

def b():
    # 打开WAV文档
    f = wave.open(r"anpb.wav", "rb")
    # 读取格式信息
    # (nchannels, sampwidth, framerate, nframes, comptype, compname)
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    # 读取波形数据
    str_data = f.readframes(nframes)
    f.close()
    #将波形数据转换为数组
    wave_data = np.fromstring(str_data, dtype=np.short)

    plt.subplot(211)
    sz = len(wave_data)/100
    plt.plot(range(sz), wave_data[sz*50:sz*50+sz])
    # plt.show()

    #转换到fft
    ifft_data = []
    for i in range(int(len(wave_data)/FFT_WIDTH)):
        seg = wave_data[i*FFT_WIDTH:i*FFT_WIDTH + FFT_WIDTH]
        fft_ret = np.fft.fft(seg)
        ifft_ret = np.fft.ifft(fft_ret)
        ifft_data.extend(ifft_ret)
    

    plt.subplot(212)
    # sz = len(ifft_data)/100
    plt.plot(range(sz), ifft_data[sz*50:sz*50+sz])
    plt.show()



if __name__ == "__main__":
    # global gFn
    # gFn = sys.argv[1]
    # main()
    b()  
    # a()
    pass