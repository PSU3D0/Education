#Project Euler - Problems 1-10

#Largest Palindrome Product | #4
min = 100
max = 999
result = 0
for a in range(min,max):
    for b in range(min+1,max):
        prod = a*b
        if prod > result:
            prod = str(prod)
            if prod == prod[::-1]:
                result = int(prod)
print(result)










'''
#Largest Prime Factor | #3
#https://projecteuler.net/problem=3

import math

def primeFactors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n /= 2
    i=3
    while i <= math.sqrt(n):
        while n%i == 0:
            factors.append(i)
            n = n/i
        i+=2
    if n > 2:
        factors.append(n)
    return factors
    
userInput = int(input("Enter number to factorize:"))
print(primeFactors(userInput))
print('max: '+str(max(primeFactors(userInput))))
'''

'''
#Even Fibonacci Numbers | #2
#https://projecteuler.net/problem=2

def generateFib(maxRange):
    sequence = [1]
    a = 1
    b = 1
    while max(sequence) < maxRange:
        c = a+b
        sequence.append(c)
        a = b
        b = c
    return sequence
output = generateFib(4000000)
output = [x for x in output if x%2 == 0]
print(sum(output))
'''

'''
#Multiples of 3 and 5 | #1
#https://projecteuler.net/problem=1

multipleOf3 = [int(x) for x in range(1000) if x%3 == 0]
multipleOf5 = [int(x) for x in range(1000) if x%5 == 0]
print(sum(multipleOf3)+sum(multipleOf5))
'''