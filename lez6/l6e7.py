
while True:
    print("\n------------------------------------------------------------------\n")
    print("Benvenuto nel menu!\nEcco le opzioni disponibili:\n")

    print("1.Calcolare la somma tra due numeri\n")
    print("2.Calcolare la differenza tra due numeri\n")
    print("3.Uscire\n")

    while True:
       try:
            scelta = int(input("Scegli una tra(1, 2 o 3): "))
            if scelta in (1, 2, 3):
                break
            else:
                print("\nErrore: Devi inserire un numero compreso tra 1 e 3, \nRiprova\n")
       except ValueError:
            print("Errore: hai inserito un numero invalido,\nRiprova!\n")

    if scelta == 1:
        while True:
            try:
                num1 = float(input("\nInserisci un reale: "))
                num2 = float(input('Inseriscine un altro: '))
                break
            except ValueError:
                print('Errore: hai inserito un reale invalido, \nRiprova!\n')

        print(f"\nLa somma di {num1} e {num2} e': {num1 + num2}\n")

    elif scelta == 2:
        while True:
            try:
                num1 = float(input("\nInserisci un reale: "))
                num2 = float(input("Inseriscine un altro: "))
                break
            except ValueError:
                print('Errore: hai inserito un reale invalido, \nRiprova!\n')

        print(f"\nLa differenza tra {num1} e {num2} e': {num1 - num2}\n")

    if scelta == 3:
        print("\nGrazie di aver usato il programma.\nUscita dal programma...\n")
        break


