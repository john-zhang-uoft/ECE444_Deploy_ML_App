import pandas as pd
import matplotlib.pyplot as plt

# Load the latency results from the CSV file
data = pd.read_csv('latency_results.csv')

# Generate a boxplot for each test case
plt.figure(figsize=(10, 6))
data.boxplot(column='Latency (seconds)', by='Test Case')
plt.title('API Latency per Test Case')
plt.suptitle('')  # Suppresses the default title to clean up the plot
plt.xlabel('Test Case')
plt.ylabel('Latency (seconds)')
plt.show()

# Calculate and print the average latency per test case
average_latency = data.groupby('Test Case')['Latency (seconds)'].mean()
print("Average Latency per Test Case:\n", average_latency)