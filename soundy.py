import pygame
pygame.mixer.init()
import time
import numpy as np
import matplotlib.pyplot as plt


import numpy.fft as f

sound = pygame.mixer.Sound("Music/Happy Jinjo House - Banjo-Tooie.ogg")

rate = 22050

arr = pygame.sndarray.samples(sound)
idx = 240000
a = arr.copy()
timestep = .1

steps = rate * timestep

elapsed = 0

limit = np.max(a)

sound.play()
while False:
    t = time.time()
    print elapsed
    sound = pygame.sndarray.make_sound(arr[idx:idx + steps])
    elapsed = time.time() - t
    time.sleep(timestep - elapsed)
    
    sound.play()
    
    idx += steps
