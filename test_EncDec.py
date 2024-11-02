import pytest
from morse import morse
from b64 import base64

#Morse Tests
def testMorseEncode():
    valid_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789"
    expected_output = (
        ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..   ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----."
    )
    assert morse(valid_char, "encode") == expected_output
    assert morse("", "encode") == ""
    
def testMorseDecode():
    valid_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789"
    input = (
         ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..   ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----."
    )
    assert morse(input, "decode") == valid_char
    assert morse("", "decode") == ""
    
def testMorseInvalidCharactersEncode():
    assert morse("!", "encode") is None
    
def testMorseInvalidCharactersDecode():
    assert morse("A", "decode") is None 
    
def testMorseInvalidType():
    assert morse("HELLO", "translate") is None
    
#Base64 Tests
def testB64Encode():
    assert base64("base64+=./", "encode") == "YmFzZTY0Kz0uLw=="
    assert base64("", "encode") == ""
    
def testB64Decode():
    assert base64("aGVsbG8=", "decode") == "hello"
    assert base64("TU9SU0U=", "decode") == "MORSE"
    assert base64("dGVzdA==", "decode") == "test"
    
def testB64InvalidCharacters():
    assert base64("!", "decode") is None
    
def testB64InvalidType():
    assert base64("Hello", "translate") is None 
    


    
