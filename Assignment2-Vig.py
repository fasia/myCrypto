# Author: Faezeh Siavashi
# Date= Jan 30 2017

#Method: Vigenere
#Alphabet: ASCII table, all of 256 symbols
#Data Type: Text file
#Hint: The file contains phrase “Hello, <Your First name Your Last name>!” (as in the table below). 
#This phrase is coming somewhere at the second line of the plaintext!


# from 69th char in the string, "Hello, Faezeh Siavashi!" can be found. so, I only search this part of the encoded string

#NOITCE: the length of the keyword is found manually


import collections

def getMessage():
    return open('file2-35121.txt.enc').read()
#decoder
def decodeMessage(symbol, msg, k):
    num = (ord(msg) - k) % 256
    if chr(num )== symbol:
        #print 'key for',chr(num),' is:', k
        myArray2.append(k)
    return num


#For a given characther, search all range of ascii codes until find the match. Then add the ascii 
def findKeyword(s):
    for symbol in knownWord:
        k = 0
        #print 'starting from', startingPoint, 'for symbol', symbol
        while k<256:
            decodeMessage(symbol, m1[s], k)
            k +=1
        s +=1

#myArray2 = [ 'u', 'k', 'u', 'j', 'k', 'h', 'g', 'h','k', 'j', 'j', 'h']

def shiftKeywordToCorrectPlace():
    myArray2[keywordLength:]=[] # first we cut the repeatitive part of the keyword. Just keep the keylength
    temp = divmod(startingPoint, keywordLength) # 68/12 = 5 and 8 remainder
    t = keywordLength-temp[1] # temp[1] == 8 remainder. the actual starting point of the keyword
    #for i in range(t): # so we shift to left 4 times (or we can shift to right 8 times)
     #   myArray2.pop(0)
    de = collections.deque(myArray2)
    de.rotate(temp[1])
    #now we translate keyword from the ascii code to char
    for i in range(len(de)):
        myArray.append(chr(de[i]))
    return de

#decode the string
def decoding():
    decode=''
    textCounter=0
    for m in m1:
        num = (ord(m) - de[textCounter%keywordLength])% 256
        #print 'm is:',ord(m),'key: ',chr(myArray2[textCounter%keywordLength]), myArray2[textCounter%keywordLength],'num:', num
        decode+=chr(num)
        textCounter +=1
    return decode

myArray = []
myArray2 =[]
#keylength is manually found based on the repeation of the same set of characters. 
keywordLength = 12 
# the given hint is to have a string as follow:
knownWord = 'Hello, Faezeh Siavashi!'
#starting point of the string should be from a position which we guess is the second line.
#I found it by looking at the encoded string and guessing :D 
# My finding is to have charecter 68th in the encoded string as the first character of the known string (Hello, ...)
startingPoint=68
#first we open the encoded string as m1
m1=getMessage()
# based on the starting point, we find the keyword. 
findKeyword(startingPoint)
# the following code is to calculate that what is the actual position of the key in location 68. 
#Since the keyword length is 12 and we started from 68, therefore, 68th char is 8th key. (5 times 12 keyword = 60 and 8 = 68) 
#so we need to shift the keyword array either 8 times to left or 4 times to right (either way we will have same result)
de =shiftKeywordToCorrectPlace()
print decoding()
print de
print myArray

