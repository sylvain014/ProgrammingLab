from random import randint

class Coin:

    """Questa classe simula il lancio di una moneta"""

    def __init__(self):
        self.faccia = "Testa"

    def lancio(self):
        random_num = randint(0,1)
        if random_num == 0:
            self.faccia = "Testa"
        else:
            self.faccia = "Croce"

    def get_faccia(self):
        return f"Risultato dopo il lancio: {self.faccia}\n"

mia_moneta = Coin()
mia_moneta.lancio()
mia_moneta.get_faccia()
print(mia_moneta.get_faccia())
mia_moneta.lancio()
print(mia_moneta.get_faccia())
mia_moneta.lancio()
print(mia_moneta.get_faccia())
