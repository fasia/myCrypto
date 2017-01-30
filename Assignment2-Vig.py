# from 69th char in the string, "Hello, Faezeh Siavashi!" can be found
#so, I only search this part of the encoded string

# author: Faezeh Siavashi

#NOITCE: the length of the keyword is found manually


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
    for i in range(4):
        myArray2.pop(0)

    #now we translate keyword from the ascii code to char
    for i in range(len(myArray2)):
        myArray.append(chr(myArray2[i]))


#decode the string
def decoding():
    decode=''
    textCounter=0
    for m in m1:
        num = (ord(m) - myArray2[textCounter%keywordLength])% 256
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
temp = divmod(startingPoint,keywordLength)
textCounter = keywordLength-temp[1]
shiftKeywordToCorrectPlace()

print decoding()
print myArray2
print myArray

