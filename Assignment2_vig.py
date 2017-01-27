def getMessage():
    return open('file2-35121.txt.enc', 'r').read()

def encodeMessage(msg):
    textCounter = 0
    translate =''
    for symbol in msg:

        if textCounter==0:
            num = (ord(symbol) + ord(key[textCounter])) % 256
            myArray.append(ord(symbol))
            textCounter += 1
        elif textCounter==1:
            num = (ord(symbol) + ord(key[textCounter])) % 256
            myArray.append(ord(symbol))
            textCounter += 1
        elif textCounter == 2:
            num = (ord(symbol) + ord(key[textCounter])) % 256
            myArray.append(ord(symbol))
            textCounter += 1
        else:
            num = (ord(symbol) + ord(key[textCounter])) % 256
            myArray.append(ord(symbol))
            textCounter = 0

        translate += chr(num)

    return translate

message= '************************************************************* Hello, Faezeh Siavashi!!!!!!!!!!!!!' \
         'congrates you made it! I hope you have a great day  consist of individual tasks of breaking cipher codes encrypted ' \
         'with known methods. Each student can download from the table below the encrypted file assigned to ' \
         '' \
         '' \
         'him/her and try to break the cipher. The challenges to be announced at the end of lectures. ' \
         '17:00 the day the corresponded challenge was announced. The answers to be send to my email.' \
         'bye' \
         '*************************************************************'


#decoder
def readMessage(msg):
    textCounter = 0
    translated =''
    restSubTextArray()
    for symbol in msg:
        num = (ord(symbol) -(32- k)) % 256
        #print 'num is:', num
        if num>31 and num <127:
            subText[textCounter%keywordLength] +=chr(num)
        textCounter +=1
        translated += chr(num)

                #print 'word ', matchWord[i],'is found in text ', subText[j]

    return translated

def decodeSubText(txt,code):
    textCounter = 0
    translated =''
    restSubTextArray()
    for symbol in txt:
        num = (ord(symbol) -(32- code)) % 256
        subText[textCounter%keywordLength] +=chr(num)
        textCounter +=1
        translated += chr(num)
    return translated

def sortMatchWords(knownWord):
    c =0
    for i in range(keywordLength):
        matchWord.append('')

    for n in knownWord:
        matchWord[c%keywordLength]+= n
        c+=1
    print matchWord

def restSubTextArray():
    del subText[:]
    setArray()

#sort encrypted String based on the length of the keyword.
def setArray():
    #initial the array with null
    for i in range(keywordLength):
        subText.append('')


key ='M2kx'
myArray = []
myArray2 =[]
subText=[]
counter=0
# file2-35121 example
m=(encodeMessage(getMessage()))

#my example
m1 =(encodeMessage(message))
keywordLength = 4
k=1
knownWord = 'Hello, Faezeh Siavashi!'
matchWord=[]
cipherCode=['']*keywordLength
sortMatchWords(knownWord)
setArray()
result = ''
while k<257:
    print ('----------------------------------------',k ,'----------------------------------------------------------')
    dec= readMessage(m1)

    for  j in range(len(subText)):
        for i in range(len(matchWord)):
            if matchWord[i] in subText[j]:
                print ('location ',i,'in keyword has key',chr(k), k)
                print dec
                cipherCode[i]=k
    k +=1
for h in range(len(cipherCode)):
    print 'the final keyword is: ',cipherCode[h]

# for h in range(len(cipherCode)):
#     print subText[h], range(len(cipherCode))
#
#     print decodeSubText(subText[h],cipherCode[h])