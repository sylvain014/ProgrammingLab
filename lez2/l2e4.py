#Definire una funzione che prende come argomento una parola e una lettera e ritorna quante volte quella lettera e' contenuta nella parola

def numero_di_lettera_in_parola(parola, lettera):
    """
    funzione che prende una parola e una lettera:
    argr:
    parola: primo
    lettera: secondo
    ritorna il numero di (lettera) in (parola)
    """
    count = 0
    for item in parola:
        if lettera is item:
            count += 1
    return count

parola = input('Inserisci una parola: ')
lettera = input('Inserisci una lettera: ')

occorenza = numero_di_lettera_in_parola(parola, lettera)

print(f'Ci sono {occorenza}{lettera} in {parola}')
