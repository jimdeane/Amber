import matplotlib.pyplot as plt
import numpy as np

# Create a 10x10 board
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(0, 11, 1))

# Drawing the grid lines
ax.grid(which='both', color='black', linestyle='-', linewidth=2)

# Removing the axis labels
ax.set_xticklabels([])
ax.set_yticklabels([])

# Adding the coordinates
for x in range(10):
    for y in range(10):
        ax.text(x + 0.5, y + 0.5, f'{x},{y}', ha='center', va='center', fontweight='bold')

plt.show()
