
class CSVFile:
    """Questa classe rappresenta un blueprint di un file CSV"""

    def __init__(self, name):
        self.name = name

    def get_data(self):
        mia_lista = []
        with open(self.name, 'r') as readfile:

            for line in readfile:
                element = line.strip().split(',')
                if element[0] != 'Date':
                    date = element[0]
                    value = element[1]

                    mia_lista.append([date, value])

        return mia_lista

my_csv = CSVFile("shampoo_sales.csv")
print(my_csv.get_data())
