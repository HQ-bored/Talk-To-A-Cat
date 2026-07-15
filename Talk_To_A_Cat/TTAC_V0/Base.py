import random
from Encoder import CatMessage 

BASE_OPTIONS = {1: 'h', 2: 'mi', 3: 'mew', 4: 'meow', 5: 'miaow'}

def DecomposeWordToBases(word):
    LettersLeft = len(word) # Counts num of chars in this word
    ChosenBases = [] # Makes this list
    
    while LettersLeft > 0:
        
        if LettersLeft == 2: # prevents "hh" spawning
            ChosenBases.append('mi')
            LettersLeft -= 2
            continue
            
        # Finds valid lengths that fit
        ValidLengths = []
        for length in BASE_OPTIONS.keys():
            if length <= LettersLeft:
                ValidLengths.append(length)
                
        # Picks a length randomly 
        PickedLength = random.choice(ValidLengths)

        ChosenBases.append(BASE_OPTIONS[PickedLength])
        LettersLeft -= PickedLength

    return "".join(ChosenBases)

# main code
CatBasedWords= [] #This list is empty at the start, it will hold all the encoded words in the sentence once the code finishes running
    
for word in CatMessage.split(): # Splits the words in CatMessage
    # This applies to each word
    CatBasedWords.append(DecomposeWordToBases(word))
        
BaseCatMessage = " ".join(CatBasedWords) # Joins these with spaces