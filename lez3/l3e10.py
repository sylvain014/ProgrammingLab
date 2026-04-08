#This is the last exercise of this section
#This program takes in a file and remove its duplicates rows and then save
#the result in a new file called unique.txt

def duplicates(text):
    righe_uniche = []

    with open(text, 'r') as my_file:
        for parola in my_file:
            line = parola.strip()
            if line not in righe_uniche:
                righe_uniche.append(line)

    with open("unique.txt", 'w') as f:
        for riga in righe_uniche:
            f.write(riga + " ")


duplicates("my_file.txt")

