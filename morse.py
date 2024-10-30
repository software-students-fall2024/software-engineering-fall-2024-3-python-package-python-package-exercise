
def morse(str, type):
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
    
    
    if type == "encode":
        morseCode = []
        for char in str.upper():
            if char in morseDict:
                morseCode.append(morseDict[char])
        return ' '.join(morseCode)
    elif type == "decode":
        words = str.split('   ')
        decodedText = []
        
        for word in words:
            decodedWord = []
            for symbol in word.split():
                if symbol in reverseMorseDict:
                    decodedWord.append(reverseMorseDict[symbol])
            decodedText.append(''.join(decodedWord))
            
        return ' '.join(decodedText)

            
    
    