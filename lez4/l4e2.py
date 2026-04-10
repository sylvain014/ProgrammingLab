
class CSVFile():
    """
    Questa classe rappresenta un oggentto CSV
    """
    def __init__(self, name):
        self.name = name

    def get_data(self):
        """
        Questo metodo prende in input un file csv e torna i suoi dati
        in una lista di liste
        """
        my_list = []        
        my_file = open(self.name, 'r')

        for line in my_file:
            elements = line.split(',')
            if elements[0] != "Date":
                date = elements[0]
                value = elements[1].strip()
                my_list.append([date, value])
        my_file.close()
        return my_list

mycsv = CSVFile('shampoo_sales.csv')
mylist = mycsv.get_data()
print(mylist)
