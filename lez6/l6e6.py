
while True:
    try:
        num = int(input("Inserisci un numero intero: "))
        print(f"Ecco il quadrato di {num}: {pow(num, 2)}")
        break
    except ValueError:
        print("Errore: non hai inserito un numero intero valido,\nRiprova!")

