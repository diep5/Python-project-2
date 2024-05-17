import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot8():
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Replace spaces in column names with underscores
    my_data.columns = my_data.columns.str.replace(' ', '_')

    # Create a line plot with seaborn
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=my_data, x='Age', y='Daily_Steps', hue='Gender', palette=["lightblue", "salmon"])

    # Add points to the line plot
    sns.scatterplot(data=my_data, x='Age', y='Daily_Steps', hue='Gender', palette=["lightblue", "salmon"], s=50)

    plt.title("Daily Steps: Trends by Age and Gender")
    plt.xlabel("Age")
    plt.ylabel("Daily Steps")
    plt.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.5)

    return g.fig
