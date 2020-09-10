import board
import neopixel
import time

PIXELNUM = 300
ORDER = neopixel.GRB
BRIGHTNESS = .25

pixels = neopixel.NeoPixel(board.D18,PIXELNUM,brightness=BRIGHTNESS,auto_write=False)

for i in range(PIXELNUM):
    pixels[i] = (0,0,0)
pixels.show()
