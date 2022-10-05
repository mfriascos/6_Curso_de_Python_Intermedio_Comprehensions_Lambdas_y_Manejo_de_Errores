import os


def printpic(hidden_word,the_word,tries,categorie): 
    os.system("clear")
    if categorie == 1:
        str_categorie = 'random words in spanish.'
    elif categorie == 2:
        str_categorie = 'verbs on english.'
    elif categorie == 3:
        str_categorie = 'verbs in spanish.'
    else:
        str_categorie = 'programation words in spanish or english.'
    print("""
         _                                             
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                           |___/                       
        
        **********Welcome to hangman game**************
        

        {}""".format(str_categorie))   
    HANGMANPICS = [
                            '''






                            ''',
                            '''
                            +---+
                            |   |
                                |
                                |
                                |
                                |
                            =========''',
                            '''
                            +---+
                            |   |
                            O   |
                                |
                                |
                                |
                            =========''',
                            '''
                            +---+
                            |   |
                            O   |
                            |   |
                                |
                                |
                            =========''',
                            '''
                            +---+
                            |   |
                            O   |
                           /|   |
                                |
                                |
                            =========''',
                            '''
                            +---+
                            |   |
                            O   |
                           /|\  |
                                |
                                |
                            =========''',
                            '''
                            +---+
                            |   |
                            O   |
                           /|\  |
                           /    |
                                |
                            =========''',
                            '''
                            +---+
                            |   |
                            O   |
                           /|\  |
                           / \  |
                                |
                            =========''']
    print(HANGMANPICS[tries].format(hidden_word))
    print("                           "+str(hidden_word))
    print(the_word)
