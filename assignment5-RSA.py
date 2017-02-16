import sys
from Crypto.Cipher import DES



def decrypt(c,d,n):
    print('decrypted to: ',str(pow(c,d,n)), hex(pow(c,d,n)))


def main():
    n = int('0x94a7c088a228fc014e2b', 0)
    e = int('0x22ccc2836d856bb56d4f', 0)
    p = 959357020577
    q = 731745016907
    print("n is:", n, 'p*q:',p*q)
    ct= int('0x89382d8b2c0acc896952',0)
    print('cipher is:',ct )
    phi_N = (p - 1) * (q - 1)
    d= modinv(e,phi_N)
    print('d is: ',d)
    decrypt(ct,d,n)

    obj = DES.new(ct,DES.MODE_ECB)









    msg=142
    n1=143
    e1=7
    phi_N1= 120
    d1= modinv(e1,phi_N1)
    en = pow(msg,e1,n1)
    print('encrypt is:', en)
    decrypt(en, d1, n1)
    ###########################################################
    # p =11
    # q=13
    # e=7
    # phi_N= (p-1)*(q-1)
    # d= modinv(e,phi_N)
    # print('d is:', d)
    ###########################################################

    #cipherText = int('0x89382d8b2c0acc896952',0)
    print(phi_N)
    #gcd, a, b = egcd(e, phi_N)
    #gcd1, a1, b1 =egcd1(e, phi_N)
    #d1=a1
    #d = a
    #print("n:  " + str(d))
    #print("n1: "+ str(d1))

    # Decrypt ciphertext
    #pt = pow(cipherText, d, n)
    #print("pt: " + str(pt))

    #pt1= modinv(a,n)
    #print("pt1: "+str(pt1))


def egcd1(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd1(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd1(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m





if __name__ == "__main__":
    main()

