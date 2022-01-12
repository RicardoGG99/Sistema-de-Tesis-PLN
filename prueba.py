from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.geometry("500x500")


def graph():
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']

    men_means = [20, 34, 30, 35, 27]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Men')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)

    fig.tight_layout()

    plt.show()


button = Button(root, text="Abrir Grafico", command=graph)
button.pack()

root.mainloop()
