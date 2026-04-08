#Definire la funzione fattoriale(versione iterativa)

def fat(numero):
    """
    la funzione fat calcola il fattoriale di un numero
    argrs:
    (numero)
    es: fat(5) restituisce 120
    """
    fattoriale = 1
    for item in range(1, numero+1):
        fattoriale *= item
    return fattoriale

numero = int(input('Inserisci un numero: '))
fatt = fat(numero)
print(f'Il fattoriale di {numero} is: {fatt}')
