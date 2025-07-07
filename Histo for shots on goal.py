import matplotlib.pyplot as plt
import pandas as pd

# Your data
data = {
    'Team': ['Mustang', 'Mustang', 'Vipers', 'Mustang', 'Mustang', 'Mustang', 'Mustang', 'Mustang', 'Mustang', 'Mustang', 'Mustang', 'Vipers', 'Mustang', 'Mustang', 'Mustang', 'Vipers', 'Vipers', 'Vipers', 'Vipers', 'Mustang', 'Vipers', 'Vipers', 'Mustang', 'Vipers', 'Vipers', 'Mustang', 'Mustang', 'Vipers'],
    'Total_Sec': [569, 724, 747, 817, 918, 968, 1040, 1107, 1179, 1381, 1416, 1457, 1640, 1729, 1947, 2192, 2261, 2285, 2418, 2723, 2814, 3091, 3111, 3223, 3267, 3409, 3449, 3683]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create subsets for each team
mustang_data = df[df['Team'] == 'Mustang']['Total_Sec']
vipers_data = df[df['Team'] == 'Vipers']['Total_Sec']

# Plotting the histograms for both teams
plt.hist(mustang_data, bins=120, alpha=0.5, label='Mustang', edgecolor='black')
plt.hist(vipers_data, bins=120, alpha=0.5, label='Vipers', edgecolor='black')

plt.title('Histogram of Total Sec for Mustang and Vipers')
plt.xlabel('Total Sec')
plt.ylabel('Frequency')
plt.legend()
plt.show()
