# Author: Faezeh Siavashi
# Date: Feb ?? 2017
#***********************************
# Method: Monoalphabetic
# Alphabet: ASCII table, all of 256 symbols
# Data Type: text

MAX_KEY_SIZE = 256
FreqArr=['e',' ','t','a','o','i','n','s','r','h','d','l','u','c','m','f','y','w','g','p','b','v','k','x','q','j','z','0']

#read the encoded file
def getFile():
    return open('file3-35121.txt.enc').read() # this file can be found in myCrypto Folder

#decode the file based on current key
def getLetterFrequency(l):
    #myarray.append(chr(l))
    myarray.append(msg.count(l))
    return msg.count(l)

def replaceLetter(l,msg):
        newString =list(msg)
        print(newString)
        counter =0
        newletter= FreqArr.pop(0)
        if newletter is not 0:
            for m in msg :
                counter +=1
                if m == l:
                    newString[counter-1]= newletter
                #print newString[counter]
        return newString


# sort array to deceding
def sortArray():
    for i in range(len(myarray)):
        arr.append(myarray[i])
    arr.sort()
    arr.reverse()
    print(arr)



msg = getFile()
myarray = []
arr = []
# make a copy of the encoded message into a new string to manipulate it
translated=''
for b in msg:
    translated += b

print('trans:', translated)

#calculate each letter's frequency
for m in range(MAX_KEY_SIZE):
    #print('range max',m)
    getLetterFrequency(chr(m))
print('my array', myarray)

#sort the array based on the maximum frequency
sortArray()
# the first element is the max

#for i in range(len(myarray)):
    #maxNum = arr.pop(0)
    #if maxNum > 7:
        #print('max num',maxNum)
        #print(myarray.index(maxNum), chr(myarray.index(maxNum)))
        #translated = replaceLetter(chr(myarray.index(maxNum)),translated)

#print translated
ar1 =[]
for h in range(MAX_KEY_SIZE):
    #print('index is',myarray[h])
    ar1.append([h,myarray[h]])
#print(ar1)
matchArray=[]
for k in range(28):
    matchArray.append([arr.pop(0),FreqArr.pop(0)])
print('match arr now:', matchArray)
#print(myarray)
newSt =list(msg)
for s in range(len(msg)):
    print('my array',myarray[s], msg[s])
    n = ord(msg[s])
    if myarray[n]>7:
        print('selected : ',matchArray.index(n))
        #newSt[s]=matchArray[s][1]
    else:
        newSt[s]= msg[s]
        #print('newST:', newSt)

print('result', newSt)
