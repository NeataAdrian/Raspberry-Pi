from sense_hat import SenseHat
import time

sense = SenseHat()
b = (0, 0, 204) #Blue
w = (255, 255, 255) #White
e = (0, 0, 0) #Empty
y = (255, 255, 0) #Yellow
r = (255, 0, 0) #red

prenume = [
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, b, e, y, y, e, r, e,
    b, e, b, y, e, y, r, e,
    b, b, b, y, e, y, r, e,
    b, e, b, y, e, y, r, e,
    b, e, b, y, y, e, r, e,
    e, e, e, e, e, e, e, e,
    ]

sense.set_pixels(prenume)
    
