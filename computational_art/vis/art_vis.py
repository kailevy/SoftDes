"""
Art visualizer
Kai Levy
Software Design 2015
"""

import alsaaudio
import audioop
import pygame
    
inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,0)
inp.setchannels(1)
inp.setrate(16000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)
        
MAXVOL = 20000

image_list = []

pygame.init()

screen = pygame.display.set_mode((350,350))

for i in range(80):
    image_list.append(pygame.image.load("art_" + str(i) + ".png"))



def remap(val, inp_start = 0, inp_end = MAXVOL, out_start = 0, out_end = 79):
    return int(round(out_start + float((val - inp_start)) / 
        (inp_end - inp_start) * (out_end - 
            out_start)))


while True:
        l,data = inp.read()
        if l:
            d = audioop.rms(data,2)
            if d > MAXVOL:
                d = MAXVOL
            image_load = remap(d)
            screen.blit(image_list[image_load],(0,0))
            pygame.display.flip()