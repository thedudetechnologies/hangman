import random
import string
import more_itertools as mit
import pdb

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

guesses = 6
avail_letters = string.ascii_lowercase
secret_word = choose_word(wordlist)  

userword = ""
#warnings = 3


def get_user_input(userinput,avail_letters):
    
    print("--------------- Available Letters ----------------")
    print(avail_letters)
    print("------------------ Guess please ------------------")
    userinput = input("Guess:")
    
    if userinput in avail_letters: 
        avail_letters = avail_letters.replace(userinput,'')
        print("Available String :",avail_letters)   
        
    else:
        print("Invalid Input")
        
    return userinput,avail_letters;

def replace_str_index(userword,position_to_change,userguess):
    for i in position_to_change:
        userword = '%s%s%s'%(userword[:i],userguess,userword[i+1:])
    return userword

def make_word(userguess,secret_word,userword):
    # Getting Position to Replace
    position_to_change = []
    position_to_change = list(mit.locate(secret_word, lambda x: x == userguess))
    userword = replace_str_index(userword,position_to_change,userguess)
    
    return userword

def hangman(secret_word,guesses,avail_letters,userword):
    swl = len(secret_word)
    print("--------------- Welcome To Hangman ---------------")
    print("------------------- Secret Word ------------------")
    # print("Secret Word :",secret_word) #Uncomment for Testing purpose only
    print("I am thinking of a word that is",swl," letters long")
    print("Note: Initially You Have 6 Guesses")
    print("Guesses:",guesses)
    print("---------------------------------------------------")
    userword = "_" * swl
    userinput =""
    try:
        while userword!=secret_word and guesses!=0:
            print("---------------------------------------------------")
            print(userword) 
            print("Guesses:",guesses)
            print("---------------------------------------------------")
            userguess,avail_letters = get_user_input(userinput,avail_letters)
            if guesses>=1:
                if userguess in secret_word:
                    userword = make_word(userguess,secret_word,userword)
                    if userword == secret_word:
                        print("--------------------------------------------------")
                        print("Winner Winner, Chiken Dinner")
                        print("Secret Word :",secret_word)
                        print("--------------------------------------------------")
                    else:
                        continue
                else:
                    guesses -= 1
                    if guesses == 0:
                        print("--------------------------------------------------")
                        print("Better Luck Next Time ")
                        print("Secret Word :",secret_word)
                        print("--------------------------------------------------")
            else:
                print("No Guesses Available ")
    except Exception as e:
        print("You Lost The Game")
        print("--------------------------------------------------")
        print(e)
        print("--------------------------------------------------")
    


if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    #print("--------------- Welcome To Hangman ---------------")
    # secret_word = choose_word(wordlist)
    hangman(secret_word,guesses,avail_letters,userword)
    
    



