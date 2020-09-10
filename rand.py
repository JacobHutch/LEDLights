import board
import neopixel
import time
import random

pixelnum = 300
pin = board.D21
brightness = 0.25
order = neopixel.GRB
pixels = neopixel.NeoPixel(pin,pixelnum,brightness=brightness,auto_write=False,pixel_order=order)

color = (0,0,0)
while True:
    for i in range(pixelnum):
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pixels[i] = color
    pixels.show()
