import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Board:
    def __init__(self, size=10):
        self.size = size
        self.board = np.ones((size, size))
        self.anim = 0
        
    def fill_square(self, x, y):
        if 0 <= x < self.size and 0 <= y < self.size:
            self.board[y, x] = 0

    def init_board_display(self):
        self.fig, self.ax = plt.subplots()
        self.matshow = plt.matshow(self.board, cmap='gray', vmin=0, vmax=1, fignum=0)
        plt.gca().set_xticks(np.arange(-.5, self.size, 1), minor=True)
        plt.gca().set_yticks(np.arange(-.5, self.size, 1), minor=True)
        plt.grid(which="minor", color="black", linestyle='-', linewidth=2)
        plt.tick_params(which="minor", size=0)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
    def update_board_display(self, frame):
        x, y = np.random.randint(0, self.size, size=2)
        self.fill_square(x, y)
        self.matshow.set_data(self.board)
        return [self.matshow]

    def animate_board(self, frames=5, interval=100):
        self.init_board_display()
        self.anim = FuncAnimation(self.fig, self.update_board_display, frames=frames, interval=interval, blit=True)
        plt.show()

# Example usage
# board = Board(size=10)
# board.animate_board(frames=50, interval=20)  # Adjust frames and interval as needed
