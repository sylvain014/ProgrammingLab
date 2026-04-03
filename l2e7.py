#Definire la funzione fattoriale(versione iterativa)

def fat(numero):
    fattoriale = 1
    for item in range(1, numero+1):
        fattoriale *= item
    return fattoriale

numero = int(input('Inserisci un numero: '))
fatt = fat(numero)
print(f'Il fattoriale di {numero} is: {fatt}')
