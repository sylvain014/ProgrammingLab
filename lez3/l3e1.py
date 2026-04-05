#This function sums all the elements of a list

num = float(input("\nInput the number of numeric elements you want for your list: "))

my_list = []
def sum_elm_list(n, i = 0):
    """
    Questa funzione calcola la somma di tutti gli elementi di una lista
    args: (number)
    es: sum_elm_list(number), dove number e' un intero
    """
    while i < num:
        n = float(input(f"\nInput element {i}: "))
        my_list.append(n)
        i += 1

    sum = 0.0 # Inintialize sum to save the sum of the list's elements

    for item in my_list:
        sum += item

    return sum

mysum = sum_elm_list(num)
print(f"\nThe sum of the elements of the following list:\n{my_list}\n is: sum = {mysum}\n")

