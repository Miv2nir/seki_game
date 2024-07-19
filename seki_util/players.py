from seki_util import game, alg
from seki_util.names import Names

class Player:
    def __init__(self,name:Names):
        self.name=name
    

    def move(self,game_obj:game.Grid,x,y):
        print(self.name.name,'decreases (%s,%s)'%(x,y))
        game_obj.decrease(x,y)
        thought=game_obj.evaluate()
        return thought
    
    def analyze(self,game_obj:game.Grid,move=True):
        '''
        Suggests the next most beneficial move to the player.
        According to the design this function should only be called when the player is Alice AKA a bot.
        '''
        guess_x,guess_y = alg.alg_minimax(game_obj)
        if move:
            thought=self.move(game_obj,guess_x,guess_y)
        else:
            thought=False
        return thought