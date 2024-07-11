import random
from seki_util import game,players

def main():
    random.seed(10)

    desired_grid=[[2,2,0],[2,0,2],[0,2,2]]
    g=game.Grid(3,3)
    #g.populate(0,10)
    g.set_space(desired_grid)
    g.print_grid()
    #init players
    bob=players.Player(players.Names.BOB)
    alice=players.Player(players.Names.ALICE)
    bob.move(g,1,1)
    alice.move(g,1,1)

    #g.print_grid()

if __name__ == '__main__':
    main()