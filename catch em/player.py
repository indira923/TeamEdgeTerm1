
import random              
from sense_hat import SenseHat
sense=SenseHat
class Player:

    def __init__(self,limit_l,limit_r, sense):
        self.limit_r= limit_r
        self.limit_l= limit_l
        self.position= random.randint(limit_l, limit_r)

    def move_right(self):
        if self.position<self.limit_r:
            self.position=self.position+1
    def move_left(self):
        if self.position<self.limit_l:
            self.position= self.position -1
    
    def get_position(self):
        return self.position

    def display(self,move):
        y=7 
        x=self.position%8
        sense.set_pixel (x-move,y,(0,0,0))
        sense.set_pixel(x,y)
        