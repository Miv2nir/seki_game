from seki_util import game
from enum import IntEnum

class Names(IntEnum):
    BOB=0 #player
    ALICE=1 #bot

class Player:
    def __init__(self,name:Names):
        self.name=name
    
    def evaluate(self,game_obj:game.Grid):
        '''
        Check the condition of the field to see if anybody won
        '''
        bob_wins=False
        alice_wins=False
        draw_possible=game_obj.draw_allowed
        #bob wins if a row is empty
        for i in game_obj.space:
            if i==([0]*game_obj.x):
                bob_wins=True
                #if not draw_possible: #no draw means there's no point in continuing to search for the win condition, bob won
                #    print('Bob wins')
                #    return True
        #alice wins if a column is empty
        for i in range(game_obj.x):
            check=True #assume the column is full of zeroes
            for j in range(game_obj.y):
                if game_obj.space[j][i]!=0:
                    check=False #sike
                    break
            if check:
                alice_wins=True
        if draw_possible and alice_wins and bob_wins:
            print('Draw!')
            return True
        elif bob_wins:
            print('Bob wins!')
            return True
        elif alice_wins:
            print('Alice wins!')
            return True
        else:
            print('nobody won')
            return False

    def move(self,game_obj:game.Grid,x,y):
        print(self.name.name,'decreases (%s,%s)'%(x,y))
        game_obj.decrease(x,y)
        self.evaluate(game_obj)
        return game_obj