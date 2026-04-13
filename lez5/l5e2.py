
class Veicolo:

    def __init__(self, modello, marca, anno):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0

    def __str__(self):
        return f"Ecco le informazioni del Veicolo:\nModello: {self.modello}\nMarca: {self.marca}\nAnno: {self.anno}\nSpeed: {self.speed}\n"
    
    def accellerare(self):
        self.speed += 5

    def frenare(self):
        self.speed -= 5
    
    def get_speed(self):
        return f"Current speed of car: {self.speed}"


class auto(Veicolo):

    '''This is a subclass of the class Veicolo adding attributes like numero
    porte '''

    def __init__(self, modello, marca, anno, numero_porte):
        super().__init__(modello, marca, anno)
        self.numero_porte = numero_porte

    def __str__(self):
        return f"\nEcco le informazioni dell'auto: \nModello: {self.modello}\nMarca: {self.marca}\nAnno: {self.anno}\nSpeed: {self.speed}\nNumero_porte: {self.numero_porte}\n"


class moto(Veicolo):
    """Questa e' una sotto classe di Veicolo con inaggiunto il tipo della moto"""

    def __init__(self, modello, marca, anno, tipo):
        super().__init__(modello, marca, anno)
        self.tipo = tipo

    def __str__(self):
        return f"\nEcco le informazioni della moto: \nModello: {self.modello}\nMarca: {self.marca}\nAnno: {self.anno}\nSpeed: {self.speed}\nTipo: {self.tipo}\n"
