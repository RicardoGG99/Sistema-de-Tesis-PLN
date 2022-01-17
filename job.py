from tkinter import *
from tkinter.filedialog import askopenfile
import pdfminer.high_level as miner
from PIL import Image, ImageTk
import string
import glob
import spacy
from spacy.matcher import Matcher
import win32api
import results

# Patterns

skills = [
    [{"TEXT": "ingles"}],
    [{"TEXT": "frances"}],
    [{"TEXT": "aleman"}],
    [{"TEXT": "orden"}],
    [{"TEXT": "ordenes"}],
    [{"TEXT": "logico"}],
    [{"TEXT": "logica"}],
    [{"TEXT": "obediente"}],
    [{"TEXT": "liderazgo"}],
    [{"TEXT": "lider"}],
    [{"TEXT": "analista"}],
    [{"TEXT": "puntual"}],
    [{"TEXT": "creativo"}],
    [{"TEXT": "proactivo"}],
    [{"TEXT": "excelencia"}],
    [{"TEXT": "creativa"}],
    [{"TEXT": "proactiva"}],
    [{"TEXT": "creatividad"}],
    [{"TEXT": "proactividad"}],
    [{"TEXT": "perfeccionista"}],
    [{"TEXT": "perfeccion"}],
    [{"TEXT": "aprendizaje"}],
    [{"TEXT": "aprender"}],
    [{"TEXT": "actitud"}],
    [{"TEXT": "aptitud"}],
    [{"TEXT": "eficiente"}],
    [{"TEXT": "eficiencia"}],
    [{"TEXT": "competencia"}],
    [{"TEXT": "competencias"}],
    [{"TEXT": "competente"}],
    [{"TEXT": "eficaz"}],
    [{"TEXT": "linux"}],
    [{"TEXT": "mac"}],
    [{"TEXT": "macos"}],
    [{"TEXT": "windows"}],
    [{"TEXT": "powershell"}],
    [{"TEXT": "terminal"}]
]

ProgWeb = [
    [{"TEXT": "javascript"}, ],
    [{"TEXT": "java"}],
    [{"TEXT": "python"}],
    [{"TEXT": "flask"}],
    [{"TEXT": "html"}],
    [{"TEXT": "angular"}],
    [{"TEXT": "angularjs"}],
    [{"TEXT": "vue"}],
    [{"TEXT": "vuejs"}],
    [{"TEXT": "react"}],
    [{"TEXT": "reactjs"}],
    [{"TEXT": "css"}],
    [{"TEXT": "objective c"}],
    [{"TEXT": "perl"}],
    [{"TEXT": "php"}],
    [{"TEXT": "typescript"}],
    [{"TEXT": "element"}],
    [{"TEXT": "ruby"}],
    [{"TEXT": "ruby"}, {"TEXT": "on"}, {"TEXT": "rails"}],
    [{"TEXT": "yii"}],
    [{"TEXT": "meteor"}],
    [{"TEXT": "meteorjs"}],
    [{"TEXT": "django"}],
    [{"TEXT": "laravel"}],
    [{"TEXT": "go"}],
    [{"TEXT": "elixir"}],
    [{"TEXT": "http"}],
    [{"TEXT": "https"}],
    [{"TEXT": "node"}],
    [{"TEXT": "nodejs"}],
    [{"TEXT": "express"}],
    [{"TEXT": "backbonejs"}],
    [{"TEXT": "scss"}],
    [{"TEXT": "lcss"}]
]

BaseDeDatos = [
    [{"TEXT": "mongo"}],
    [{"TEXT": "database"}],
    [{"TEXT": "base"}, {"TEXT": "de"}, {"TEXT": "datos"}],
    [{"TEXT": "bases"}, {"TEXT": "de"}, {"TEXT": "datos"}],
    [{"TEXT": "dbms"}],
    [{"TEXT": "data"}, {"TEXT": "base"}],
    [{"TEXT": "mongodb"}],
    [{"TEXT": "postgre"}],
    [{"TEXT": "postgresql"}],
    [{"TEXT": "mysql"}],
    [{"TEXT": "mariadb"}],
    [{"TEXT": "cockroachdb"}],
    [{"TEXT": "clickhouse"}],
    [{"TEXT": "neo4j"}],
    [{"TEXT": "rethinkdb"}],
    [{"TEXT": "redis"}],
    [{"TEXT": "sqlite"}],
    [{"TEXT": "cassandra"}],
    [{"TEXT": "couchdb"}],
    [{"TEXT": "firebird"}],
    [{"TEXT": "firebase"}],
    [{"TEXT": "cubrid"}],
    [{"TEXT": "sql"}]
]

ProgramacionRegular = [
    [{"TEXT": "java"}],
    [{"TEXT": "c++"}],
    [{"TEXT": "c#"}],
    [{"TEXT": "kotlin"}],
    [{"TEXT": "go"}],
    [{"TEXT": "golang"}],
    [{"TEXT": "assembly"}],
    [{"TEXT": "assembler"}],
    [{"TEXT": "ensamblador"}],
    [{"TEXT": "swift"}],
    [{"TEXT": "rust"}],
    [{"TEXT": "ruby"}],
]

