from sense_hat import SenseHat
import time

sense= SenseHat()

r=(255,0,0)
b=(1,1,1)

matrice= [ r, r, r, r, r, r, r, r,
           r, b, b, b, b, b, b, r,
           r, b, r, r, r, r, b, r,
           r, b, r, b, b, r, b, r,
           r, b, r, b, b, r, b, r,
           r, b, r, r, r, r, b, r,
           r, b, b, b, b, b, b, r,
           r, r, r, r, r, r, r, r,
           ]

matrice2= [b, b, b, b, b, b, b, b,
           b, r, r, r, r, r, r, b,
           b, r, b, b, b, b, r, b,
           b, r, b, r, r, b, r, b,
           b, r, b, r, r, b, r, b,
           b, r, b, b, b, b, r, b,
           b, r, r, r, r, r, r, b,
           b, b, b, b, b, b, b, b,
           ]

for i in range(10):
        sense.set_pixels(matrice)
        time.sleep(0.5)
        sense.set_pixels(matrice2)
        time.sleep(0.5)


