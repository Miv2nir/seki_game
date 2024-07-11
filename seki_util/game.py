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