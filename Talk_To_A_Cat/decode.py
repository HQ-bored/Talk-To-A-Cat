# ai wrote the entire thing, i just gave it the instructions how and added the if true loop

INT_MORSE_LIB = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',  '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}

# Invert the dictionary for Morse -> English lookups
REVERSE_MORSE = {value: key for key, value in INT_MORSE_LIB.items()}

def DecodeToMorseCode(encoded_text):
    morse_signals = []
    
    for i in range(len(encoded_text)):
        char = encoded_text[i]
        
        if char == ' ':
            morse_signals.append(' ')
            continue
            
        if char.isupper():
            morse_signals.append('-')
        elif char.islower():
            morse_signals.append('.')
            
        if i + 1 < len(encoded_text):
            next_char = encoded_text[i + 1]
            if next_char != ' ' and char.lower() != next_char.lower():
                morse_signals.append('/')
                
    return "".join(morse_signals)

def TranslateMorseToEnglish(morse_str):
    # Split by spaces to separate words
    words = morse_str.split(' ')
    english_words = []
    
    for word in words:
        if not word:
            continue
        # Split by slashes to separate individual letters
        letters = word.split('/')
        english_letters = []
        
        for letter in letters:
            if letter in REVERSE_MORSE:
                english_letters.append(REVERSE_MORSE[letter])
            elif letter == '':
                continue
            else:
                english_letters.append('?') # Fallback for structural anomalies
                
        english_words.append("".join(english_letters))
        
    return " ".join(english_words)

if __name__ == "__main__":
    while True:
        cat_input = input("Paste Cat Message here: ")
    
        # Step 1: Extract Morse code
        morse_output = DecodeToMorseCode(cat_input)
        print("\n[1] Clean Morse Code:")
        print(morse_output)
    
        # Step 2: Translate to English
        english_output = TranslateMorseToEnglish(morse_output)
        print("\n[2] Human Translation:")
        print(english_output)