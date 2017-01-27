# Caesar Cipher

MAX_KEY_SIZE = 256


def getFile():
    print('give encoded file name:')
    return open('file1-35121.rtf.enc').read()


def getTranslatedMessage(message):
        translated = ''
        for symbol in message:
            num = (ord(symbol)-(currentKey))%256
            translated += chr(num)
        return translated


encoded_file = getFile()
currentKey =1
text_file = open("de.txt", "a")

while (currentKey<MAX_KEY_SIZE):
    text_file.write(getTranslatedMessage(encoded_file))
    currentKey +=1
text_file.close()
