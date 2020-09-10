import board
import neopixel
import time
import math
import random

bpc = 8
vpc = 2 ** bpc
vpp = vpc - 1
semicol = 2 * vpp
totalcol = 3 * vpp
count = 300
speed = 1800
direction = 1
start = 76
end = 299
length = end - start + 1
inc = totalcol/length
wait = ((speed / length) - (speed / length * 0.1))

order = neopixel.GRB
brightness = 0.25

pixels = neopixel.NeoPixel(board.D21,count,brightness=brightness,auto_write=False)

colors = []
for n in range(totalcol):
    if n < (vpp):
        r = vpp - n
        g = n
        b = 0
    elif n < (semicol):
        r = 0
        g = vpp - (n % vpp)
        b = n % vpp
    elif n < totalcol:
        r = n % vpp
        g = 0
        b = vpp - (n % vpp)
    else:
        r,g,b = 0,0,0
    r,g,b = r,g,b
    colors.append((r,g,b))

for i in range(start):
    pixels[i] = (0,0,0)

if direction > 0:
    rng = (0,length,1)
else:
    rng = (length-1,-1,-1)
while True:
    for i in range(*rng):
        for j in range(start,end+1):
            k = round(((j + i) * inc) % totalcol)
            pixels[j] = colors[k]
        pixels.show()
        time.sleep(wait)
