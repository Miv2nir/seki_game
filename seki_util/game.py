import random
from seki_util.names import Names
class Grid:
    def __init__(self,x=1,y=1,draw_allowed=False):
        self._x=x
        self._y=y
        self._grid = [[0 for col in range(x)] for row in range(y)]
        self.draw_allowed=draw_allowed #d-seki mode
    
    def set_grid(self,m):
        '''
        m is assumed to be a list of lists
        '''
        self._grid=m
        #TODO: Set appropriate coordinates to follow-up
        #calculating new dimensions
        self._x=len(m[0])
        self._y=len(m)
    def populate(self,low,high):
        '''
        Populates the matrix with random values >=0
        low - min value
        high - max value
        '''
        low=max(0,low)
        for i in range(self._y):
            for j in range(self._x):
                self._grid[i][j]=random.randint(low,high)
            #print(i)
    
    def print_grid(self):
        for i in self._grid:
            print(i)
        return None
    
    def decrease(self,x,y):
        '''
        As per the game's definition, decrease a value on the grid by 1
        x & y - values from 1 to the coordinate maximum
        '''
        #print('Decreasing (%s,%s):'%(x,y))
        self._grid[y-1][x-1]=max(self._grid[y-1][x-1]-1,0)
        return self
    
    def get_value(self,x,y):
        '''Returns a value on an (x,y) coordinate'''
        return self._grid[y-1][x-1]

    def get_grid(self):
        '''Returns the grid'''
        return self._grid

    def height(self):
        '''
        Calculates the sum of all elements in a matrix
        '''
        s=0
        for i in self._grid:
            for j in i:
                s+=j
        return s

    def evaluate(self,verbal=False):
        '''
        Check the condition of the field to see if anybody won
        '''
        bob_wins=False
        alice_wins=False
        draw_possible=self.draw_allowed
        #bob wins if a row is empty
        for i in self._grid:
            if i==([0]*self._x):
                bob_wins=True
                #if not draw_possible: #no draw means there's no point in continuing to search for the win condition, bob won
                #    print('Bob wins')
                #    return True
        #alice wins if a column is empty
        for i in range(self._x):
            check=True #assume the column is full of zeroes
            for j in range(self._y):
                if self._grid[j][i]!=0:
                    check=False #sike
                    break
            if check:
                alice_wins=True
        if draw_possible and alice_wins and bob_wins:
            if verbal:
                print('Draw!')
            return True
        elif bob_wins:
            if verbal:
                print('Bob wins!')
            return Names.BOB.name
        elif alice_wins:
            if verbal:
                print('Alice wins!')
            return Names.ALICE.name
        else:
            if verbal:
                print('nobody won')
            return False