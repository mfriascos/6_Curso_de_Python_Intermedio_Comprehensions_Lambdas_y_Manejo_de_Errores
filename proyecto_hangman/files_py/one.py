
import unicodedata
import random
import os

from .hang import printpic

categorie = 1

def one():
    words = []
    with open("./files_py/files_txt/data.txt","r",encoding="utf-8") as f:
        for line in f:
            #Quitar las tíldes y mantener las ñ's
            trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
            line = unicodedata.normalize('NFKC', unicodedata.normalize('NFKD', str(line)).translate(trans_tab))
            #---------------------------------------
            words.append(str(line))

    choose_word = random.randint(0,len(words)-1)

    the_word = "".join(words[choose_word]).rstrip().upper()
    the_words = list(the_word)
    hidden_word = (len(the_word)*'X ')
    hidden_words = list(hidden_word)

    printpic(hidden_word,the_word,0,categorie)
    try:
        letter = str(input("     type a letter: "))
    except ValueError:
        print("\nType a valid character\n")

    printpic(hidden_word,the_word,1,categorie)

    try:
        letter = str(input("     type a letter: "))
    except ValueError:
        print("\nType a valid character\n")

    
    printpic(hidden_word,the_word,1,categorie)
