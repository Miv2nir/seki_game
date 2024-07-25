import random
from seki_util import game,players,archive
from seki_util.names import Names

def option_picker_str(options:set):
    while True: #option selector
        option=str(input("Type an option: "))
        if option in options:
            return option
        print('Incorrect option specified.')

def option_picker_int(options:set):
    while True: #option selector
        option=int(input("Pick an option: "))
        if option in options:
            return option
        print('Incorrect option number specified.')


def runtime(bob,alice,presets):
    '''runtime for the CLI play'''
    print('Select an option:')
    print('1. Load a field preset')
    print('2. Define and randomly generate the game field')
    option1=option_picker_int({1,2})
    
    g=game.Grid()
    if option1==1: #picking a preset map
        print('Type the name of a desired preset.')
        print('Available presets are:')
        for i in presets:
            print("%s:"% i)
            g_temp=game.Grid()
            g_temp.set_grid(presets[i])
            g_temp.print_grid()
        g.set_grid(presets[option_picker_str(presets.keys())])
        
        
    elif option1==2: #generating a map
        x,y=map(int,input("Enter desired dimensions of a grid: ").split())
        print('Generating a grid of %s by %s...'%(x,y))
        g=game.Grid(x,y)
        #populate with random values
        low,high=map(int,input("Enter desired range of random variables: ").split())
        g.populate(low,high)
    g.print_grid()

    #time to play
    game_over=False
    while not game_over:
        #bob starts first
        bob_x,bob_y=map(int,input('Select a space to reduce a number in: ').split())
        #check for out of bounds selection
        if (bob_x>g._x) or (bob_y>g._y) or (0>bob_x) or (0>bob_y):
            print(g._x,g._y)
            print('Selection is Out of Bounds!')
            continue
        #check for selecting a zero
        if g.get_value(bob_x,bob_y)==0:
            print('Cannot select a Zero!')
            continue
        #continuing on
        bob.move(g,bob_x,bob_y,verbal=True)
        g.print_grid()
        game_over=alice.analyze(g,move=True,verbal=True)
        


#main function starts here
def main():

    random.seed(10)
    #predefined presets for convenience
    presets={
        'cascade':[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
        'doc':[[2,2,0],[2,0,2],[0,2,2]],
        'even':[[1,1,1],[1,1,1],[1,1,1]]
    }
    #init players
    bob=players.Player(players.Names.BOB)
    alice=players.Player(players.Names.ALICE)

    #runtime for the CLI play
    runtime(bob,alice,presets)
    
    #archive.copy_test(bob,alice)




if __name__ == '__main__':
    main()