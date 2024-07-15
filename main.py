import random
from seki_util import game,players,archive

def option_picker(options:set):
    while True: #option selector
        option=int(input("Pick an option: "))
        if option in options:
            return option
        print('Incorrect option number specified.')


def runtime(bob,alice):
    '''runtime for the CLI play'''
    print('Select an option:')
    print('1. Load a field preset')
    print('2. Define and randomly generate the game field')
    option1=option_picker({1,2})
    
    if option1==1: #picking a preset map
        print('Type the name of a desired preset.')
        print('Available presets are:')
        for i in presets:
            print("%s ->"% i)
            g_temp=game.Grid().set_grid(presets[i])
            g_temp.print_grid()
        


        


    elif option1==2: #generating a map
        x,y=map(int,input("Enter desired dimensions of a grid: ").split())
        print('Generating a grid of %s by %s:3'%(x,y))
        g=game.Grid(x,y)
        g.print_grid()

#main function starts here
def main():

    random.seed(10)
    #predefined presets for convenience
    presets={
        'cascade':[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
        'doc':[[2,2,0],[2,0,2],[0,2,2]]
    }
    #init players
    bob=players.Player(players.Names.BOB)
    alice=players.Player(players.Names.ALICE)

    #runtime for the CLI play
    g=game.Grid()
    g.set_grid(presets['cascade'])
    g.print_grid()
    print(g._x,g._y)
    


if __name__ == '__main__':
    main()