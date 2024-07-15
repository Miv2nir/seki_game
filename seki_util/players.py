from seki_util import game, alg
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
    
    def analyze(self,game_obj:game.Grid):
        '''
        Suggests the next most beneficial move to the player.
        According to the design this function should only be called when the player is Alice AKA a bot.
        '''
        return alg.alg_random(game_obj)