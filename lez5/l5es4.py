
class Poligono:
    """Questa e' una classe che descrive la struttura di 
    un Poligono"""

    def __init__(self, lati):
        self.lati = lati

    def __str__(self) -> str:
        return f"Sono un poligono con {self.lati} lati\n"


class Quadrilatero(Poligono):
    """Questa e' una sottoclasse di Poligono che rappresenta
    un quadrilatero"""

    def __init__(self):
        super().__init__(4)

    def __str__(self) -> str:
        return "Sono un quadrilatero\n"


class Rettangolo(Quadrilatero):
    """Questa e' una sottoclasse di Quadrilatero che rappresenta
    un rettangolo"""

    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def __str__(self) -> str:
        return f"\nSono un rettangolo di \nbase: {self.base}\naltezza: {self.altezza}\n"

    def perimetro(self):
        return f"Il perimetro del rettangolo e': {2 * self.base * self.altezza}\n"

    def area(self):
        return f"L'area del rettangolo e': {self.base * self.altezza}\n"


class Triangolo(Poligono):
    """Questa e' una sottoclasse di Poligono che rappresenta un triangolo"""

    def __init__(self, lat1, lat2, lat3):
        self.lat1 = lat1
        self.lat2 = lat2
        self.lat3 = lat3

    def __str__(self) -> str:
        return f"Sono un triangolo con i seguenti lati: \n{self.lat1}\n {self.lat2}\n {self.lat3}\n"

    def perimetro(self):
        return f"Il perimetro del triangolo e': {self.lat3 + self.lat2 + self.lat1}\n"

    def is_equilatero(self):
        if(self.lat1 == self.lat2 == self.lat3):
            return True
        else:
            return False

mio_triangolo = Triangolo(2, 2, 4)

print(mio_triangolo.is_equilatero())

print(mio_triangolo.perimetro())

