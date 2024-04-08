# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:58:37 2024

@author: jim
"""
import numpy as np

class two_d_space:
    def __init__(self, size, max_moves):
        self.size = ( size)
        self.max_moves = max_moves
        self.space = np.zeros((1, size))
        self.current_position = 0
        self.moves = 0
        
    def get_current_position(self):
        return self.current_position
    
    def move_drunkard(self, direction):
        self.moves +=1
        match direction:
            case "left":
                self.current_position = self.current_position - 1
                
            case "right":
                self.current_position = self.current_position + 1
                
            case _:
                print("illegal direction -" , direction)
                return ("error",direction)
         
        if self.moves >= self.max_moves:
            return ( True, self.current_position)
        
        return (False,self.current_position )      
               
                