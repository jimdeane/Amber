# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:58:37 2024

@author: jim
"""
import numpy as np
import sys
import random
class two_d_space_walker:
    def __init__(self, size, max_moves):
        self.size = ( size)
        self.max_position = 5
        self.min_position = -5
        self.max_moves = max_moves
        self.space = np.zeros((1, size))
        self.current_position = 0
        self.moves = 0
        
    def get_current_position(self):
        return self.current_position
    
    def move_drunkard(self, moves, random_function ):
        for j in range(1,moves+1):                    
                
            
            direction = random_function()
            
            match direction:
                case "left":
                    self.current_position = self.current_position - 1
                    
                case "right":
                    self.current_position = self.current_position + 1
                    
                case _:
                    print("illegal direction -" , direction)
                    return ("error", direction)
            print(self.current_position)
            if self.is_arrested(self.current_position):
                return (True, j) # drunk arrested 
            self.moves += 1
        return (False, j ) # after all the permissable moves
                                   # walker ahd not been arrested  
               
    def is_arrested(self, position):
        if self.min_position < position < self.max_position:
            return False
        else:
            return True