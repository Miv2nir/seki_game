from seki_util import game,players
#this module is only used to store 'test' functions that i ran before while testing the algoritms and everything

def game_1(bob,alice): #test game
    desired_grid=[[2,2,0],[2,0,2],[0,2,2]]
    g=game.Grid(3,3)
    #g.populate(0,10)
    g.set_grid(desired_grid)
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

def game_5(bob,alice): #alg test
    desired_grid=[[1,2,3],[4,5,6],[7,8,9]]
    g=game.Grid(3,3)
    #g.populate(0,10)
    g.set_grid(desired_grid)
    g.print_grid()
    bob.move(g,1,1)
    alice.analyze(g)
    bob.move(g,2,1)
    alice.analyze(g)
    bob.move(g,2,1)
    alice.analyze(g)
    bob.move(g,3,1)