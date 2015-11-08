import pygame
pygame.mixer.init()
import time
import numpy as np
import matplotlib.pyplot as plt


import numpy.fft as f

#sound = pygame.mixer.Sound("Music/I would walk 500 miles - The Proclaimers.ogg")
#sound = pygame.mixer.Sound("Music/Happy Jinjo House - Banjo-Tooie.ogg")
sound = pygame.mixer.Sound("sumsad.ogg")

rate = 22050

arr = pygame.sndarray.samples(sound)
idx = 240000
a = arr.copy()
timestep = .1

steps = rate * timestep

elapsed = 0

limit = np.max(a)

ahat = f.rfft(a, axis = 0)
w = f.rfftfreq(a.shape[0], )

high_t = ahat.copy()
high_t[w < .02] = 0
high = f.irfft(high_t, axis = 0)

low_t = ahat.copy()
low_t[w > .02] = 0
low = f.irfft(low_t, axis = 0)

sound.play()

time = np.array((np.linspace(0, 300, len(a)), np.linspace(0, 300, len(a)))).transpose()

while False:
    t = time.time()
    print elapsed
    sound = pygame.sndarray.make_sound(arr[idx:idx + steps])
    elapsed = time.time() - t
    time.sleep(timestep - elapsed)
    
    sound.play()
    
    idx += steps
