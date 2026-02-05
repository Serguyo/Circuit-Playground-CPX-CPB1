import board
import digitalio
import time
import neopixel

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
while True:
    for i, color in enumerate(colors):
        led[i] = color

    time.sleep(0.5)

    led.fill((0, 0, 0))
    time.sleep(0.5)
