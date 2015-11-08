import pygame
pygame.mixer.init()
import time
import numpy as np
import matplotlib.pyplot as plt













import numpy.fft as f

#sound = pygame.mixer.Sound("Music/Iwouldwalk500miles-TheProclaimers.ogg")
#sound = pygame.mixer.Sound("Music/HappyJinjoHouse-Banjo-Tooie.ogg")
sound = pygame.mixer.Sound("Music/sumsad.ogg")
#sound = pygame.mixer.Sound("Music/CrazyFrog-AxelF.ogg")
#sound = pygame.mixer.Sound("Music/WagonWheelDariusRucker.ogg")



arr = pygame.sndarray.samples(sound)

a = arr.copy()



timestep = 2
rate = 22050

beat = 60./122 * rate

steps = 2*int(rate * timestep / 2)

windows = []

elapsed = 0
idx = 0
while elapsed < sound.get_length():
    windows += [idx]
    elapsed += timestep
    idx += steps

windows = windows[:-1]

limit = np.max(a)
high = a * 0
med = a * 0
low = a * 0
for p in windows:
    ahat = f.rfft(a[p:p + steps], axis = 0)
    print ahat.shape
    w = f.rfftfreq(steps, 1./rate)

    high_t = ahat.copy()
    high_t[w < 1400] = 0
    high [p:p + steps]= f.irfft(high_t, axis = 0)

    low_t = ahat.copy()
    low_t[w > 600] = 0
    low[p:p + steps] = f.irfft(low_t, axis = 0)

med = a - high - low


scratch = pygame.sndarray.make_sound(pygame.sndarray.array(pygame.mixer.Sound("Music/scratch.ogg"))[.5 * rate:.7 * rate])


sound.play()

ind= np.arange(a.shape[0]/2)

tt = np.linspace(0, sound.get_length(), len(a))
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
    
def scratchback(n):
    scratch.play();
    temp = arr[:beat *n]
    arr[beat*n :] = arr[:-beat*n ]
    arr[:beat * -n] =temp
