import os


class CSVFile():
    """
    Questa classe rappresenta un oggentto CSV
    """
    def __init__(self, name):
        self.name = name
        if not isinstance(self.name, str):
            raise TypeError(f"Errore: il nome del file deve essere una stringa.")

    def get_data(self, start = None, end = None):
        """
        Questo metodo prende in input un file csv e torna i suoi dati
        in una lista di liste
        """
        if (start is None or start == 0):
            self.start = 1
        else:
            self.start = start

        if end is None:
            tmp = []
            with open(self.name, 'r') as f:
                for line in f:
                    elem = line.split(',')
                    if elem[0] != "Date":
                        date = elem[0]
                        val = elem[1]
                        tmp.append([date, val])
            self.end = len(tmp)
        else:
            self.end = end

        if (self.start > self.end):
            raise IndexError("Errore: intervallo invalido.")
        
        if not os.path.isfile(self.name):
            raise FileNotFoundError(f'Errore: il file "{self.name}" non esiste')
        
        else:

            my_list = [] 
            mia_lista = []
            
            my_file = open(self.name, 'r')
        
            for line in my_file:
                elements = line.split(',')
                #if elements[0] == "Date":
                    #date = elements[0]
                    #sales = elements[1]
                    #my_list.append([date, sales])
                #elif elements[0] != "Date":
                date = elements[0]
                value = elements[1].strip()
                my_list.append([date, value])
            my_file.close()
            mia_lista = my_list[abs(self.start) - 1 : abs(self.end)]
            return mia_lista


class NumericalCSVFile(CSVFile):
    """Questa classe e' un estensione ovvero una sottoclasse
    di CSVFile che rappresenta la versione numerica"""

    def __init__(self, name):
        super().__init__(name)

    def get_data(self, *args, **kwargs):

        my_list = super().get_data(*args, **kwargs)
        conv_list = []

        for elem in my_list:
            if elem[0] == "Date":
                date = elem[0]
                sales = elem[1].strip()
                conv_list.append([date, sales])
            else:
                try:
                
                    conv_list.append([elem[0], float(elem[1])])
                except:
                    print("cannot convert to floating point number")
                    continue

        return conv_list


mycsv = NumericalCSVFile("shampoo_sales.csv")
myl = mycsv.get_data(5, 10)
print(myl)
