 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Board:
    def __init__(self, size=10):
        self.size = size
        self.board = np.ones((size, size))
        self.anim = 0
        
    def fill_square(self, x, y):
        #if 0 <= x-5 < self.size and 0 <= y-5 < self.size:
        self.board[y-6, x-6] = 0

    def init_board_display(self):
        self.fig, self.ax = plt.subplots()
        self.matshow = plt.matshow(self.board, cmap='gray', vmin=0, vmax=1, fignum=0)
        plt.gca().set_xticks(np.arange(-.5, self.size, 1), minor=True)
        plt.gca().set_yticks(np.arange(-.5, self.size, 1), minor=True)
        plt.grid(which="minor", color="black", linestyle='-', linewidth=2)
        plt.tick_params(which="minor", size=0)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
        for x in range(self.size):
            for y in range(self.size):
                self.ax.text( x, y , f'{x-5},{ y-5}', ha='center', va='center')
    def update_board_display(self, frame):
        # x, y = np.random.randint(0, self.size, size=2)
        
        #self.fill_square(x, y)
        self.matshow.set_data(self.board)
        return [self.matshow]

    def animate_board(self, frames=5, interval=100):
        # board.fill_square(0,0)
        # board.fill_square(0,1)
        # board.fill_square(1,1) 
        # board.fill_square(2,1)
        # board.fill_square(3,1)
        # board.fill_square(3,2)
        # board.fill_square(4,2)
        # board.fill_square(5,2)
        self.init_board_display()
        # self.anim = FuncAnimation(self.fig, self.update_board_display, frames=frames, interval=interval, blit=True)
        plt.show()
    
    def showBoard(self):
        plt.show()
        
        
board = Board(size=11)
board.animate_board(frames=50, interval=20)  # Adjust frames and interval as needed