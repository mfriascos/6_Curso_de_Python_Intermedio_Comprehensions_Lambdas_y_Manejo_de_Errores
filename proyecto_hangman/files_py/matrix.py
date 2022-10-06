import random
import os

from .hang import printpic


def you_win(the_word):
    os.system("clear")
    print('''
        ____    ____   ______    __    __     ____    __    ____  __  .__   __. 
        \   \  /   /  /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | 
         \   \/   /  |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | 
          \_    _/   |  |  |  | |  |  |  |      \            /   |  | |  . `  | 
            |  |     |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | 
            |__|      \______/   \______/         \__/  \__/     |__| |__| \__| 
            
        THE WORD IS {}

        '''.format(the_word))

def game_over(the_word,category):
    printpic(7,category)
    print('''
         _______       ___      .___  ___.  _______      ______   ____    ____  _______ .______      
        /  _____|     /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \     
        |  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |    
        |  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /     
        |  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.
         \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|
    
    THE WORD WAS {}
    '''.format(the_word))

def matrix(words,category):    
    choose_word = random.randint(0,len(words)-1)

    the_word = "".join(words[choose_word]).rstrip().upper()
    the_word_show = list(the_word)
    hidden_word = (len(the_word)*'_')
    

    tries = 0
    aux = 0
    flag2 = False
    while True:
        
        flag = False
        printpic(tries,category)
        print("                           "+str(hidden_word))
        #print(the_word)
        
        if aux > 2 and flag2 == True:
            print()
            option_word =str(input("       You know what the word is (y/n): ")).lower()

            while option_word != 'y' and option_word != 'n':
                print('\nType a valid option\n')
                option_word =str(input("       You know what the word is (y/n): ")).lower()
                
            if option_word == 'y':
                print()
                right_word = str(input("       Type the word: ")).upper()

                if right_word == the_word:
                    you_win(the_word)
                    break
                else:
                    game_over(the_word,category)
                    break
        flag2 = False

        hidden_word_show = list(hidden_word)
        letter = str(input("       type a letter: ")).upper()
        
        for index,value in enumerate(the_word_show):
            if value == letter:
                hidden_word_show[index] = letter
                flag = True
                flag2 = True

        if flag == False:
            tries = tries+1    

        if tries == 7:
            game_over(the_word,category)
            break
        hidden_word = "".join(hidden_word_show).upper()

        if hidden_word == the_word:
            you_win(the_word)    
            break

        aux = aux+1