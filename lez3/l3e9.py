#This program takes in a file and returns a dictionary
import re
from collections import Counter

with open("my_file.txt", 'r') as my_file:

    content = my_file.read()

    def word_count(text):
        text = text.lower()
        
        words = re.findall(r'\b\w+\b', text)

        return dict(Counter(words))

    my_dic = word_count(content)
    print(f"\nThis is the corresponding dictionary from the file's content: \n{my_dic}\n")

