# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:00:22 2024

@author: jim
"""

 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class space:
    def __init__(self, size=11):
        self.size = ( size)
        self.space = np.ones((1, size))
        self.anim = 0
        
    def fill_square(self, J):
        #if 0 <= J-5 < self.size and 0 <= y-5 < self.size:
        self.space[0, J-6] = 0

    def init_space_display(self):
        self.fig, self.ax = plt.subplots()
        self.matshow = plt.matshow(self.space, cmap='gray', vmin=0, vmax=1, fignum=0)
        plt.gca().set_xticks(np.arange(-.5, self.size, 1), minor=True)
        plt.gca().set_yticks(np.arange(-.5, 1, 1), minor=True)
        plt.grid(which="minor", color="black", linestyle='-', linewidth=2)
        plt.tick_params(which="minor", size=0)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
        for J in range(self.size):
            self.ax.text( J,0,  f'{J-5}', ha='center', va='center')
            
    def update_space_display(self, frame):
        # J, y = np.random.randint(0, self.size, size=2)
        
        #self.fill_square(J, y)
        self.matshow.set_data(self.space)
        return [self.matshow]

    def animate_space(self, frames=5, interval=100):
        space.fill_square(0)
        space.fill_square(1)
        # space.fill_square(1,1) 
        # space.fill_square(2,1)
        # space.fill_square(3,1)
        # space.fill_square(3,2)
        # space.fill_square(4,2)
        # space.fill_square(5,2)
        self.init_space_display()
        # self.anim = FuncAnimation(self.fig, self.update_space_display, frames=frames, interval=interval, blit=True)
        plt.show()
    
    def showspace(self):
        plt.show()
        
        
space = space(size=11)
space.animate_space(frames=50, interval=20)  # Adjust frames and interval as needed