#Scrivere un programma che fa la somma di n numeri inseriti dall'utente. Di all'utente di scrivere 0 per fermarsi

somma = 0
numero = int(input('Inserisci un numero(0 per fermarti): '))

while (numero != 0):
    somma += numero
    numero = int(input('Inserisci un numero(0 per fermarti): '))

print(f'Somma = {somma}')
