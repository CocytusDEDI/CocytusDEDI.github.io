import random

prime = []
stringNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# randomly picks prime numbers
def pickPrimes():
    correct = False
    while correct == False:
        max = input('largest possible number (from 3): ')
        booleanPList = [characters in stringNumbers for characters in max]
        if all(booleanPList) == True:
            max = int(max)
            if max > 2:
                correct = True
            else:
                print('invalid')
        else:
            print('invalid')
    prime.clear()
    for num in range(2, max):
        if all(num % i != 0 for i in range(2, num)):
            prime.append(num)
    p = random.choice(prime)
    q = random.choice(prime)
    return p, q

# checks if p and q are primes from user input
def isPrime(p, q):
    checked = False
    max = 1000
    loop = 0
    while checked is False:
        prime.clear()
        for num in range(2, max):
            if all(num % i != 0 for i in range(2, num)):
                prime.append(num)
        if int(p) in prime and int(q) in prime:
            return True
        elif p > max or q > max:
            if loop < 3:
                max = max + 1000
            elif loop < 10:
                max = max + 100000
            elif loop < 20:
                max = max + 100000000000
        else:
            return False

        loop = loop + 1

# loop till randomising prime numbers or picking prime numbers is chosen
def menu():
    chosenPrimeChoice = False
    while chosenPrimeChoice is False:
        primeChoice = input('input or randomise: ').lower().strip()
        if primeChoice == 'input':
            p = input('choose p (prime number): ')
            q = input('choose q (prime number): ')
            booleanPList = [characters in stringNumbers for characters in p]
            booleanQList = [characters in stringNumbers for characters in q]
            if all(booleanQList) == True and all(booleanPList) == True:
                if isPrime(p, q) is True:
                    chosenPrimeChoice = True
                    p = int(p)
                    q = int(q)
                else:
                    print('numbers not prime')
                    print('')
            else:
                print('not number')
        elif primeChoice == 'randomise':
            p, q = pickPrimes()
            chosenPrimeChoice = True
        else:
            print('invalid option')
            print('')
    return p, q

# gets the amount of numbers that have common factors with N
def CalcCoprimesOfN(p, q):
    CoPrimesAmountOfN = (p - 1) * (q - 1)
    return CoPrimesAmountOfN

# N is p times q
def N(p, q):
    n = p * q
    return n

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1


# the first number in the public key (public key used for encryption)
def E(N, CoPrimesOfN):
    optionsForE = []
    optionsForEToRemove = []
    # condition one: 1 < e < CoPrimesOfN
    for option in range(2, CoPrimesOfN):
        optionsForE.append(option)
    # condition two: e can't share common factor with N (has to be CoPrime)
    CoPrimeWithN = []
    for option in optionsForE:
        if is_coprime(option, N) == True:
            CoPrimeWithN.append(option)
    # condition three: e can't share common factor with CoPrimesOfN
    for option in optionsForE:
        if is_coprime(option, CoPrimesOfN) == True:
            if option in CoPrimeWithN:
                e = option
    return e


def D(e, CoPrimesOfN):
    found = False
    i = 1
    times = 0
    repeatTimes = random.randrange(1, 100)
    while not found:
        step = i * e
        form = step % CoPrimesOfN
        if form == 1:
            #return i
            if times == repeatTimes:
                return i
            times = times + 1
        i = i + 1

def DFast(e, CoPrimesOfN):
    found = False
    i = 1
    while not found:
        mutiple = e * i
        step = mutiple * e
        form = step % CoPrimesOfN
        if form == 1:
            return i
        i = i + 1

# making keys
p, q = menu()
n = N(p, q)
CoPrimesOfN = CalcCoprimesOfN(p, q)
e = E(n, CoPrimesOfN)
publicKey = e, n
d = D(e, CoPrimesOfN)
privateKey = d, n
print('public key:', publicKey)
print('private key:', privateKey)

# encryption or decryption
def encryption(text, e, n):
    # text into numbers
    numberText = []
    for character in text:
        numberText.append(ord(character))
    # encrypt numbers
    encyptedNumber = []
    for number in numberText:
        encyptedNumber.append(((number ** e) % n))
    return encyptedNumber

def decryption(encoded, d, n):
    numberList = []
    for number in encoded:
        numberList.append(((number ** d) % n))
    text = ''
    for number in numberList:
        text = text + chr(round(number))
    return text

print(decryption(encryption('hi', e, n), d, n))