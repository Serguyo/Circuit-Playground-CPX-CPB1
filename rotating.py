import board
import digitalio
import time
import neopixel

#all 10 colors on 10 leds on the circuit playground

colors = [
    (225, 0, 0),
    (225, 50, 0),
    (175, 200, 0),
    (100, 225, 0),
    (0, 225, 0),
    (0, 225, 50),
    (25, 225, 225),
    (0, 0, 225),
    (100, 25, 225),
    (225, 0, 225),
]

led = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=True)
led.brightness = 0.25
print(dir(led))


#loop infinitely 
while True:

# loop through each LED (all 10)
    for l in range(10):

#sets the LED number l to the color at the position l in the colors list. 
        led[l] = colors[l]

    time.sleep(0.1)

    # rotate the colors by one position in the clockwise direction
    colors = colors[1:] + colors[:1]
