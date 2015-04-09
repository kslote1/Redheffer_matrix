import math


# check that n is in N \{0}.
def isValid (n):
    if (n <=0):
        return 0
    elif (n-int (n) != 0):
        return 0
    return 1

#The Mobius function .
def mu (n):
    if not isValid (n):
        return 0
    elif (n ==1):
        return 1
    # Important to chech this first .
    elif ( isDivisibleBySquare (n)):
        return 0
    else :
        #As n is not divisible by a square ,
        # every power of a prime is equal to one.
        #Hence , the number of factors is correct .
        return ( -1)** numberOfFactors (n)

def mertens(n):
    sum = 0
    for i in xrange(1, n+1):
        sum += mu(i)
    return sum

# Check if n is divisible by a square .
def isDivisibleBySquare (n):
    i = 2
    while (i**2 <=n):
        if (n%(i **2)==0):
            return 1
        i += 1
    return 0

# Count the number of prime factors of n.
def numberOfFactors (n):
    counter = 0
    while (n >1):
        i = 2
        while (i <=n):
            if (n%i ==0):
                n /= i
                counter += 1
                break
            i += 1
    return counter

#The summation of mu(n).
#mu (1)=1 , 0 otherwise .
def sumOfMu (n):
    d = 1
    muSum = 0
    while (d <=n):
        if (n%d ==0):
            muSum += mu(d)
        d += 1
    return muSum

#The number of numbers smaller than or
# equal to n which is relatively prime to n
def phi (n):
    if not isValid (n):
        return 0
    if (n ==1):
        return 1
    else :
        for i in range (2 ,n +1):
            if ((n%i) == 0 and isPrime (i)):
                n *= (1 - (1.0 / i))
        return int (n)

# Check if a numer is prime or not
def isPrime (n):
    return not (n < 2 or any (n % i == 0 for i in range (2 , int (n **0.5)+1)))

#The summation of phi(n).
#The sum over the divisors
#is equal to n.
def sumOfPhi (n):
    d = 1
    phiSum = 0
    while (d <=n):
        if (n%d ==0):
            phiSum += phi (d)
            d += 1
    return phiSum

#The natural function
# which return the input
def N (n):
    if not isValid (n):
        return 0
    return n

#The identity function .
#I(1)=1 , 0 otherwise
def I (n):
    if n ==1:
        return 1
    return 0



