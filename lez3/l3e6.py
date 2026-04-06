# from list to dictionary

fruits = ["Mango", "Apple", "Banana", "Lemon", "Mango", "Apple", "Mango", "Apple", "Mango", "Lemon", "Banana"]

def list_to_dict(my_list):
    """
    Questa funzione prende in input una lista e restituisce un dizionario
    con il conteggio delle occorenze
    args: list
    es: list_to_dict(list)
    """
    my_dict = {}
    my_set = set(my_list)
    mlist = list(my_set)

    for item in mlist:
        ac_item = item
        found = 0
        for elem in my_list:
            if ac_item == elem:
                found += 1
        my_dict[item] = found

    return my_dict
my_dict = list_to_dict(fruits)

print(f"\n{my_dict}")

