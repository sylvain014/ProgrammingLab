#This program creates a class Canguro with some special methods

class Canguro:
    def __init__(self, data = None):
        if data == None:
            self.contenuto_tasca = []
        else:
            self.contenuto_tasca = data

    def intasca(self, ogg):
        self.contenuto_tasca.append(ogg)

    def __str__(self):
        return f"\n{self.contenuto_tasca}"


#Now let's create two objects to check it our class is really working

can = Canguro()
guro = Canguro()

can.intasca(1)
can.intasca("food")
can.intasca("child")
can.intasca(3.8)

print(can)

