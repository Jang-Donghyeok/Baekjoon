import random

def getRandom(A,B):
    n = random.randint(ord(A),ord(B))
    print(chr(n))
def getRandomLower():
    n = random.randint(97,122)
    print(chr(n))
def getRandomUpper():
    n = random.randint(65,90)
    print(chr(n))
def getRandomDigitCharacter():
    n = random.randint(0,100)
    print(n)
def getRandomASCII():
    n = random.randint(32,127)
    n = chr(n)
    print(n)

A = input("문자를 입력하시오.")
B = input("문자를 입력하시오.")

getRandom(A,B)
getRandomLower()
getRandomUpper()
getRandomDigitCharacter()
getRandomASCII()

