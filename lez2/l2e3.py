#Scrivere un programma che verifica se un numero inserito dall'utente e' pari o dispari

numero = float(input('Inserisci un numero: '))

if (numero % 2 == 0):
    print(f'{numero} is pari')
else:
    print(f'{numero} is  dispari')
