# FPlusRSA

### Made by [FPlus Studio](https://ql27731117.icoc.ws)
## **Introduction**
This is a simple library,you can use it to implement encryption and decryption functions based on RSA encryption algorithm.
It contains six functions that require the introduction of the ```secrets``` library and the ```math``` library.

## **Usages of functions**
#### 1.```RSA_encrypt```
It has two parameters ```data:str``` and ```pubic_key:tuple```,the ```pubic_key:tuple``` has two ```int``` items,they are geted by function ```get_pubic_key```.In the end,it will return a encrypted list.
*The ```pubic_key[1]``` is must greater than every coding number of data's character,or the encrypted data will be wrong.*
#### 2.```RSA_decode```
It has two parameters ```data:list``` and ```private_key:tuple```,the ```private_key:tuple``` has two ```int``` items,they are geted by function ```get_private_key```.The ```data:list``` is the encrypted list from ```RSA_encrypt```.In the end,it will return a decoded string.
#### 3.```is_prime```
It is a internal functions,has one parameter ```n:int```.Ine the end,it will return a ```bool```.
#### 4.```get_pubic_key```
It has two parameters ```p:int``` and ```q:int```,they are must prime numbers.You can get them by function ```get_random_prime```.And in the end,it will return a tuple(the pubic key).
#### 5.```get_private_key```
It has three parameters ```pubic_key:tuple```,```p:int``` and ```q:int```,the ```p:int``` and ```q:int``` is the same as ```p:int``` and ```q:int``` of ```get_pubic_key```,the ```pubic_key:tuple``` is from ```get_pubic_key```,too.In the end,it will return a tuple(the private key).
#### 6.```get_random_prime```
It has one parameter ```bits:int```,the ```bits:int``` is must a even number and greater than 1.In the end,it will return a random prime number of ```bits:int``` bits.

## **A simple example**
```python
from FPlusRSA import *

#if you want to encrypt most languages normally,the parameter of get_random_prime() better be greater than 8
p = get_random_prime(10)
q = get_random_prime(10)

a = get_pubic_key(p, q)
b = get_private_key(a, p, q)

string = "hello world"
e = RSA_encrypt(string, a)
print(e)#encrypted data
d = RSA_decode(e, b)
print(d)#decoded data
```

## **Versions**
### `1.0.0` 
##### 1.Basic function implementation.