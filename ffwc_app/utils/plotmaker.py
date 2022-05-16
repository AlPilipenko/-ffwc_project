import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from .db_manips import data_extractor

colors = ['gold', 'magenta', 'green', 'brown', 'red', 'blue']


def create_pie_chart(weight, initial_weight, goal_weight):
    plt.pie([initial_weight - weight, initial_weight - goal_weight],
            colors=colors, shadow=True,
            wedgeprops={'edgecolor': 'black'})
    print("OOOOOOOOOOOOOOOOOOO",initial_weight - weight, initial_weight - goal_weight )
     # labels='chart',

     #     , textprops='textprops')
    plt.grid(False)

    path = os.getcwd()
    file = '/ffwc_app/static/base/plots/pie_chart.png'
    file_path = path + file
    plt.savefig(file_path, bbox_inches='tight', transparent=True)



def create_graph(dataset):

    x = []
    y = []
    users = []
    for user in dataset:
        print(user)
        user_data = dataset.get(user)
        # print(user_data)
        # for entry in user_data:
        #     print(entry)
        date = user_data.get('Date')
        weight = user_data.get('Weight')
        users.append(user)
        tics = (len(date))
        x_steps = [c for c in range(1, tics+1)]
        x.append(x_steps)
        y.append(weight)

    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()
    ax.grid(False)

    # x_steps = (len(x) ) * len(users)+1
    # x = [c for c in range(1, x_steps)]
    # print()
    color_counter = 0
    print("!!!!!!!!!!!!!!!!!!!!!!!!!", x,y)
    for name in users:
        # counter = 0
        color = colors[color_counter]
        for tick, weight in zip(x, y):
            print(tick, weight)
            print("!!!!!!!!!!!!!!!!!!!!!!!!!", color)
            ax.plot(tick, weight, label="Line",
                                    linewidth=2.0, color=color)
            # counter += 1
        color_counter += 1



    # fig, ax = plt.subplots(figsize=(6, 6))


    # ax.plot(x[0], y[0], label="Line", linewidth=2.0, color='blue')
    # return graph_plot


    path = os.getcwd()
    file = '/ffwc_app/static/base/plots/graph_chart.png'
    file_path = path + file
    plt.savefig(file_path, bbox_inches='tight', transparent=True)


    # plot_instance = Plots()
    # plot_instance.plot_name = name
    # plot_instance.plot = 'aggregator/plots/' + name
    # plot_instance.save()

    plt.close('all')
