# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:43:14 2024

@author: jim
"""
from walk_space import two_d_space
from scipy.stats import linregress
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import sys

iterations = 100
steps = 40
random.seed(10)
survivors = np.zeros(steps + 1)

# create the data frame for the results
df = pd.DataFrame(columns=['Index','Hit', 'Alive'])
walkspace = two_d_space(11,400)

for i in range(iterations):  
    for j in range(steps):
        direction = random.choice(["left","right"])
        # print(direction)
        result = walkspace.move_drunkard(direction)
        # print(result)
        if result[0] == "error":
            sys.exit()
        if result[0] == True: # True means run out of moves
            df.loc[i] = [i, 0, True]
        else:
            df.loc[i] = [i, j, False]

for index, row in df.iterrows():
    print(index, row)
    if row['Alive']:  # If survived till the end
        survivors += 1  # Increment survivor count for all steps
    else:  # If arrested, increment survivor count up to the 'hit at' step
        survivors[:int(row['Hit'])] += 1

# Calculate the number of survivors after each step
k_values = np.cumsum(survivors[::-1])[::-1]

# Remove steps with no survivors to avoid log(0)
n_steps = np.arange(steps + 1)
valid_steps = k_values > 0
n_steps = n_steps[valid_steps]
k_values = k_values[valid_steps]        
      
# Step 3: Plot the Data
log_k = np.log(k_values)
plt.figure(figsize=(10, 6))
plt.plot(n_steps, log_k, marker='o', linestyle='-', color='blue')
plt.title('Log of Survivors vs. Steps')
plt.xlabel('Number of Steps (n)')
plt.ylabel('Log of Survivors (log(k))')

# Linear regression to find the slope (-λ)
slope, intercept, r_value, p_value, std_err = linregress(n_steps, log_k)
plt.plot(n_steps, intercept + slope*n_steps, 'r', label=f'Linear Fit: slope={slope:.4f}')
plt.legend()

plt.show()

# The slope of the line is -λ, so λ is the negative of the slope
lambda_estimate = -slope
print(f'Estimated rate of arrest, λ: {lambda_estimate:.4f}')        
     
