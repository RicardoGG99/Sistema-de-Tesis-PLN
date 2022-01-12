import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import tkinter as tk


def callResultsPage(allScores, jobScores):
    root = tk.Tk()
    main(root, allScores, jobScores)
    root.mainloop()


scoresPorcentaje = []


def main(root, allScores, jobScores):

    print("all: ", allScores)
    print("job: ", jobScores)

    newJobScore = []

    for scoreporfabor in jobScores:
        newJobScore.append(scoreporfabor)

    for scorex in allScores:
        i = 0
        for aux in jobScores:
            if jobScores[i] == 0:
                scorex[i] = 0
                newJobScore[i] = 1
            i += 1
        print(scorex)
    print(jobScores)
    print(newJobScore)
    for scorex in allScores:
        arraysUnidos = zip(scorex, newJobScore)
        result = [(x/y)*100 for x, y in arraysUnidos]
        print(result)
        scoresPorcentaje.append(result)

    elmejor = zip(allScores)
    result = [()]
    print(scoresPorcentaje)

    # lo que estaba en huevo
    root.geometry("500x500")

    z = 0

    def graph(values):
        labels = ['Hab', 'Web', 'BDD',
                  'Prog', 'Ciencia DD', 'Movil', 'MAX']

        values.append(100)

        x = np.arange(len(labels))
        width = 0.35

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, values, width, label='CV')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('% de Afinidad')
        ax.set_title('Afinidad de Postulante por Categoria')
        ax.set_xticks(x, labels)
        ax.set_xlabel('Categorias')
        ax.legend()

        ax.bar_label(rects1, padding=3)

        fig.set_size_inches(9, 6)
        fig.tight_layout()

        plt.show()

    for score in scoresPorcentaje:
        # button = Button(root, text="Abrir Grafico", command=graphAux)
        # button.pack()
        graph(score)
