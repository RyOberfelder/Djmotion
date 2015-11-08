import pygame
pygame.mixer.init()
import time
import numpy as np
import matplotlib.pyplot as plt


import numpy.fft as f

#sound = pygame.mixer.Sound("Music/I would walk 500 miles - The Proclaimers.ogg")
#sound = pygame.mixer.Sound("Music/Happy Jinjo House - Banjo-Tooie.ogg")
#sound = pygame.mixer.Sound("sumsad.ogg")
sound = pygame.mixer.Sound("Music/CrazyFrog-AxelF.ogg")

rate = 22050

arr = pygame.sndarray.samples(sound)
idx = 240000
a = arr.copy()
timestep = .1

steps = rate * timestep

elapsed = 0

limit = np.max(a)

ahat = f.rfft(a, axis = 0)
w = f.rfftfreq(a.shape[0], sound.get_length / a.shape[0])

high_t = ahat.copy()
high_t[w < .06] = 0
high = f.irfft(high_t, axis = 0)

low_t = ahat.copy()
low_t[w > .02] = 0
low = f.irfft(low_t, axis = 0)

med = a - high - low

sound.play()

ind= np.arange(len(w)/2)

tt = np.linspace(0, sound.get_length(), len(a
time = np.array((tt, tt)).transpose()

while False:
    t = time.time()
    print elapsed
    sound = pygame.sndarray.make_sound(arr[idx:idx + steps])
    elapsed = time.time() - t
    time.sleep(timestep - elapsed)
    
    sound.play()
    
    idx += steps
    
    
high_bal = 1.
med_bal = 1.
low_bal = 1.

def set_high_balance(val):
    high_bal = val
    doPass()

def set_med_balance(val):
    med_bal = val
    doPass()
    
def set_low_balance(val):
    low_bal = val
    doPass()
    
    
def doPass():
    Pass = high_bal * high + med_bal * med + low_bal * low
    doFilt()
    
filt = lambda x: x

def nofilt():
    filt = lambda x:x
    doFilt()
    
def robot():
    filt = lambda x: x * np.sin(time * 200)
    
  
