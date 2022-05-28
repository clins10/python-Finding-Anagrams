# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from lib2to3.pgen2.token import COMMENT


COMMENT = "SOLUTION"


def find_anagram(word, anagram):
    # [assignment] Add your code here

    #   COMMENT = 'take user input'
    # String1 = input('Enter the 1st string :')
    # String2 = input('Enter the 2nd string :')

    # COMMENT = " check if length matches" 
    # if len(String1) != len(String2):
    #if False
    # print('Strings are not anagram')
    # else:
    #sorted function sort string by characters
    # String1 = sorted(String1)
    # String2 = sorted(String2)
    #check if now strings matches
    # if String1 == String2:
        #if True
        # print('Strings are anagram')
    # else:
        #  print('Strings are not anagram')

    # COMMENT = "SOLUTION"

    word = word.lower() # make all letters lowercase
    anagram = anagram.lower() # make all letters lowercase

    # COMMENT = "comparing the length of the two words"
    # if(sorted(word) == sorted(anagram)):
        # print(sorted(word), sorted(anagram))
        # return True
    # else:
        # return False

    word = input('Enter the 1st string :') # take user input
    anagram = input('Enter the 2nd string :') # take user input

    COMMENT = "check if length matches"
    word = sorted(word)
    anagram = sorted(anagram)
    if word == anagram:
        return True
            # print('Strings are anagram')
    else:
        return False  
        # print('Strings are not anagram')

print(find_anagram("word", "anagram"))



     



    

