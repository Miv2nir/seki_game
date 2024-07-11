from seki_util import game

def main():
    g=game.Grid(3,4)
    g.populate(0,10)
    g.print_grid()

if __name__ == '__main__':
    main()