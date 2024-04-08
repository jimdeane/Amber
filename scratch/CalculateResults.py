# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 18:18:45 2024

@author: jim
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Step 1: Read the Excel file
file_path = 'Results.xlsx'
df = pd.read_excel(file_path)

# Assuming 'True' in 'Left Alive' means survived till the end (400 steps)
# and 'Hit at' contains the step number they were arrested

# Step 2: Process the Data to find survivors after each step
# Initialize an array to hold the count of survivors after each step
max_steps = 400
survivors = np.zeros(max_steps + 1)  # +1 to include step 0

for index, row in df.iterrows():
    if row['Left Alive']:  # If survived till the end
        survivors += 1  # Increment survivor count for all steps
    else:  # If arrested, increment survivor count up to the 'hit at' step
        survivors[:int(row['Hit at'])] += 1

# Calculate the number of survivors after each step
k_values = np.cumsum(survivors[::-1])[::-1]

# Remove steps with no survivors to avoid log(0)
n_steps = np.arange(max_steps + 1)
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
