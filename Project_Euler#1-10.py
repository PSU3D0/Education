#Project Euler - Problems 1-10

#10001st Prime | #7
#https://projecteuler.net/problem=7

#Yes, this is not remotely efficient, will redo in future
l1 = list(range(2,500000))
limit = 10000
primes = []
p = 2
while len(primes) <= limit:
    l1 = [item for item in l1 if not item % p == 0]
    primes.append(p)
    if len(l1) != 1:
        p = min(l1)
print(primes[limit])


    
        
        



'''
#Sum Square Difference | #6
#https://projecteuler.net/problem=6

nums = list(range(1,100))
numsSummed = sum(nums)
numsSquared = sum([x**2 for x in nums])
sumSquareDiff = numsSquared - numsSummed
print (sumSquareDiff)
'''


'''
#Smallest Multiple | #5
#https://projecteuler.net/problem=5
a = 100000
i = 20
while i >=1:
    if a%i == 0:
        i -= 1
    else:
        i = 20
        a+= 2
print(a)
'''

'''
#Largest Palindrome Product | #4
#https://projecteuler.net/problem=4
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