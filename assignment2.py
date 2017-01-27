
def getMessage():
    return open('encode-ex.txt.enc', 'r').read()

def readMessage(msg):
    counter =0
    textCounter = 0
    translate =''
    for symbol in msg:
        textCounter +=1
        myArray.append(ord(symbol))
        if (ord(symbol)>256):
            #print ('unichr is: ',symbol, 'in position ', textCounter)
            translate += ' '
        else:

            num = (ord(symbol) - key) % 256
            if chr(num) == 'e':
                #myArray.append(textCounter)
                #print('there is a e in key',key,' character number ', textCounter)
                counter +=1
            translate += chr(num)
   # print(counter)

        # if counter% 4 == 0:
        #     #print('the symbol number ', counter,' in ascii is: ',ord(symbol) )
        #     num = (ord(symbol)-(32-key))%126
        #     #print('translated to ', chr(num))
        #     #print('charecter number :' , textCounter)
        #     myArray.append(chr(num))
        #
        # elif counter == 11:
        #     counter =0
        # else: counter += 1
    return translate


message = getMessage()
key =1
myArray = []
# for term in 'Hello, Faezeh Siavashi!':
#     print('ascci code for ', term, 'is : ', ord(term))
while key<256:
    print ('----------------------------------------',key ,'----------------------------------------------------------')
    print(readMessage(message))
    key +=1

print(myArray)
