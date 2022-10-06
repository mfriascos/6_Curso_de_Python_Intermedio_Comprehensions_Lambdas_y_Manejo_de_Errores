import os


def printpic(tries,category): 
    os.system("clear")
    if category == 1:
        str_category = 'random words in spanish.'
    elif category == 2:
        str_category = 'verbs on english.'
    elif category == 3:
        str_category = 'verbs in spanish.'
    else:
        str_category = 'programation words in spanish or english.'
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
        

        {}""".format(str_category))   
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
    print(HANGMANPICS[tries])
