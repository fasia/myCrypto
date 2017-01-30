# Author: Faezeh Siavashi
# Date: Jan 23 2017
#***********************************
# Method: Caesar
# Alphabet: ASCII table, all of 256 symbols
# Data Type: Some Microsoft Document Text Format

MAX_KEY_SIZE = 256

#read the encoded file
def getFile():
    print('give encoded file name:')
    return open('file1-35121.rtf.enc').read() # this file can be found in myCrypto Folder

#decode the file based on current key
def getTranslatedMessage(message):
        translated = ''
        for symbol in message:
            num = (ord(symbol)-(currentKey))%MAX_KEY_SIZE # caeser decoding folmula: decode=(encode-key)mod MAX_KEY_SIZE
            translated += chr(num)
        return translated


    
encoded_file = getFile()
currentKey =1

#output file
text_file = open("de.txt", "a")
while (currentKey<MAX_KEY_SIZE):
    text_file.write(getTranslatedMessage(encoded_file))
    currentKey +=1
text_file.close()
