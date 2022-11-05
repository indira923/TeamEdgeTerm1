import random 
from sense_hat import SenseHat
from time import sleep
sense=SenseHat
Sense = SenseHat()
# sleep()
# speed = 1

class Berry:
    def __init__(self, color, speed, value):
        self.position = random.randint (0,7)
        self.color = color
        self.speed = .5
        self.value = value
        self.posX = random.rand.int(0,7)
        self.posY = 0 

class Berry:
    def drop(self):
    #    if self.position <=55:
    #        self.position += 8
        sleep (self.speed)
        if self.posY >=0 and self.posY<7:
            self.posY+=1
        self.display()


    def display (self):
        x = self.posX
        y=self.posY
        sense.set_pixel (x,(y-1), (0,0,0))
        sense.set_pixel(x,y,(200, 155, 255))
        x= self.posY
        y = self.posY
