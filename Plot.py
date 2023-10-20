import seaborn as sns
import matplotlib.pyplot as plt

def get_plot(data):
    sns_plot = sns.scatterplot(x='Timestamp', y='Temp1', data=data)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot Example')

    mpl_plot = plt.gcf()
    return mpl_plot