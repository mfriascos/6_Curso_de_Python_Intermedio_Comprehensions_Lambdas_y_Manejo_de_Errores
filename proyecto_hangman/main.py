import os
from files_py.one import *
from files_py.hang import printpic

def start():
    os.system("clear")
    print(
        """
         _                                             
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                           |___/                       
        
        **********Welcome to hangman game**************

        Select a categorie:

        1. random words in spanish.
        2. verbs on english.
        3. verbs in spanish.
        4. programation words in spanish or english.
        """
    )

def run():
    try:
        start()
        option = int(input())
        while option < 1 or option > 4:
            start()
            option = int(input())
    except ValueError:
        print("\nType a valid option\n")
    
    if option == 1:
        one()
    # elif option == 2:
    #     two()
    # elif option == 3:
    #     three()
    # else:
    #     four()

    


if __name__ == '__main__':
    run()