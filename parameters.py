from tkinter import *


def callParametersPage():
    root = Tk()
    main(root)
    root.mainloop()


def main(root):

    canvas = Canvas(root, width=600, height=650)
    canvas.grid(columnspan=3, rowspan=3)

    # label
    label = Label(
        root, text="Selecciona el nivel de importancia de 0-5", font="Arial", pady=20)
    label.grid(columnspan=3, column=0, row=0)
    label.place(anchor='n', relx=0.5)

    # HABILIDADES
    # input
    scale = Scale(root, from_=0, to=5, orient=HORIZONTAL)
    scale.place(x=420, y=90)
    # label
    label = Label(root, text="Habilidades: ", font="Arial")
    label.place(x=180, y=90)

    # PROGRAMACION WEB
    # input
    scale1 = Scale(root, from_=0, to=5, orient=HORIZONTAL)
    scale1.place(x=420, y=170)

    # label
    label1 = Label(root, text="Programación Web: ", font="Arial")
    label1.place(x=180, y=170)

    # BASES DE DATOS
    # input
    scale2 = Scale(root, from_=0, to=5, orient=HORIZONTAL)
    scale2.place(x=420, y=250)

    # label
    label2 = Label(root, text="Bases de Datos: ", font="Arial")
    label2.place(x=180, y=250)

    # PROGRAMACION GENERAL
    # input
    scale3 = Scale(root, from_=0, to=5, orient=HORIZONTAL)
    scale3.place(x=420, y=330)

    # label
    label3 = Label(root, text="Programación General: ", font="Arial")
    label3.place(x=180, y=330)

    # CIENCIAS DE DATOS
    # input
    scale4 = Scale(root, from_=0, to=5, orient=HORIZONTAL)
    scale4.place(x=420, y=410)

    # label
    label4 = Label(root, text="Ciencias de Datos: ", font="Arial")
    label4.place(x=180, y=410)

    # PROGRAMACION MOVIL
    # input
    scale5 = Scale(root, from_=0, to=5, orient=HORIZONTAL)
    scale5.place(x=420, y=490)

    # label
    label5 = Label(root, text="Programación Móvil: ", font="Arial")
    label5.place(x=180, y=490)

    buttonText = StringVar()
    submit = Button(root, textvariable=buttonText, font="Raleway",
                    bg='#20bebe', fg="white", width=15, height=1, command=lambda: submit())
    buttonText.set("Enviar Resultados")

    submit.grid(column=1, row=2)
    submit.place(x=250, y=570)

    def submit():
        print(scale.get())
        print(scale1.get())
        print(scale2.get())
        print(scale3.get())
        print(scale4.get())
        print(scale5.get())
