from sense_hat import SenseHat
import time

sense = SenseHat()

e = (0, 0, 0)
b = (0, 0, 255)

Oleft = [ e, e, e, e, e, e, e, e,
          e, b, b, b, b, b, e, e,
          e, b, e, e, e, b, e, e,
          e, b, e, e, e, b, e, e,
          e, b, e, e, e, b, e, e,
          e, b, b, b, b, b, e, e,
          e, e, e, e, e, e, e, e,
          e, e, e, e, e, e, e, e
          ]


Oright = [ e, e, e, e, e, e, e, e,
           e, e, b, b, b, b, b, e,
           e, e, b, e, e, e, b, e,
           e, e, b, e, e, e, b, e,
           e, e, b, e, e, e, b, e,
           e, e, b, b, b, b, b, e,
           e, e, e, e, e, e, e, e,
           e, e, e, e, e, e, e, e
          ]

def left():
    sense.set_pixels(Oleft)

def right():
    sense.set_pixels(Oright)

sense.stick.direction_left = left
sense.stick.direction_right = right

while True:
    pass
