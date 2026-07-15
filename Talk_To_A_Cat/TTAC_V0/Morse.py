from Encoder import CatMessage 

INT_MORSE_LIB = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',  '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}

# Main code

encoded_letters = [] 

for letter in CatMessage.upper(): #loop through each letter in the input text, converting it to uppercase

    if letter in INT_MORSE_LIB: # Converts letter known to the dicttionary

        encoded_letters.append(INT_MORSE_LIB[letter]) # add it to this list

MorseCatMessage = "".join(encoded_letters)