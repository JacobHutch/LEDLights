import board
import neopixel
import time
import math
import random
import sys

bpc = 8
vpc = 2 ** bpc
vpp = vpc - 1
semicol = 2 * vpp
totalcol = 3 * vpp
count = 300
speed = 300
direction = 1
start = 88
end = 299
desiredLength = end - start + 1
inc = len(sys.argv) - 4

presets = {"red":[(255,0,0)],"green":[(0,255,0)],"blue":[(0,0,255)],
        "magenta":[(255,0,255)],"yellow":[(255,255,0)],"cyan":[(0,255,255)],
        "purple":[(95,0,255)],"orange":[(255,127,0)],
        "vapor":[(0,255,127),(0,127,255),(127,0,255),(255,0,255)],
        "rainbow":[(255,0,0),(255,255,0),(0,255,0),(0,255,255),(0,0,255),(255,0,255)],"watermelon":[(255,0,63),(0,255,63)]}

def colClamp(num,mini=0,maxi=255):
    return min(max(num,mini),maxi)

cardinals = []

for i in range(4,inc + 4):
    if(sys.argv[i] in presets):
        for j in presets[sys.argv[i]]:
            cardinals.append(j)
    else:
        col = sys.argv[i].split(",")
        cardinals.append(tuple([int(x) for x in col]))

inc = len(cardinals)

if(sys.argv[1] == "true" and inc > 2):
    for i in range(inc - 2,0,-1):
        if(cardinals[i] in presets):
            for j in presets[cardinals[i]]:
                cardinals.append(j)
        else:
            cardinals.append(cardinals[i])
    inc = (inc * 2) - 2

if(sys.argv[2] == "full"):
    lpg = round(desiredLength / inc)
elif(sys.argv[2] == "part"):
    lpg = round(desiredLength / ((inc + 2) / 2))
elif(sys.argv[2] == "half"):
    lpg = round(desiredLength / (((inc + 2) / 2) - 1))
else:
    lpg = round(desiredLength / (inc * float(sys.argv[2])))
lpg = max(lpg,1)

print(cardinals)

length = lpg * inc
wait = ((speed / length) - (speed / length * 0.1))

order = neopixel.GRB
brightness = float(sys.argv[3])
bright = round(1/brightness)

pixels = neopixel.NeoPixel(board.D21,count,brightness=0.5,auto_write=False)

colors = []

for i in range(inc):
    rInc = (cardinals[i][0] - cardinals[(i + 1) % inc][0]) / lpg
    gInc = (cardinals[i][1] - cardinals[(i + 1) % inc][1]) / lpg
    bInc = (cardinals[i][2] - cardinals[(i + 1) % inc][2]) / lpg

    for j in range(lpg):
        r = round(cardinals[i][0] - (rInc * j))
        g = round(cardinals[i][1] - (gInc * j))
        b = round(cardinals[i][2] - (bInc * j))

        colors.append((r,g,b))

print(colors)

for i in range(start):
    pixels[i] = (0,0,0)

if direction > 0:
    rng = (0,length,1)
else:
    rng = (length-1,-1,-1)
while True:
    for i in range(*rng):
        for j in range(start,end+1):
            k = round((j + i) % length)
            if(j % bright == 0):
                pixels[j] = colors[k]
        pixels.show()
        time.sleep(wait)
