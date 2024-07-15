from seki_util import game
import random

def alg_random(game_obj:game.Grid):
    '''An implementation of random moves in order to get a grasp of the board reading and handling'''
    
    #Return x y coords
    #1. Select a position at random
    #2. If zero, select another one
    #3. If not zero, return the coordinates
    zero_target=True
    while zero_target:
        guess_x=random.randint(1,game_obj.x)
        guess_y=random.randint(1,game_obj.y)
        print('Alice randomly decides: (%s,%s)'%(guess_x,guess_y))
        print(game_obj.space[guess_y-1][guess_x-1])
        break
