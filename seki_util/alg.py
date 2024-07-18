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

def alg_naive(game_obj:game.Grid):
    '''An algorithm which scans the field and simply goes to try to find the easiest column to reduce to a zero one'''

    #1. Calculate the weight of each column
    #2. Select the smallest one
    #3. Reduce the smallest variable there
    d=dict()
    for i in range(game_obj._x):
        sum_col=0
        for j in range(game_obj._y):
            sum_col+=game_obj.get_grid()[j][i]
        d[i]=sum_col
    #print(d)
    lowest_val=float('inf')
    lowest_key=-1
    for i in d.keys():
        if d[i]<lowest_val:
            lowest_val=min(lowest_val,d[i])
            lowest_key=i
    
    #print(lowest_key)

    smallest_value=float('inf')
    x=0
    y=0
    for i in range(game_obj._y):
        if game_obj.get_grid()[i][lowest_key]<smallest_value and game_obj.get_grid()[i][lowest_key]!=0:
            smallest_value=game_obj.get_grid()[i][lowest_key]
            #print(smallest_value,x,y)
            x=lowest_key+1
            y=i+1
    return (x,y)
    
def alg_minimax(game_obj:game.Grid):
    '''Implementing a minimax algorithm here with a condition that whenever this function is called, Alice is the current player (aka the MAX player) and Bob is always a MIN player.
    '''
    return None

