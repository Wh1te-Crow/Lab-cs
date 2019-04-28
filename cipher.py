from random import choice, randint
import math

def randomNumberGenerator(len):
    number = str()
    for i in range(len-2):
        number += str(choice([0, 1]))
    number = ''.join(('1', number, '1'))
    return int(number,2)


def randomPrimeNumber(len):
    num = randomNumberGenerator(len)
    while not testMillerRabin(num):
        num+=2
    return num

def generateKeys(len): 
    p = randomPrimeNumber(len)
    q = randomPrimeNumber(len)
    n = p*q
    oiler = oilerFunction(p, q)
    e = randint(2, oiler-1)
    while  advancedEuclideanAlgorithm(e,oiler)[0] != 1:
        e = randint(2, oiler-1)
    d = advancedEuclideanAlgorithm(e,oiler)[1]%oiler
    rezult = {}
    rezult['e'] = e
    rezult['n'] = n
    rezult['d'] = d
    return(rezult) 

def oilerFunction(p, q):
    return (p-1)*(q-1)

def testMillerRabin(p):    # k = 20
    temp_p = p-1           
    s=0
    while temp_p%2 == 0:
        temp_p //= 2
        s += 1
    d = temp_p
    x = 0
    for i in range(20):
        x = randint(2, p-1)
        if advancedEuclideanAlgorithm(x, p)[0] == 1:
            if pow(x, d, p) == 1 or pow(x, d, p) == (-1)%p:
                continue
            else:
                for r in range (1, s):
                    xr = pow(x, d*pow(2,r), p)
                    if xr == (-1)%p:
                        return True
                    elif xr == 1:
                        return False
                    else:
                        continue
                return False
        elif advancedEuclideanAlgorithm(x, p)[0] > 1:
            return False
    return True

def advancedEuclideanAlgorithm(num1, num2):   # u*num1 + v*num2 = gcd(num1, num2)
    if(num2==0):
        return (num1, 1, 0)
    else:
        (greatestCommonDivisior, u, v) = advancedEuclideanAlgorithm(num2, num1 % num2)
        return (greatestCommonDivisior, v, u - num1//num2*v)

def encrypt(message, e, n):
    c = pow(message, e, n)
    return c

def decrypt(c, d ,n ):
    m = pow(c, d, n)
    return m

