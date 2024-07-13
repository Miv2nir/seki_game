import random

class Grid:
    def __init__(self,x,y,draw_allowed=False):
        self.x=x
        self.y=y
        self.space = [[0 for col in range(x)] for row in range(y)]
        self.draw_allowed=draw_allowed #d-seki mode
    
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
            #print(i)
    
    def print_grid(self):
        for i in self.space:
            print(i)
        return None
    
    def decrease(self,x,y):
        '''
        As per the game's definition, decrease a value on the grid by 1
        x & y - values from 1 to the coordinate maximum
        '''
        #print('Decreasing (%s,%s):'%(x,y))
        self.space[y-1][x-1]=max(self.space[y-1][x-1]-1,0)
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

    def evaluate(self):
        '''
        Check the condition of the field to see if anybody won
        '''
        bob_wins=False
        alice_wins=False
        draw_possible=self.draw_allowed
        #bob wins if a row is empty
        for i in self.space:
            if i==([0]*self.x):
                bob_wins=True
                #if not draw_possible: #no draw means there's no point in continuing to search for the win condition, bob won
                #    print('Bob wins')
                #    return True
        #alice wins if a column is empty
        for i in range(self.x):
            check=True #assume the column is full of zeroes
            for j in range(self.y):
                if self.space[j][i]!=0:
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