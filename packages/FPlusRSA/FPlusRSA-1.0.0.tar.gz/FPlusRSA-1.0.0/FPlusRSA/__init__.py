import secrets
import math

def RSA_encrypt(data:str,pubic_key:tuple):#the pubic_key[1] is must greater than every coding number of data's character
    encrypted = []
    for i in range(len(data)):
        code = ord(data[i])
        code = code**pubic_key[0]
        code = code%pubic_key[1]
        encrypted.append(code)
    return encrypted

def RSA_decode(data:list,private_key:tuple):
    decoded = ""
    for i in range(len(data)):
        code = data[i]**private_key[0]
        code = code%private_key[1]
        code = chr(code)
        decoded += code
    return decoded

def is_prime(n:int):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True  

def get_pubic_key(p:int,q:int):
    N = p*q
    T = (p-1) * (q-1)
    run = True

    s = secrets.SystemRandom()
    while run:
        r = s.randrange(2, T-1)
        if T%r != 0 and is_prime(r):
            run = False

    E = (r,N)
    return E

def get_private_key(pubic_key:tuple,p:int,q:int):
    T = (p-1) * (q-1)
    run = True
    d = 0
    while run:
        d += 1
        if (d*pubic_key[0])%T == 1:
            run = False
    
    D = (d,pubic_key[1])
    return D

def get_random_prime(bits:int):
    if bits % 2 == 0 and bits >= 2:
        run = True
        while run:
            p = secrets.randbits(bits)
            if is_prime(p):
                run = False
        return p
    return 0

