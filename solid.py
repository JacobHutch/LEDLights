import board
import neopixel
import time
import sys

pixelnum = 300
pin = board.D21
brightness = 0.25
order = neopixel.GRB
pixels = neopixel.NeoPixel(pin,pixelnum,brightness=brightness,auto_write=False,pixel_order=order)

color = tuple([int(x) for x in sys.argv[1].split(",")])

for i in range(pixelnum):
    pixels[i] = (0,0,0)

for i in range(76,pixelnum):
    pixels[i] = color
pixels.show()
