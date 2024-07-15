from seki_util import game
import random

def alg_random(game_obj:game.Grid):
    '''An implementation of random moves in order to get a grasp of the board reading and handling (subject to the global random seed)'''
    
    #Return x y coords
    #1. Select a position at random
    #2. If zero, select another one
    #3. If not zero, return the coordinates
    while True:
        guess_x=random.randint(1,game_obj._x)
        guess_y=random.randint(1,game_obj._y)
        print('Alice randomly decides: (%s,%s)'%(guess_x,guess_y))
        #print(game_obj.get_value(guess_x,guess_y))
        if game_obj.get_value(guess_x,guess_y)!=0:
            return (guess_x,guess_y)
