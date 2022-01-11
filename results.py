from tkinter import *
import tkinter as tk


def callResultsPage(allScores, jobScores):
    root = tk.Tk()
    main(root, allScores, jobScores)
    root.mainloop()


def main(root, allScores, jobScores):

    print("all: ", allScores)
    print("job: ", jobScores)

    canvas = Canvas(root, width=600, height=300)
    canvas.grid(columnspan=3, rowspan=3)

    canvas = Canvas(root, width=600, height=250)
    canvas.grid(columnspan=3)

    # label
    label = Label(
        root, text="Revisa tus Resultados", font="Arial", pady=20)
    label.grid(columnspan=3, column=0, row=0)
    label.place(anchor='n', relx=0.5)

    newJobScore = []

    for scoreporfabor in jobScores:
        newJobScore.append(scoreporfabor)

    for scorex in allScores:
        i = 0
        for scoreVerga in jobScores:
            #print("esta es la iteracion numero: ", i)
            # print(jobScores[i])
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
