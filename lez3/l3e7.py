#This program takes in a function with a csv file and then sum the sales in the file

with open("shampoo_sales.csv", 'r') as my_file:
#We need a list to store the values of the shampoo_sales

    val = []
    #now that we've our file's content in a variable we can use it
    for line in my_file:
        #if it's the header of the file we skip 
        element = line.split(',')
        if element[0] != "Date":
            date = element[0]
            value = element[1]
            val.append(value)
    def sum_shampoo_sales(my_val):
        sum = 0
        for val in my_val:
            sum = sum + float(val)

        return sum

    shampoo_sales = sum_shampoo_sales(val)
    print(f"\nLa somma delle vendite degli shampoo_sales e': {shampoo_sales: 2f}\n")


