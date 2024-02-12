#Sorry that i make that by 1 file , it was more easily to call all functions in the in.py
#I tried to separate them by spaces and commnets

from itertools import * #for 5th 
import math
import random # for 13th

# 1
def toOunces(gramm):
    return 28.3495231 * gramm

# print(toOunces(30))
# 2
def toCel(F):
    return (5/9 * (F-32))

# print(toCel(300))
# 3
def solve(numheads, numlegs):
    rab = (numlegs - numheads*2 )/2
    kur = numheads - rab
    return [rab , kur]

# print(solve(35,94))
#  4
def isPrime(x):
    if x == 1:
        return False
    d = 2
    while x % d != 0 and pow(d,2) < x:
        d+=1
    if x % d == 0:
        return False
    else: 
        return True

def filterPrime(li):
    return list(filter(isPrime,li))

# print(filterPrime(([1, 3, 2,5 , 20, 21])))

#5 
def per():
    s = input()
    print(' '.join(map(lambda x: ''.join(x), permutations(s))))
# per()

#6
def rev():
    s = input()
    p = ''
    i = s.__len__()
    while i != 0:
        i-=1
        p+=s[i]
    print(p)
# rev()
        
#7
def check(li):
    i = 0
    while i != li.__len__() :
        if li[i] == 3 and i+1 != li.__len__() :
                if li[i+1]==3 :
                    return True #Not sure about this one// it becomes an error because i < li.len()
        i+=1
    return False
# print(check([3, 1, 3]))

#8 

def checkSpy(li):
    i = 0
    while i != li.__len__() : #Yep, only while,no for 
        if li[i] == 0:
            k = i
            while k != li.__len__():
                if li[k] == 0:
                    o = k
    
                    while o != li.__len__():
                        if li[o] == 7 :
                            return True    
                        o+=1
                k+=1
        i+=1
    return False
# print(checkSpy([1,7,2,0,4,5,0]))

#9
def volume(rad):
    return (4/3)*math.pi* ( rad * rad * rad)
# print(volume(4))

#10 

def uniq(li):
    li1 = []
    for i in li:
        if i not in li1:
            li1.append(i)
    return li1
# print(uniq([1,1,1,5,7]))

#11

def isPalindrom(s):
    i = 0
    while i != math.ceil(s.__len__() / 2):
        if s[i] != s[s.__len__()-i-1]:
            return False
        i+=1
    return True
# print(isPalindrom('asdsa'))

#12
def histogram(li):
    for i in li:
        for k in range(i):
            print('*',end='')
        print()
# histogram([1,5,9])


#13 my game

print('Hello! What is your name?')
name = input()

print(f'Well, {name}, I am thinking of a number between 1 and 20.')
print('Take a guess.')

myNum = random.randint(1, 20)

def low():
    print('Your guess is too low')
    print('Take a guess.')

def up():
    print('Your guess is too high.')
    print('Take a guess.')

cnt = 1
while True:
    num = int(input())
    if num == myNum:
        print(f'Good job,{name}! You guessed my number in {cnt} guesses!')
        break
    if num < myNum:
        low()
    if num > myNum:
        up()
    cnt +=1