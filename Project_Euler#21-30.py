#Project Euler #21-30

#Non-abundant sums | #23
#https://projecteuler.net/problem=23

def sumfindDivisors(n):
    i = 1
    result = []
    while i <= (n**.5):
        if n % i == 0:
            if (n / i == i):
                result.append(i)
            else:
                result.append(i)
                a = n/i
                result.append(a)
        i+=1
    result.remove(n)#Just for this problem
    result = sum(result)
    return result



maxN = 28123
abundantNumsA = []


#generate abundant
for num in range(2,maxN):
    if sumfindDivisors(num) > num:
        abundantNumsA.append(num)
abundantNumsB = abundantNumsA

sumAbun = set()
for a in abundantNumsA:
    for b in abundantNumsB:
        if b >= a:
            c = a+b
            sumAbun.add(c)
print(1)
result = 0
for num in range(2,maxN):
    if num not in sumAbun:
        result+=num
        print(num)
print(result)









'''
#Amicable Numbers | #21
#https://projecteuler.net/problem=21
import time
start = time.time()
def sumDivisors(n):
    numDivisors = [x for x in range(1,n) if n%x == 0]
    return sum(numDivisors)
maxNum = 10000
result = 0
i = 100
for numA in range(100,maxNum,2):
    if numA % 100 == 0:
        print(time.time()-start)
    sumNumA = sumDivisors(numA)
    if sumNumA > numA and sumNumA <= maxNum:
        sumNumB = sumDivisors(sumNumA)
        if sumNumB == numA:
            result+=sumNumB+sumNumA
print(result)
#This took some work
'''