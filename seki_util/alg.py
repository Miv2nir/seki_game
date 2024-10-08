from seki_util import game
from seki_util.names import Names
import random,copy
from math import inf
import threading,multiprocessing,time


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
    
def if_terminal(game_obj:game.Grid):
    '''Check if anybody won in this case (wrapper for game_obj.evaluate())
    If true, proceed to terminal_calc, if not then return False'''
    thought=game_obj.evaluate()
    #print(thought)
    if thought==Names.ALICE.name or thought==Names.BOB.name or thought==True:
        #print("true lol,", thought==Names.ALICE, thought==Names.BOB)
        return True
    return False

def terminal_calc(game_obj:game.Grid):
    '''Wrapper for game_obj.evaulate() that should only be called if if_terminal returns True
    Returns the following values:
    1 - Alice won (evaluate() returns ALICE) 
    0 - Draw (only possible with a corresponding mode turned on, evaulate() returns True)
    -1 - Bob won (evaluate() returns BOB)'''
    thought=game_obj.evaluate()
    #print('thought:',thought)
    if thought==Names.ALICE.name:
        #print('alice test')
        return 1
    elif thought==Names.BOB.name:
        return -1
    else: #must be a draw, the function here shouldn't be called if the state isn't a terminal one
        return 0
    


def cut_off_evaluation(game_obj:game.Grid):
    '''This function should evaluate the current position of a field and return a score from -1 to 1 on how beneficial that position is'''
    global heuristics_called
    heuristics_called=True
    #idea: calculate a distance of both bob and alice towards their victories as of right now
    #equal distances = 0
    #advantageous positions should be on a scale 

    #assuming the game state is not terminal here
    
    #1. Calculate the number of moves till victory for Alice
    min_alice=inf
    for i in range(game_obj._x):
        calc=0
        for j in range(game_obj._y):
            if game_obj._grid[j][i]!=0:
                calc+=game_obj._grid[j][i]
        min_alice=min(calc,min_alice)
    #2. Do the same thing for Bob
    min_bob=inf
    for i in game_obj._grid:
        calc=0
        for j in i:
            if j!=0:
                calc+=j
        min_bob=min(calc,min_bob)
    #3. (Bob - Alice)/Column_Size
    #column_size=game_obj._y
    return (min_bob-min_alice)/game_obj._y

def minimax(game_obj:game.Grid,x,y,alpha=-inf,beta=inf,depth=inf,alice=True):
    '''Implementing a minimax algorithm here with a condition that whenever this function is called, Alice is the current player (aka the MAX player) and Bob is always a MIN player.
    '''
    #first up we need a way to evaluate whether the game is over or not and who won
    if if_terminal(game_obj): #we're getting our win/lose condition evaluation here
        #print('This state is terminal lol',x,y)
        return terminal_calc(game_obj)
    #not a terminal position
    #depth check
    if depth<=0:
        #print('outta depth')
        return cut_off_evaluation(game_obj) #returns a score of a current position

    #alice is always the maximizing player
    if alice:
        maxEval= -inf
        #call this function for each valid position in the field
        for i in range(game_obj._x):
            break_flag=False
            for j in range(game_obj._y):
                #copy the matrix
                future_game_obj=copy.deepcopy(game_obj)
                #apply a possible move to the next step of this procedure
                if future_game_obj.get_value(i+1,j+1)==0:
                    #cannot do anything here
                    continue
                future_game_obj.decrease(i+1,j+1)
                #recursive calls
                eval=minimax(future_game_obj,i+1,j+1,alpha,beta,depth-1,False)
                maxEval=max(eval,maxEval)
                alpha=max(alpha,eval)
                if beta <= alpha:
                    break_flag=True
                    break
            if break_flag:
                break
        return maxEval
    else: #evaulating bob
        minEval=inf
        for i in range(game_obj._x):
            break_flag=False
            for j in range(game_obj._y):
                future_game_obj=copy.deepcopy(game_obj)
                if future_game_obj.get_value(i+1,j+1)==0:
                    #cannot do anything here
                    continue
                future_game_obj.decrease(i+1,j+1)
                eval=minimax(future_game_obj,i+1,j+1,alpha,beta,depth-1,True)
                minEval=min(eval,minEval)
                beta=min(beta,eval)
                if beta<=alpha:
                    break_flag=True
                    break
            if break_flag:
                break
        return minEval

def alg_minimax(game_obj:game.Grid,depth=inf):
    '''minimax function wrapper for further integration into the code + iterative deepening work'''
    d=dict()
    #pass check
    if game_obj.pass_allowed:
        future_game_obj=copy.deepcopy(game_obj)
        d[(0,0)]=minimax(future_game_obj,0,0,depth=depth,alice=False)
    #iterate through the entire game field, calculate minimax values for each position, return the highest one possible
    for i in range(game_obj._x):
        for j in range(game_obj._y):
            #print('iteration',i,j)
            future_game_obj=copy.deepcopy(game_obj)
            if future_game_obj.get_value(i+1,j+1)==0:
                #cannot do anything here
                continue
            future_game_obj.decrease(i+1,j+1)
            d[(i+1,j+1)]=minimax(future_game_obj,i+1,j+1,depth=depth,alice=False)
            #print(d)
    #pick the highest value coordinate
    max_val=-inf
    final_x=0
    final_y=0
    for i in d.keys():
        if d[i]>max_val:
            max_val=d[i]
            final_x,final_y=i
    #depth not supported yet
    return (final_x,final_y) 

def alg_minimax_process(game_obj:game.Grid,best_coords:list):
    '''An iterative deepening thread that should be able to terminate whenever needed'''
    depth=0
    while True:
        copied_game_obj=copy.deepcopy(game_obj)
        global heuristics_called
        heuristics_called=False
        best_x,best_y=alg_minimax(copied_game_obj,depth)
        best_coords[0]=best_x #for mutability purposes
        best_coords[1]=best_y
        #print(depth,best_x,best_y)
        depth+=1
        if not heuristics_called:
            return None


def alg_minimax_timed(game_obj:game.Grid,decision_max_seconds):
    '''Wrapper of a wrapper of a minimax algorithm for the purposes of iterative deepening'''
    #Run alg_minimax in a loop with a timer
    seconds=decision_max_seconds

    t_end=time.time()+seconds
    depth=0
    best_x=0
    best_y=0
    #first call out of a thread
    global heuristics_called
    heuristics_called=False
    #print(depth)
    best_x,best_y=alg_minimax(game_obj,depth)
    depth+=1
    #time the next step
    manager=multiprocessing.Manager()
    best_coords=manager.list([best_x,best_y])
    #Iterate with the depth 0 1 2 3 etc
    t=multiprocessing.Process(target=alg_minimax_process,args=(game_obj,best_coords))
    t.start()
    #After a timer is over, return the last result of an algorithm
    t.join(seconds)
    if t.is_alive():
        t.terminate()
    
    best_x=best_coords[0]
    best_y=best_coords[1]
    #print('final:',best_x,best_y)
    return best_x,best_y


