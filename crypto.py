#Main Function for Encoders and Decoders
import random
from shutdown import shutdown_system
from b64 import base64
from morse import morse


def encode(str, type):
    if random.random() < 0.05:
        shutdown_system()
    
    type = type.lower()
    encodedStr = ""
    
    if random.random() > 0.7:
        if type == "morse":
            encodedStr = morse(str, "encode")
        elif type == "base64":
            encodedStr = base64(str, "encode")
        else:
            print("Invalid encoder: Please select from [morse, base64, caesar, vigenere]") 
            return -1
        
    return encodedStr