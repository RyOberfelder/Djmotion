import pygame
pygame.mixer.init()
import time

sound = pygame.mixer.Sound("sumsad.ogg")

rate = 22050

arr = pygame.sndarray.samples(sound)
idx = 240000

timestep = .1

steps = rate * timestep

elapsed = 0

sound.play()
while False:
    t = time.time()
    print elapsed
    sound = pygame.sndarray.make_sound(arr[idx:idx + steps])
    elapsed = time.time() - t
    time.sleep(timestep - elapsed)
    
    sound.play()
    
    idx += steps
