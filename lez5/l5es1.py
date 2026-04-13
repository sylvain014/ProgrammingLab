#Let's practice some inheritance principles in python

from types import EllipsisType


class Persona:
    #definiamo il costruttore
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    #A greeting function
    def saluta(self):
        print(f"\nCiao, Io sono {self.nome}  {self.cognome}.\n")

class Studente(Persona):
    '''This is a subclass Studente from the super class Persona which defines
    a student'''

    def __init__(self, nome, cognome, corsi = None):

        super().__init__("Studente UniTS", nome, cognome)
        if corsi == None:
            self.corsi = []
        else:
            self.corsi = corsi

    def saluta(self):

        Persona.saluta(self)
        print(f"\nFrequento i corsi: {self.corsi}\n")

class Docente(Persona):
    '''This is a subclass Docente from the parent class Persona which defines
    a teacher'''

    def __init__(self, nome, cognome, corsi = None):

        super().__init__("Docente UniTS", nome, cognome)
        if corsi == None:
            self.corsi = []
        else:
            self.corsi = corsi

    def saluta(self):
        Persona.saluta(self)
        print(f"\nInsegno i seguenti corsi: {self.corsi}\n")

    def insegna_tutti_corsi(self, student):
        """Un algoritmo che calcoli se un docente insegna tutti i corsi frequentati
        da uno student"""

        

        for corso in student.corsi:
            if corso not in self.corsi:
                
                print(f"\nIl Docente {self.nome} non insegna tutti i corsi frequentati dallo student!\n")
                return False
        
        print(f"\nIl Docente {self.nome} insegna tutti i corsi frequentati dallo student!\n")
        return True


    def esistenza_docenti(self, student, docenti = None):
        
        if docenti is None:
            self.docenti = []
        else:
            self.docenti = docenti

        for docente in self.docenti:
            if(docente.insegna_tutti_corsi(student)):
                print("\nEsistono dei docenti che insegnano tutti i corsi frequentati dallo student")
                return True
        print("\nNon esistono dei docenti che insegnano tutti i corsi frequentati dallo student")
        return False


corsi = ["Programmazione", "Laboratorio", "Analisi", "Geometria"]
d_corsi = ["Programmazione", "Laboratorio", "Analisi", "Geometria", "Fisica", "Chimica"]

stu_Irene = Studente("Irene", "Rossi", corsi)
stu_Irene.saluta()

do_Paolo = Docente("Paolo", "Bianchi", d_corsi)
do_Paolo.saluta()

do_Paolo.insegna_tutti_corsi(stu_Irene)

do_Paolo.esistenza_docenti(stu_Irene, [do_Paolo])
