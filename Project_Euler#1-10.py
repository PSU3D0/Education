#Project Euler - Problems 1-10

#Summation of Primes | #10
#https://projecteuler.net/problem=10
#Going for an actual sieve this time 

import math as m

#Creating boolean dict sequenced by nums 2-maxN
maxN = 2000000
l1 = dict()
for x in range(2,maxN):
    l1[x] = True
#Instantiating logic variables
j = 0
ctr = 1

#Count loop
ct = list(range(2,int(m.sqrt(maxN))))
#Sieve
for num in ct:
    if l1[num] == True:
        for key in l1.keys():
            if key % num == 0 and key != num:
                l1[key] = False
    
#Summation
Sum = 0
for i in l1.keys():
    if l1[i] == True:
        Sum += i
print(Sum)

#Executes in about 22 seconds, aka not efficient
#Just learned about enumerate() replaces all this dict nonsense
#Will fix in next commit




'''
# Special Pythagorean Triplet | #9
#https://projecteuler.net/problem=9
for a in range(0,1000):
    for b in range(a,1000-a):
        c = 1000 - a - b
        if a * a + b * b == c*c:
            print((a,b,c))
            print((a+b+c))
            print((a*b*c))
#Pythonic much?
'''

'''
#Largest Product in a Series | #8
#https://projecteuler.net/problem=8

num = str("""73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace("\n", ""))

store = 0

for a in num:
    indexA = num.index(a)
    a = int(a)
    if indexA < 986:

        i = 1
        determine = a
        while i < 12:
        
            determine *= int(num[indexA+i])
            i += 1
        if determine > store:
            store = determine
print(store)
'''



'''
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
print(primes[limit])9
'''

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