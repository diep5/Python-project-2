import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot10():
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Replace spaces in column names with underscores
    my_data.columns = my_data.columns.str.replace(' ', '_')

    # Create a scatter plot with seaborn
    plt.figure(figsize=(10, 6))
    scatter = sns.scatterplot(data=my_data, x='Age', y='Occupation', size='Stress_Level', hue='Gender', 
                          sizes=(30, 300), alpha=0.25, palette=["darkblue", "darkred"])

    plt.title("Stress Level by Occupation and Age")
    plt.xlabel("Age")
    plt.ylabel("Occupation")
    scatter.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1)
    plt.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.7)

    return g.fig
