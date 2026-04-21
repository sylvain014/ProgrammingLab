#Scrivere un programma che fa la somma che verifica se un numero inserito dall'utente e' primo
numero = int(input('Inserisci un numero: '))

count = True
if (numero == 2):
    print(f'{numero} is a prime number')
for item in range(3, numero):
    if (numero % item == 0):
        count = False

if not count:
    print(f'{numero} is not a prime number')
else:
    print(f'{numero} is a prime number')
