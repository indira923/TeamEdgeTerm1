from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)

rmon4 = [k, k, k, d, d, d, k, k,
         k, k, r, r, r, r, r, k,
         k, k, k, r, r, r, r, k,
         k, b, k, k, b, r, r, k,
         k, b, k, b, k, k, r, k,
         k, b, b, k, k, k, k, k,
         k, k, k, k, k, k, k, p,
         k, p, p, k, p, p, k, k
]


sense.set_pixels(rmon4)		
		
		
		
		
		
		
		
		
		