import board
import neopixel
import time

PIXEL_NUM = 300
ORDER = neopixel.GRB
BRIGHTNESS = .15

pixels = neopixel.NeoPixel(board.D21,PIXEL_NUM,brightness=BRIGHTNESS,auto_write=False)
def flash():
    for i in range(PIXEL_NUM):
        pixels[i] = (0,255,255)
    pixels.show()
    time.sleep(5)
    for i in range(PIXEL_NUM):
        pixels[i] = (0,0,0)
    pixels.show()

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)

def rainbow():
    for j in range(255):
        for i in range(115,PIXEL_NUM):
            pixel_index = (i * 256 // PIXEL_NUM) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(.001)

while True:
    rainbow()
