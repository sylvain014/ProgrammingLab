#Definire una funzione che conta quante vocali sono presenti in una stringa

def conta_vocali(stringa):
    """
    conta quante vocali sono presenti in una stringa

    """
    conta = 0
    for lettera in stringa:
        if (str(lettera).lower() in ['a', 'e', 'o', 'i', 'u']):
            conta += 1

    return conta

mia_stringa = input('Inserici una stringa: ')

numero_vocali = conta_vocali(mia_stringa)

print(f'Il numeri di vocali presenti in "{mia_stringa}" is: {numero_vocali}')
