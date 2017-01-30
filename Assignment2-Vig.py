# from 69th char in the string, "Hello, Faezeh Siavashi!" can be found
#so, I only search this part of the encoded string

# author: Faezeh Siavashi

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
keywordLength = 12
knownWord = 'Hello, Faezeh Siavashi!'
startingPoint=68
m1=getMessage()
findKeyword(startingPoint)
de =shiftKeywordToCorrectPlace()


print decoding()
print de
print myArray

