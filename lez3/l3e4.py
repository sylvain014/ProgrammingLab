# This program verifies if two lists have at least one element in common

my_list1 = [1, 2, 3, 4, 5, 6, 7]
my_list2 = [8, 9, 0, 11, 12, 5]

def compare(A, B):
    """
    Questo funzione prende due liste in input e verifica se hanno al meno
    un elemento in common
    arg: lista1, lista2
    es: compare(lista1, lista2)
    """
    found = False
    for item in A:
        if item in B:
            print(f"Queste due liste hanno al meno un elemento in comune: \n{A}\n{B}\nche e' {item}\n")
            found = True
            break
    if not found:
        print(f"Queste due liste non hanno nessun elemento in comune: \n{A}\n{B}\n")

compare(my_list1, my_list2)

