
class Veicolo:
    """Questa class crea istanze di macchine"""

    def __init__(self, modello, marca, anno):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0

    def __str__(self):
        return f"\nMarca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Speed: {self.speed}\n"

    def accellerare(self):
        """
        aumenta la velocita' del Veicolo di 5 unita'
        """
        self.speed += 5
    def frenare(self):
        """
        diminuisce la velocita' del Veicolo de 5 unita'
        """
        self.speed -= 5

    def get_speed(self):
        """
        restituisce la velocita' del Veicolo
        """
        return f"\nCurrent speed: {self.speed}\n"

mia_auto = Veicolo("XTZ", "Toyota", 2004)

print(mia_auto)

mia_auto.accellerare()
print(mia_auto.get_speed())
mia_auto.accellerare()

print(mia_auto)

mia_auto.frenare()

print(mia_auto)
