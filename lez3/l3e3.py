#A function that takes a function with two arguments and swaps their values


my_string = input("\nInserisci una stringa senza punteggiatura: ")
my_list = my_string.split()
ori_list = my_list.copy()

def scambia_indici(mylist, i, j):
    """
    Questa funzione prende in input una lista e due indici e scambia 
    i valori presenti agli indici
    """
    tmp = mylist[i]
    mylist[i] = mylist[j]
    mylist[j] = tmp
    return my_list

i = int(input("\nInput the first index: "))
j = int(input("\nInput the second index: "))

print(f"\nQuesta e' la lista originale che hai inserito: {ori_list}")
my_list = scambia_indici(my_list, i, j)

print(f"\nEcco la lista aggiornata: {my_list}\n")


