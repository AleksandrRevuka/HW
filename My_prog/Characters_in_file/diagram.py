import matplotlib as mpl
import matplotlib.pyplot as plt


def make_diagram(data_names, data_values):
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(1000 / dpi, 800 / dpi))
    mpl.rcParams.update({'font.size': 10})
    plt.title('OpenStreetMap Point Types')
    ax = plt
    ax.grid()
    xs = range(len(data_names))
    plt.bar(xs, data_values, width=0.8, color='blue', alpha=0.7, zorder=2, edgecolor='black', linewidth=2)
    plt.xticks(xs, data_names)
    fig.autofmt_xdate(rotation=25)
    plt.show()

