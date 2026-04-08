#Definire una funzione che dati 3 numeri interi stabilisce se possono essere i valori dei lati di un triangolo e, se si, dire che tipo di triangolo

def triangolo(num1, num2, num3):
    """
    Questa funzione verifica se tre valori arbitrari possono essere
    il lati di un triangolo e se si stabilisce quale tipo di triangolo
    argrs: (lato1, lato2, lato3)
    """
    if (not((num1 + num2) > num3) or not((num1 + num3) > num2) or not ((num2 + num3) > num1)):
        print('I valori non possono essere dei lati di un triangolo')
    else:
        if (num1 == num2 == num3):
            print('Il triangolo is: Equilaterale')
        elif ((num1 == num2) or (num1 == num3) or (num2 ==  num3)):
            print('Il triangolo is: Isoscele')
        else:
            print('Il triangolo is: Scaleno')

(a, b, c) = (2, 3, 4)

triangolo(a, b, c)
