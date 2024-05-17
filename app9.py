import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot9():
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Replace spaces in column names with underscores
    my_data.columns = my_data.columns.str.replace(' ', '_')

    # Create a violin plot with seaborn
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=my_data, x='Gender', y='Daily_Steps', palette=["lightblue", "salmon"], linewidth=1)

    plt.title("Daily Steps Distribution by Gender: A Look at the Violin Plot")
    plt.xlabel("Gender")
    plt.ylabel("Daily Steps")
    plt.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.5)
    plt.show()
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd

    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Replace spaces in column names with underscores
    my_data.columns = my_data.columns.str.replace(' ', '_')

    # Create a violin plot with seaborn
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=my_data, x='Gender', y='Daily_Steps', palette=["lightblue", "salmon"], linewidth=1)

    plt.title("Daily Steps Distribution by Gender: A Look at the Violin Plot")
    plt.xlabel("Gender")
    plt.ylabel("Daily Steps")
    plt.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.5)

    return g.fig
