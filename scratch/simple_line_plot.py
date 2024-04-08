# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define the function (for example, f(x) = x^2)
def f(x):
    return x ** 2

# Create a range of x-values
N = 10
x = np.linspace(-5, 5, 10)

# Compute corresponding y-value
times = np.arange(0,50)
y = np.linspace(0,len(times)-1,N,endpoint=True)

# Plot the data
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = x^2")
plt.grid(True)
plt.show()

print(x)
print(y)
