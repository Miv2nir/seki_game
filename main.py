import random
from seki_util import game,players

#below is a collection of game runs that im doing for testing purposes

def game_1(bob,alice): #test game
    desired_grid=[[2,2,0],[2,0,2],[0,2,2]]
    g=game.Grid(3,3)
    #g.populate(0,10)
    g.set_space(desired_grid)
    g.print_grid()
    bob.move(g,1,1)
    alice.move(g,1,1)

def game_2(bob,alice): #alice wins
    g=game.Grid(4,3)
    g.populate(0,3)
    g.print_grid()
    bob.move(g,1,3)
    alice.move(g,1,2)

def game_3(bob,alice): #bob wins
    g=game.Grid(4,3)
    g.populate(1,1)
    g.print_grid()
    bob.move(g,1,1)
    alice.move(g,2,1)
    bob.move(g,3,1)
    alice.move(g,4,1)

def game_4(bob,alice): #draw test
    g=game.Grid(2,2)
    g.draw_allowed=True
    g.populate(0,0)
    g.print_grid()
    bob.move(g,1,1)

#main function starts here
def main():
    random.seed(10)

    #init players
    bob=players.Player(players.Names.BOB)
    alice=players.Player(players.Names.ALICE)

    #generate the game object and the grid here
    game_4(bob,alice)


if __name__ == '__main__':
    main()