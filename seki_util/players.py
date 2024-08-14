from seki_util import game, alg
from seki_util.names import Names

class Player:
    def __init__(self,name:Names):
        self.name=name
    

    def move(self,game_obj:game.Grid,x,y,verbal=False,passing=False):
        if not passing:
            print(self.name.name,'decreases (%s,%s)'%(x,y))
        else:
            print(self.name.name,'is passing on the move.')
        if not passing:
            game_obj.decrease(x,y)
        thought=game_obj.evaluate(verbal)
        return thought
    
    def analyze(self,game_obj:game.Grid,decision_max_seconds,move=True,verbal=False):
        '''
        Suggests the next most beneficial move to the player.
        According to the design this function should only be called when the player is Alice AKA a bot.
        '''
        guess_x,guess_y = alg.alg_minimax_timed(game_obj,decision_max_seconds)
        if move:
            thought=self.move(game_obj,guess_x,guess_y,verbal)
        else:
            thought=False
        game_obj.print_grid()
        return thought