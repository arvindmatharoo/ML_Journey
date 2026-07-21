import matplotlib.pyplot as plt
import numpy as np

# Create a figure with a specific size
fig = plt.figure(figsize=(10, 6))

# Add a subplot to the figure
ax = fig.add_subplot(1, 1, 1)  # 1 row, 1 column, 1st plot

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot data on the subplot
ax.plot(x, y, label='Sine Wave', color='purple')

# Add labels and a title
ax.set_title('Figure with a Single Subplot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Add a legend
ax.legend()

# Show the figure
plt.show()
