#This program checks if a string a palindrome

my_string = input("\nInserisci una stringa: ")

def palindromo(mystr):
    """
    Questa funzione verifica se una string e' palindromo
    args: (str)
    es: palindromo(str) stabilisce se str e' palindromo oppure no
    """
    rev_str = mystr[-1::-1]

    if my_string == rev_str:
        print(f"\n{my_string} e' palindromo\n")
    else:
        print(f"\n{my_string} non e'  palindromo\n")

palindromo(my_string)
