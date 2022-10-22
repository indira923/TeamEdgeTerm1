import random 
from sense_hat import SenseHat
from time import sleep
sense=SenseHat
Sense = SenseHat()
sleep()
speed = 1
-0.5

class Berry:
    def __init__(self, color, speed, value):
        self.position = random.randint (0,7)
        self.color = color
        self.speed = speed
        self.speed = value 
 
class Berry:
    def drop(self):
       if self.position <=55:
           self.position += 8
           self.display()
    def display (self):
        x = self.position%8
        y=self.position1/8
        sense.set_pixel (x,y-1 (0,0,0))
        sense.set_pixel(x,y,self.color)
