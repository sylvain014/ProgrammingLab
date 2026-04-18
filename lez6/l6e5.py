from datetime import date

data = input("Inserisci la tua data di nascita(Giorno-Mese-Anno): ")

mia_lista = data.split('-')
anno = int(mia_lista[2])
mese = int(mia_lista[1])
giorno = int(mia_lista[0])

today = date.today()

print(f"\nHai {today.year - anno} anni!\n")

data_nascita = date(anno, mese, giorno)

data_compleanno = date(today.year, mese, giorno)

if data_compleanno > today:
    giorni = data_compleanno - today
    print(f"Mancano {giorni.days} giorni per il tuo prossimo compleanno\n")
elif data_compleanno == today:
    giorni = data_compleanno - today
    print("Buon compleanno!")
else:
    prossimo_anno = date(today.year + 1, mese, giorno)
    giorni = prossimo_anno - today
    print(f"Mancano {giorni.days} giorni per il tuo prossimo compleanno\n")

print(f"Mancano {giorni.days * 24} ore per il tuo prossimo compleanno\n")
print(f"Mancano {giorni.days * 24 * 60} minuti per il tuo prossimo compleanno\n")
print(f"Mancano {giorni.days * 24 * 60 * 60} secondi per il tuo prossimo compleanno\n")
