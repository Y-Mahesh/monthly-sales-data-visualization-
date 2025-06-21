import pandas as pd
import matplotlib.pyplot as plt

# Create sample sales data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [15000, 18000, 12000, 22000, 20000, 25000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Show the DataFrame (optional)
print("Monthly Sales Data:")
print(df)

# Plot the data
plt.figure(figsize=(8, 5))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='green')
plt.title('Monthly Sales Overview')
plt.xlabel('Month')
plt.ylabel('Sales (INR)')
plt.grid(True)
plt.tight_layout()
plt.show()
