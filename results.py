import matplotlib.pyplot as plt
import numpy as np
from tkinter import *


def callResultsPage(allScores, jobScores):

    main(allScores, jobScores)


scoresPorcentaje = []


def main(allScores, jobScores):

    newJobScore = []

    for jobScoresX in jobScores:
        newJobScore.append(jobScoresX)

    for scorex in allScores:
        i = 0
        for aux in jobScores:
            if jobScores[i] == 0:
                scorex[i] = 0
                newJobScore[i] = 1
            i += 1
    for scorex in allScores:
        arraysUnidos = zip(scorex, newJobScore)
        result = [(x/y)*100 for x, y in arraysUnidos]
        z = 0
        for valor in result:
            if valor > 100:
                result[z] = 100
            z += 1
        scoresPorcentaje.append(result)

    print(scoresPorcentaje)

    def graph(values):
        labels = ['Hab', 'Web', 'BDD',
                  'Prog', 'Ciencia DD', 'Movil', 'MAX']

        values.append(100)

        x = np.arange(len(labels))
        width = 0.35

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, values, width, label='CV')

        ax.set_ylabel('% de Afinidad')
        ax.set_title('Afinidad de Postulante por Categoria')
        ax.set_xticks(x, labels)
        ax.set_xlabel('Categorías')
        ax.legend()

        ax.bar_label(rects1, padding=3)

        fig.set_size_inches(9, 6)
        fig.tight_layout()

        plt.show()

    for score in scoresPorcentaje:
        graph(score)
