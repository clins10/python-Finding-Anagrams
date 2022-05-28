# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from lib2to3.pgen2.token import COMMENT


COMMENT = "SOLUTION"


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.lower()
    anagram = anagram.lower()

    if(sorted(word) == sorted(anagram)):
        print(sorted(word), sorted(anagram))
        return True
    else:
        return False
print(find_anagram("snow", "nows"))
print(find_anagram("below", "elbow"))


     



    

