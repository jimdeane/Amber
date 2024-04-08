# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:38:22 2024

@author: jim
"""
import pandas as pd
from walk_space import two_d_space
import sys
import random

def test_space_gets_set_up_with_postion_at_centre():
    space = two_d_space(11,400)
    assert space.get_current_position() == 0 
    
def test_moving_left_takes_us_to_J_equals_minus_1():
    space = two_d_space(11,400)
    result = space.move_drunkard("left")
       
    assert  space.get_current_position() == -1
    assert result == (False, -1)
    
def test_run_out_of_moves_after_400():
    space = two_d_space(11,400)
    for i in range(400):
       j = i % 2
       if j == 0:
           result = space.move_drunkard("left")
       else:
           result = space.move_drunkard("right")
       
    assert result == (True, 0)
    
def test_incorrect_direction_gives_eeror():
    space = two_d_space(11,400)
    result = space.move_drunkard("wrong direction")
    assert result == ("error", "wrong direction")

def test_something():
    df = pd.DataFrame(columns=['Index','Hit', 'Alive'])
    space = two_d_space(11,40)
    for i in range(100):
        space.moves = 0
        for j in range(40):
            direction = random.choice(["left","right"])
            print(direction)
            result = space.move_drunkard(direction)
            print(result)
            if result[0] == "error":
                sys.exit()
            if result[0] == True: # True means run out of moves
                df.loc[i] = [i, 0, True]
            else:
                df.loc[i] = [i, j, False]
    print(df)
    assert True