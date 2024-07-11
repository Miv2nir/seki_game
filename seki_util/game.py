import random

class Grid:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.space = [[0 for col in range(x)] for row in range(y)]
    
    def set_space(self,m):
        '''
        m is assumed to be a list of lists
        '''
        self.space=m
    def populate(self,low,high):
        '''
        Populates the matrix with random values >=0
        low - min value
        high - max value
        '''
        low=max(0,low)
        for i in range(self.y):
            for j in range(self.x):
                self.space[i][j]=random.randint(low,high)
            print(i)
    
    def print_grid(self):
        for i in self.space:
            print(i)
        return None
    
    def decrease(self,x,y):
        '''
        As per the game's definition, decrease a value on the grid by 1
        x & y - values from 1 to the coordinate maximum
        '''
        print('Decreasing (%s,%s):'%(x,y))
        self.space[x-1][y-1]=max(self.space[x-1][y-1]-1,0)
        return self.print_grid()

    def height(self):
        '''
        Calculates the sum of all elements in a matrix
        '''
        s=0
        for i in self.space:
            for j in i:
                s+=j
        return s