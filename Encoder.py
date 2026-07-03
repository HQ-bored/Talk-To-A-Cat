import random

BASE_OPTIONS = {2: 'mi', 3: 'mew', 4: 'meow', 5: 'miaow'}
INT_MORSE_LIB = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',  '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '_' # I put the underscore togot rid of spaces in the combine function
}

def GenerateBase():
    global BaseCatMessage # Saves mods to main code variable
    CatBasedWords = [] #This list is empty at the start, it will hold all the encoded words in the sentence once the code finishes running
    
    for word in CatMessage.split(): # Splits the words in CatMessage
        # its only apling the base generation to the first word now
        LettersLeft = len(word) # Counts num of chars in this word
        ChosenBases = [] # Makes this list
    
        while LettersLeft > 0:
        
            if LettersLeft == 1: # Only spawns "h" last
                ChosenBases.append('h')
                LettersLeft -= 1
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

        CatBasedWords.append("".join(ChosenBases))
        
    BaseCatMessage = " ".join(CatBasedWords) # Joins these with spaces

def TranslateToMorse():
    global MorseCatMessage
    encoded_letters = [] 

    for letter in CatMessage.upper(): #loop through each letter in the input text, converting it to uppercase

        if letter in INT_MORSE_LIB: # Converts letter known to the dicttionary

            encoded_letters.append(INT_MORSE_LIB[letter] + '/') # / after each letter tells the combiner to swich to ne next letterin the combine function
        else:
            encoded_letters.append('#/')

    MorseCatMessage = "".join(encoded_letters)

def CombineBaseAndMorse():
    global EncodedCatMessage
    FinalList = []
    BaseCounter = 0 # tracks pos of char in BaseCatMessage in loop 

    for signal in MorseCatMessage: # 
        
        # Moves it up a letter in BaseCatMessage
        if signal == '/':
            BaseCounter += 1
            continue
        if signal == '#':
            continue
        # If it's a space between words, just keep it as a space
        if signal == '_':
            FinalList.append(' ')
            continue

        # Looks up char in base after dealing with the special chars
        char = BaseCatMessage[BaseCounter]    

        # Turns symboles to letters : Dash = Uppercase, Dot = Lowercase
        if signal == '-':
            FinalList.append(char.upper())
        elif signal == '.':
            FinalList.append(char.lower())
         
    EncodedCatMessage = "".join(FinalList)



# Main code

BaseCatMessage = ''
MorseCatMessage = ''
EncodedCatMessage = ''


def RunCatEncoder(text_from_ai):
    global CatMessage, EncodedCatMessage
    CatMessage = text_from_ai

    GenerateBase()
    TranslateToMorse()
    CombineBaseAndMorse()

    return EncodedCatMessage

if __name__ == "__main__":
    user_input = input("CatMessage: ")
    print("Result:", RunCatEncoder(user_input))