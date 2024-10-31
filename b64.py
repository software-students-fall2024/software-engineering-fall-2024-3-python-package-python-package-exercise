def base64(str, type="encode"):
    base64_Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    type =  type.lower()
    
    if type == "encode":
        binaryStr = ''.join([format(ord(char), '08b') for char in str])
        
        paddingLength = 6- len(binaryStr) % 6
        binaryStr = binaryStr + '0' * paddingLength
        
        sixBitChunks = [binaryStr[i:i+6] for i in range(0, len(binaryStr), 6)]
        
        base64Encoded = ''.join(base64_Chars[int(chunk, 2)] for chunk in sixBitChunks)
        
        padding = "=" * (4 - len(base64Encoded) % 4)

        return base64Encoded + padding
    elif type == "decode":
        if not all(char in base64_Chars or char == '=' for char in str): 
            print("Invalid format: Only base64 Characters are allowed(A-Z, a-z, 0-9, +, /, =)")
            return None
        
        str = str.rstrip("=")
        
        binaryStr = ''.join([format(base64_Chars.index(char), '06b') for char in str])
        
        byteChunk = [binaryStr[i:i+8] for i in range(0, len(binaryStr), 8)]
        
        decodedStr = ''.join([chr(int(byte, 2)) for byte in byteChunk if len(byte) == 8])
        
        return decodedStr
    else:
        print("Invalid action type: Please select 'encode' or 'decode'.") 
        return None
        
        
    
# str = "="
# encoded = base64(str, "encode")
# print(encoded)
# print(base64(encoded, "decode"))
        