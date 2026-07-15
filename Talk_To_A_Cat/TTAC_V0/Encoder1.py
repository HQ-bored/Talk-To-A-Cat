# Main code
CatMessage = input("CatMessage: ") # temp get from terminal

EncodedCatMessage = []

# Runs these files and gets value of these Varibles
from Base import BaseCatMessage
from Morse import MorseCatMessage 

morse_index = 0 # Counter for the position of the character that the for loop is currently processing

#Combines them using uppercase and lowercase
for char in BaseCatMessage:
        # If it's a space between words, just keep it as a space
        if char == ' ':
            EncodedCatMessage.append(' ')
            continue
            
        # Looks at the matching signal in our Morse string
        signal = MorseCatMessage[morse_index] 
        
        # Rule: Dash = Uppercase, Dot = Lowercase
        if signal == '-':
            EncodedCatMessage.append(char.upper())
        else:
            if signal == '.':
                EncodedCatMessage.append(char.lower())
            else:
                continue
            
        # Moves to the next dot/dash signal
        morse_index += 1
         
"".join(EncodedCatMessage)

print("CatMessage:", EncodedCatMessage)