
from sense_hat import SenseHat
from time import sleep
import random
from player import Player

sense=SenseHat()

class Game:
    def __init__(self):

        self.score = 0
        self.game_over=False
        self.speed = .5
        self.berries : self.berries = []
        self.player = Player(56,63, sense)


    def start(self, colors):
        sense.show_message("Catchem!",text_colour=colors,scroll_speed=0.05)

    def play(self):
        self.start((0,0,255))
        self.player.display(0)
        while not self.game_over:
            for event in sense.stick.get_events():
                if event.action == "pressed" and event.direction == "left":
                    print("left")
                    self.player.move_left()

                   # self                                                                          