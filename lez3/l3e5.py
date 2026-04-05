# A function that takes a numeric list in input and returns a list of characters
# corresponding

my_list = [1, 0, 7, 9, 8]

def convert(A):
    """
    Questa funzione prende in input una lista di interi e restituisce 
    una corrispondente lista di interi scritti in lettera
    args: lista
    es: convert(lista)
    """
    tmp_list = []
    my_dict = {0 : "zero", 1 : "Uno", 2 : "due", 3 : "tre", 4 : "quattro", 5 : "cinque", 6 : "sei", 7 : "sette", 8 : "otto", 9 : "nove"}
    for item in A:
        tmp_list.append(my_dict[item])

    return tmp_list;

print(f"\nQuesta e' la lista originale inserita: \n{my_list}")
conv_list = convert(my_list)
print(f"\nEcco la lista convertita: \n{conv_list}\n")
