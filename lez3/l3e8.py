#This program counts the number of time a word is found in a file

with open("my_file.txt", 'r') as my_file:

    file_content = my_file.read()
    #Use .split() without an argument to create a list of words and not char
    file_content = file_content.split()
    
    def count_words(my_file, myword):
        """
        Questa funzione conta quante parole(occorenza) ci sono in un file
        args: file, parola
        es: count_words(file, parola)
        """
        #Use str.lower to solve the case sensitive problem
        my_word = str.lower(myword)
        count = 0
        for word in my_file:
            if str.lower(word) == my_word:
                count += 1

        return count
    word = input("\nInserisci una parola: ")
    words_in_file = count_words(file_content, word)
    print(f"\nCi sono {words_in_file}: '{word}' nel file.\n")

