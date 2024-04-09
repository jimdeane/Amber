# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:43:14 2024

@author: jim
"""

from production_random import production_random
from walk_space import two_d_space_walker
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


iterations = 1000
steps = 400

survivors = np.zeros(steps + 1)

# create the data frame for the results
df = pd.DataFrame(columns=['Index','Moves', 'Arrested'])
for i in range(iterations): # trying just one simulation
        walker = two_d_space_walker(11,steps) # 11 means j=5` 400 is the number of steps to survive to be counted`
        simulation = walker.move_drunkard(steps, production_random) # test 40 moves
        print(i, simulation)
df.loc[i] = [i,simulation[1],simulation[0]]  # Adding a new row at the end
print(df)

for index, row in df.iterrows():
    if row['Arrested']:  # If survived till the end
        survivors[:int(row['Moves'])] += 1
    else:  # If arrested, increment survivor count up to the 'hit at' step
        
        survivors += 1  # Increment survivor count for all steps

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
     
