
def morse(str, type="encode"):
    morseDict = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
        'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
        'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
        'Z': '--..',  '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ' ': ' '
    }
    reverseMorseDict = {value: key for key, value in morseDict.items()}
    
    type = type.lower()
    
    if type == "encode":
        if not all(char.isalnum() or char.isspace() for char in str): 
            print("Invalid format: Only alphanumeric characters and spaces are allowed.")
            return -1
        morseCode = []
        for char in str.upper():
            if char in morseDict:
                morseCode.append(morseDict[char])
        return ' '.join(morseCode)
    elif type == "decode":
        if not all(char.isspace() or char == '.' or char == '-' for char in str): 
            print("Invalid format: Only dots, dashes, and spaces are allowed for decoding")
            return -1
        words = str.split('   ')
        decodedText = []
        
        for word in words:
            decodedWord = []
            for symbol in word.split():
                if symbol in reverseMorseDict:
                    decodedWord.append(reverseMorseDict[symbol])
            decodedText.append(''.join(decodedWord))    
        return ' '.join(decodedText)
    else:
        print("Invalid action type: Please select 'encode' or 'decode'.") 
        return -1

            
    
    