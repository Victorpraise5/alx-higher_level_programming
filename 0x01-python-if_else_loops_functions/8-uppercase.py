#!/usr/bin/python3
def uppercase(str):
    result = " "
    for char in str:
        #to check if the character is lowercase
        if 'a' <= char <= 'z':
            #to convert lowercase to uppercase
            uppercase_char = chr(ord(char)-32)
            result += uppercase_char
        else:
            result += char
    print(result)
