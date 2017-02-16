# Author: Faezeh Siavashi
# Date: Feb ?? 2017
#***********************************
# Method: Monoalphabetic
# Alphabet: ASCII table, all of 256 symbols
# Data Type: text


6.587998E7  

MAX_KEY_SIZE = 256
FreqArr=['e','t','a','o','i','n','s','h','r','d','l','u']#,'c','m','f','y','w','g','p','b','v','k','x','q','j','z']

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
    # for i in range(len(arr)):
    #     print(chr(myarray.index(arr[i])))
    print('array of sorted letter',arr)



msg = getFile()
myarray = []
arr = []
orderedletter= ''
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
    #print('index',myarray[h], h)
    ar1.append([h,myarray[h]])
#print(ar1)
matchArray=[]
for k in range(len(myarray)):
    matchArray.append([arr[k],chr(myarray.index(arr[k]))])
print('match arr now:', matchArray)
#print(myarray)



print('ëm is :',msg.count('ëm'))
print('vv is: ', msg.count('vv'))
print('mv is :', msg.count('mv'))
print('vë is :',msg.count('vë'))
print('Ãm is :',msg.count('Ãm'))
print('vm is :', msg.count('vm'))
print('vvm is :', msg.count('vvm'))
print('ê  is :', msg.count('ê '))
print('ëmë is :', msg.count('ëmë'))

print('vvmv is :', msg.count('vvmv'))

result=''
for m in msg:
    if m == 'm':
        result+= 't'
    elif m== 'ë':
        result += 'q'
    elif m == 'ê':
        result += 'h'
    elif m == ' ':
        result += 'e'
    # elif m == '°':
    #     result += 'n'
    # elif m == '¡':
    #     result += 's'
    # elif m == '@':
    #     result += 'h'
    # elif m == '!':
    #     result += 'd'
    # elif m == '\x19':
    #     result += 'l'
    # elif m == ' ':
    #     result += 'c'
    # elif m == 'Ã':
    #     result += 'w'
    # elif m == '\x10':
    #     result += 'w'
    # elif m == 'e':
    #     result += 'w'
    else:
        result +=m

digraphsList= []
numbers=[]
for i in range(len(msg)-1):
        if msg[i]+msg[i+1] not in digraphsList:
            digraphsList.append(msg[i]+msg[i+1])
            digraphsList.append(msg.count(msg[i] + msg[i + 1]))
            numbers.append(msg.count(msg[i] + msg[i + 1]))

print('dig',digraphsList)
print('numbers', numbers)

trigraphsList= []
numbers2=[]
for i in range(len(msg)-2):
        if msg[i]+msg[i+1]+msg[i+2] not in trigraphsList:
            trigraphsList.append(msg[i]+msg[i+1]+msg[i+2])
            numbers2.append(msg.count(msg[i] + msg[i + 1]+msg[i+2]))
            trigraphsList.append(msg.count(msg[i] + msg[i + 1]+msg[i+2]))


print('tri', trigraphsList)
print('numbers2', numbers2)
# result2=''
# for m in result:
#     if m == 'ë':
#         result2+='r'
#     else:
#         result2 +=m

#result.replace('eê ', 'ent')

print(result)
