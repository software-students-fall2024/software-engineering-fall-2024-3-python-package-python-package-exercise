#Main Function for Encoders and Decoders
import random
from shutdown import shutdown_system
from b64 import base64
from morse import morse
import string


def encode(str, type):
    if random.random() <= 0.05:
        shutdown_system()
    
    type = type.lower()
    encodedStr = ""
    
    if random.random() >= 0.7:
        if type == "morse":
            encodedStr = morse(str)
        elif type == "base64":
            encodedStr = base64(str)
        else:
            print("Invalid encoder: Please select from [morse, base64, caesar, vigenere]") 
            return None
    else:
        encoded_chArr = []
        for char in str:
            choice = random.choice(["morse", "base64"])
            if not(char.isalnum() or char.isspace()):
                if random.random() >= 0.5:
                    choice = "base64"
                else:
                    encoded_chArr.append(char)
                    continue      
            if choice == "morse":
                encoded_chArr.append(morse(char))
            elif choice == "base64":
                encoded_chArr.append(base64(char))
        encodedStr = ''.join(encoded_chArr) 
    return encodedStr 



def isMorse(segment):
    return all(c in ".-" or c.isspace() for c in segment)

def isBase64(segment):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    return all(c in base64_chars or c == '=' for c in segment)

def randomGibberish(n):
    return ''.join(random.choice(string.ascii_letters + string.digits + "+/.-= ") for _ in range(n))

def decode(str, type):
    if random.random() <= 0.05:
        shutdown_system()
    
    type = type.lower()
    decodedStr = ""
    # Set a probability for normal decoding vs. random decoding
    if random.random() >= 0.7:
        # Normal decoding with 30% probability
        if type == "morse":
            decodedStr = morse(str, "decode")
        elif type == "base64":
            decodedStr = base64(str, "decode")
        else:
            print("Invalid decoder: Please select from [morse, base64, caesar, vigenere]") 
            return None
    else:
        decodedSegments = []
        
        i = 0
        while i < len(str):
            
            segmentLength = random.randint(1, 5)
            segmentEnd = i + segmentLength
            if segmentEnd <= len(str): 
                segment = str[i:segmentEnd]
            else: 
                segment = str[i: len(str)]
                segmentLength = len(str) - i
            
            i += segmentLength

            if random.random() >= 0.5:
                if isMorse(segment):
                    decodedSegments.append(morse(segment, "decode"))
                elif isBase64(segment):
                    decodedSegments.append(base64(segment, "decode"))
                else:
                    decodedSegments.append(randomGibberish(segmentLength))
            else:
                decodedSegments.append(randomGibberish(segmentLength))
        
        decodedStr = ''.join(decodedSegments)
        
    return decodedStr


# Example usage
encoded_str = ".... . .-.. .-.. ---"  # Example Base64 encoded text
print(decode(encoded_str, "morse"))


#print(encode("Hello World!", "base64"))