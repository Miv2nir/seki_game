import random
from seki_util import game

def main():
    random.seed(10)

    g=game.Grid(3,3)
    #g.populate(0,10)
    desired_grid=[[2,2,0],[2,0,2],[0,2,2]]
    g.set_space(desired_grid)
    g.print_grid()
    g.decrease(1,1)
    print(g.height())

if __name__ == '__main__':
    main()