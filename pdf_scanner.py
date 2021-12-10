from tkinter import *
from tkinter.filedialog import askopenfile
import tkinter as tk
from PIL import Image, ImageTk
import pdfminer.high_level as miner
import string
import pandas as pd


root = tk.Tk()
content = ''
summary = pd.DataFrame()

terms = {'Habilidades Generales': ['ingles', 'frances', 'aleman', 'orden', 'ordenes', 'obediente', 'liderazgo', 'lider', 'puntual', 'responsable', 'cooperativo', 'cooperacion', 'creativo', 'creatividad', 'proactivo', 'proactividad', 'excelencia', 'perfeccionista', 'perfeccion', 'aprendizaje', 'aprender', 'actitud', 'aptitud', 'aptitudes', 'eficiente', 'eficiencia', 'competencia', 'competencias', 'competente', 'eficaz', 'linux', 'mac', 'macos', 'windows', 'powershell', 'terminal'],
         'Programacion Web': ['javascript', 'java', 'python', 'flask', 'html', 'angular', 'angular', 'vue', 'vue', 'react', 'react', 'css', 'objective c', 'perl', 'php', 'typescript', 'element', 'ruby', 'ruby on rails', 'yii', 'meteor', 'meteorjs', 'django', 'laravel', 'go', 'elixir', 'http', 'https''node', 'nodejs', 'express', 'backbonejs', 'scss', 'lcss'],
         'Database': ['mongo', 'mongodb', 'postgre', 'postgre', 'mysql', 'mariadb', 'cockroachdb', 'clickhouse', 'neo4j', 'rethinkdb', 'redis', 'sqlite', 'cassandra', 'couchdb', 'firebird', 'firebase', 'cubrid'],
         'Programacion': ['c++', 'c', 'c#', 'python', 'java', 'kotlin', 'go', 'golang', 'assembly', 'swift', 'rust', 'ruby'],
         'Data Science': ['panda', 'big data', 'data mining', 'clustering', 'nlp', 'machine learning', 'data science', 'deep learning', 'modelado', 'modeling', 'nlp', 'pln'],
         'Programacion Movil': ['react native', 'flutter', 'ionic', 'swift', 'kotlin', 'java']
         }

canvas = Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)


# logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = Label(
    root, text="Select a Resume PDF file from your computer", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

# el boton al fin gazione
buttonText = StringVar()
button = Button(root, textvariable=buttonText, command=lambda: open_pdf(), font="Raleway",
                bg='#20bebe', fg="white", width=15, height=2)
buttonText.set("Browse for a PDF")
button.grid(column=1, row=2)

canvas = Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

# funcion del boton


def open_pdf():
    buttonText.set("Loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a PDF File", filetypes=[
                       ("Pdf file", "*.pdf")])
    if file:
        content = miner.extract_text(file)
        # caja de texto

        textBox = Text(root, height=10, width=50, padx=15, pady=15)
        textBox.insert(1.0, content)
        textBox.tag_config("center", justify="center")
        textBox.tag_add("center", 1.0, "end")
        textBox.grid(column=1, row=3)

        buttonText.set("Browse for a PDF")

        content = content.lower()

        content = content.translate(str.maketrans('', '', string.punctuation))

        content = normalize(content)

        print(terms.keys())

        text = content

        puntuacion(text)

        return


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def puntuacion(t):

    habilidades = 0
    web = 0
    database = 0
    programacion = 0
    datascience = 0
    movil = 0

    scores = []
    print(t)
    for area in terms.keys():

        if area == 'Habilidades Generales':
            for word in terms[area]:
                if word in t:
                    habilidades += 1
                    print(word)
            scores.append(habilidades)

        elif area == 'Programacion Web':
            for word in terms[area]:
                if word in t:
                    web += 1
                    print(word)
            scores.append(web)

        elif area == 'Database':
            for word in terms[area]:
                if word in t:
                    database += 1
                    print(word)
            scores.append(database)

        elif area == 'Programacion':
            for word in terms[area]:
                if word in t:
                    programacion += 1
                    print(word)
            scores.append(programacion)

        elif area == 'Data Science':
            for word in terms[area]:
                if word in t:
                    datascience += 1
                    print(word)
            scores.append(datascience)

        else:
            if area == 'Programacion Movil':
                for word in terms[area]:
                    if word in t:
                        movil += 1
                        print(word)
                scores.append(movil)
    summary = pd.DataFrame(scores, index=terms.keys(), columns=[
                           'score']).sort_values(by='score', ascending=False)


root.mainloop()
