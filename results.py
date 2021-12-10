from tkinter import *
import tkinter as tk


def callResultPage(resultadosfacheritos):
    root = tk.Tk()
    main(root, resultadosfacheritos)
    root.mainloop()


def main(root, resultadosfacheritos):

    resultadosreales = []

    for i in resultadosfacheritos:
        print(i)
        resultadosreales.append(str(i))
        print(resultadosreales)

    canvas = Canvas(root, width=600, height=300)
    canvas.grid(columnspan=3, rowspan=3)

    canvas = Canvas(root, width=600, height=250)
    canvas.grid(columnspan=3)

    # label
    label = Label(
        root, text="Revisa tus Resultados", font="Arial", pady=20)
    label.grid(columnspan=3, column=0, row=0)
    label.place(anchor='n', relx=0.5)

    # HABILIDADES
    # input
    labelHabilidades = Label(
        root, text=resultadosreales[0] + " punto(s) ", font="Arial")
    labelHabilidades.place(x=420, y=90)
    # label
    label = Label(root, text="Habilidades: ", font="Arial")
    label.place(x=180, y=90)

    # PROGRAMACION WEB
    # input
    labelWeb = Label(
        root, text=resultadosreales[1] + " punto(s) ", font="Arial")
    labelWeb.place(x=420, y=170)

    # label
    label1 = Label(root, text="Programación Web: ", font="Arial")
    label1.place(x=180, y=170)

    # BASES DE DATOS
    # input
    labelBDD = Label(
        root, text=resultadosreales[2] + " punto(s) ", font="Arial")
    labelBDD.place(x=420, y=250)

    # label
    label2 = Label(root, text="Bases de Datos: ", font="Arial")
    label2.place(x=180, y=250)

    # PROGRAMACION GENERAL
    # input
    labelGeneral = Label(
        root, text=resultadosreales[3] + " punto(s) ", font="Arial")
    labelGeneral.place(x=420, y=330)

    # label
    label3 = Label(root, text="Programación General: ", font="Arial")
    label3.place(x=180, y=330)

    # CIENCIAS DE DATOS
    # input
    labelScience = Label(
        root, text=resultadosreales[4] + " punto(s) ", font="Arial")
    labelScience.place(x=420, y=410)

    # label
    label4 = Label(root, text="Ciencias de Datos: ", font="Arial")
    label4.place(x=180, y=410)

    # PROGRAMACION MOVIL
    # input
    labelMovil = Label(
        root, text=resultadosreales[5] + " punto(s) ", font="Arial")
    labelMovil.place(x=420, y=490)

    # label
    label5 = Label(root, text="Programación Móvil: ", font="Arial")
    label5.place(x=180, y=490)


# callResultPage(['1', '2', '3', '4', '5', '6'])
