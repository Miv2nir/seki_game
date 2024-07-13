from seki_util import game
from enum import IntEnum

class Names(IntEnum):
    BOB=0 #player
    ALICE=1 #bot

class Player:
    def __init__(self,name:Names):
        self.name=name
    

    def move(self,game_obj:game.Grid,x,y):
        print(self.name.name,'decreases (%s,%s)'%(x,y))
        game_obj.decrease(x,y)
        game_obj.evaluate()
        return game_obj