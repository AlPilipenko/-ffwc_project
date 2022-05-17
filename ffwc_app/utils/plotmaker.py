import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from .db_manips import data_extractor

colors = ['gold', 'magenta', 'green', 'brown', 'red', 'blue']


def create_pie_chart(weight, initial_weight, goal_weight):
    """Creates pie chart of group effort to lose weight
    versus already made progress. Responsive to changes."""
    lost_weight = initial_weight - weight
    lose_weight_diff = initial_weight - goal_weight
    left_to_lose = lose_weight_diff - lost_weight
    left_to_lose = left_to_lose if left_to_lose >= 0 else 0
    lables = ['Lost weight', 'Weight to lose']
    plt.pie([lost_weight, left_to_lose],
            colors=colors, shadow=True,
            wedgeprops={'edgecolor': 'black'},
            labels=lables, startangle=90,
            autopct='%1.1f%%')
    plt.title('Group effort progress')
    plt.grid(False)
    path = os.getcwd()
    file = '/ffwc_app/static/base/plots/pie_chart.png'
    file_path = path + file
    plt.savefig(file_path, bbox_inches='tight', transparent=True)
    plt.close('all')


def create_graph(dataset):
    """Creates a plot of challenge participants. The progress of each
    user is represented by unique color line. Responsive to changes.
    """
    x = []
    y = []
    users = []
    for user in dataset:
        user_data = dataset.get(user)
        date = user_data.get('Date')
        weight = user_data.get('Weight')
        users.append(user)
        tics = (len(date))
        x_steps = [c for c in range(1, tics+1)]
        x.append(x_steps)
        y.append(weight)

    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()
    fig = matplotlib.pyplot.gcf()
    ax.grid(False)

    counter = 0
    for name in users:
        color = colors[counter]
        plt.plot(x[counter], y[counter], label=name,
                                    linewidth=2.0, color=color)
        ax.set_xticks([])
        ax.set_ylabel('Weight (kg)')
        counter += 1

    plt.title('Individual progress')
    plt.legend()
    path = os.getcwd()
    file = '/ffwc_app/static/base/plots/graph_chart.png'
    file_path = path + file
    plt.savefig(file_path, bbox_inches='tight', transparent=True)
    plt.close('all')