DataScience = [
    [{"TEXT": "panda"}],
    [{"TEXT": "big"}, {"TEXT": "data"}],
    [{"TEXT": "data"}, {"TEXT": "mining"}],
    [{"TEXT": "clustering"}],
    [{"TEXT": "machine"}, {"TEXT": "learning"}],
    [{"TEXT": "data"}, {"TEXT": "science"}],
    [{"TEXT": "deep"}, {"TEXT": "learning"}],
    [{"TEXT": "modelado"}],
    [{"TEXT": "modeling"}],
    [{"TEXT": "nlp"}],
    [{"TEXT": "pln"}],
    [{"TEXT": "procesamiento"}, {"TEXT": "de"}, {
        "TEXT": "lenguaje"}, {"TEXT": "natural"}],
    [{"TEXT": "natural"}, {"TEXT": "language"}, {"TEXT": "processing"}],
    [{"TEXT": "inteligencia"}, {"TEXT": "artificial"}],
    [{"TEXT": "ia"}],
    [{"TEXT": "ai"}],
]

MobileProg = [
    [{"TEXT": "react"}, {"TEXT": "native"}],
    [{"TEXT": "flutter"}],
    [{"TEXT": "ionic"}],
    [{"TEXT": "swift"}],
    [{"TEXT": "kotlin"}],
    [{"TEXT": "java"}]
]

# Agrega lenguaje de Spacy y agrega los patterns al matcher.

nlp = spacy.load("es_core_news_sm")
matcher = Matcher(nlp.vocab)

matcher.add("HAB", skills)
matcher.add("WEB", ProgWeb)
matcher.add("BDD", BaseDeDatos)
matcher.add("PROG", ProgramacionRegular)
matcher.add("DATA", DataScience)
matcher.add("MOB", MobileProg)

# Realiza los matches.


def spacy(content):

    doc = nlp(content)
    matches = matcher(doc)

    habilidades = 0
    web = 0
    database = 0
    programacion = 0
    datascience = 0
    movil = 0

    jobScores = []
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        #print(string_id, span.text)

        if string_id == 'HAB':
            habilidades += 1

        elif string_id == 'WEB':
            web += 1

        elif string_id == 'BDD':
            database += 1

        elif string_id == 'PROG':
            programacion += 1

        elif string_id == 'DATA':
            datascience += 1

        else:
            if string_id == 'MOB':
                movil += 1

    jobScores.append(habilidades)
    jobScores.append(web)
    jobScores.append(database)
    jobScores.append(programacion)
    jobScores.append(datascience)
    jobScores.append(movil)
    # print(jobScores)

    return jobScores

# Invoca la interfaz.


def callJob(allScores):
    root = Tk()
    main(root, allScores)
    root.mainloop()


def resultsPage(root, allScores, jobScores):
    root.destroy()
    results.callResultsPage(allScores, jobScores)


# Interfaz de la pagina

def main(root, allScores):

    canvas = Canvas(root, width=600, height=600)
    canvas.grid(columnspan=4, rowspan=4)

    # logo
    for filename in glob.glob('resources/logo.png'):
        logo = Image.open(filename)
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(image=logo)
        logo_label.image = logo
        logo_label.grid(column=1, row=0)

    # instrucciones
    instructions = Label(
        root, text="Selecciona una Descripción de Trabajo", font="Raleway")
    instructions.grid(columnspan=3, column=0, row=1)

    # boton para browsear
    buttonText = StringVar()
    button = Button(root, textvariable=buttonText, command=lambda: open_pdf(buttonText, root, allScores), font="Raleway",
                    bg='#20bebe', fg="white", width=40, height=2)
    buttonText.set("Navega por tus archivos")
    button.grid(column=1, row=2)

    canvas = Canvas(root, width=600, height=250)
    canvas.grid(columnspan=3)


# Funcion para abrir y leer el PDF, Procesamiento principal, llamada a funciones.

def open_pdf(buttonText, root, allScores):
    buttonText.set("Cargando...")
    file = askopenfile(parent=root, mode='rb', title="Elige una Descripción de Trabajo", filetypes=[
        ("Pdf file", "*.pdf")])

    if file:

        content = miner.extract_text(file)
        # caja de texto
        content = content.lower()
        content = content.translate(
            str.maketrans('', '', string.punctuation))
        content = normalize(content)
        # print(terms.keys())
        JobScores = spacy(content)

        win32api.MessageBox(0, 'Descripción de Trabajo Cargada Exitosamente',
                            'Éxito', 0x00001000, )

        buttonText.set("Elige una Descripción de Trabajo")

        # boton resultsPage
        nextText = StringVar()
        next = Button(root, textvariable=nextText,
                      command=lambda: resultsPage(root, allScores, JobScores), font='Raleway', bg='#20bebe', fg="white", width=15, height=2)
        nextText.set('Siguiente')
        next.place(x=230, y=600)

        return

# Remplaza las letras con acentos.


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
