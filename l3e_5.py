#Esercizio 5 della lezione 3

def remove_duplicate(infile):
    with open(infile, 'r') as infile, open('unique.txt', 'w') as outfile:
        righe_viste = set()

        for riga in infile:
            if riga not in righe_viste:
                outfile.write(riga)
                righe_viste.add(riga)
