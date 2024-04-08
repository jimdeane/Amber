# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:37:51 2024

@author: jim
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
frame_count = 10
background_size = 20
circle_radius = 1  # For a 2-pixel diameter

# Create a figure and a single subplot
fig, ax = plt.subplots()

# Set limits for the axes
ax.set_xlim(0, background_size)
ax.set_ylim(0, background_size)
ax.set_aspect('equal')  # Ensure the aspect ratio is square

# Remove axes for clarity
ax.axis('off')

def plot_circle(frame):
    ax.clear()  # Clear the previous circle
    ax.set_xlim(0, background_size)
    ax.set_ylim(0, background_size)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Generate random center within the limits, accounting for the circle's radius
    x = np.random.uniform(circle_radius, background_size - circle_radius)
    y = np.random.uniform(circle_radius, background_size - circle_radius)
    
    # Create a circle at the random location
    circle = plt.Circle((x, y), circle_radius, color='blue')
    ax.add_patch(circle)

# Create animation
anim = FuncAnimation(fig, plot_circle, frames=frame_count, repeat=False)

# To display the animation in a Jupyter notebook, use the following:
# from IPython.display import HTML
# HTML(anim.to_jshtml())

# To save the animation as a GIF file
anim.save('/mnt/data/random_circles.gif', writer='imagemagick', fps=1)

print("Animation saved as 'random_circles.gif'.")
