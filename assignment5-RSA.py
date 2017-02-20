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
    print('phi_n:', phi_N)
    d= modinv(e,phi_N)
    print('d is: ',hex(d))
    #decrypt(ct,d,n)
    #print('we have ',pow(ct,d)%n)



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

