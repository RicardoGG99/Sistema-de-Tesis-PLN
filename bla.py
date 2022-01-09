import spacy
import random
from spacy.training.example import Example

nlp = spacy.blank('es')

ner = nlp.add_pipe('ner')

ner.add_label('PROG')

trainData=[('escribir codigo en varios lenguajes como java', {'entities': [(41, 45,'PROG')]}), ('el papel del ingeniero de software es crear software innovador', {'entities': [(53, 62,'HAB')]}), ('habilidad para desarrollar software en python', {'entities': [(39, 45,'PROG')]}), ('excelente conocimiento de bases de datos relacionales', {'entities': [(26, 40, 'BDD')]}), ('java es un lenguaje de programacion orientado a objetos', {'entities': [(0, 4, 'PROG')]}), ('experiencia en manejo de proyectos', {'entities': []}), ('relacionales en sql', {'entities': [(16, 19, 'DBB')]}), ('experiencia en el desarrollo de aplicaciones web con framework como react', {'entities': [(68, 73, 'WEB')]}), ('dominio del desarrollo con javascript', {'entities': [(27, 37, 'WEB')]})]

nlp.begin_training()
for itn in range(10):
    random.shuffle(trainData)
    for batch in spacy.util.minibatch(trainData, size = 2):
        texts = [text for text, annotation in batch]
        annotations = [annotation for text, annotation in batch]
        nlp.update(texts, annotations)
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)