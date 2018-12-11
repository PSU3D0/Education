# Factorial Digit Sum | #20
#https://projecteuler.net/problem=20

def sumFactorialResult(n):
    nums = list(range(1,n+1))
    factorial = 1
    result = 0
    
    for x in nums:
        factorial *= x
    factorial = str(factorial)

    for num in factorial:
        num = int(num)
        result+=num

    return result

print(sumFactorialResult(100))


'''
#Counting Sundays | #19
#https://projecteuler.net/problem=19
#Algorithm https://en.wikipedia.org/wiki/Zeller%27s_congruence

def zellerCongruence(q,m,K,J):
    #q=day of month, m=month, K=year of century, J=zero based century
    if m >= 13:
        K-=1
    h = q + ((13*(m+1))//5)
    h += K + (K//4) + (J//4) - 2*J
    h = h%7
    if h == 1:
        return 1
    else:
        return 0

#Using Zeller's Congruence
startYear = 1901
endYear = 2000
i = 0

numSundays = 0
while i < (endYear-startYear):
    m = 13
    n = 0
    while n < 12:
        numSundays+= zellerCongruence(1,m,((startYear+i)%100),((startYear+i)//100))
        m+=1
        n+=1
        if m ==15:
            m = 3
    i+=1

print(numSundays)
'''

'''
#Maximum Path Sum I | # 18
#https://projecteuler.net/problem=18

f = open('/home/psu3d0/Desktop/Programming Projects/Education/#18Data.txt')

#Love this line
data = [[int(i) for i in line.split()] for line in f]

sumTotal = 0
elementIndex = 0
for row in data:
    maxAdj = 0
    if len(row) == 1:
        sumTotal += row[0]
        maxIndice = 0
    else:
        for idx, el in enumerate(row):
            if el > maxAdj and idx == (elementIndex) or el > maxAdj and idx ==(elementIndex +1):
                maxAdj = el
                maxIndice = idx
    elementIndex = maxIndice
    sumTotal +=maxAdj


print(sumTotal)
'''
'''
#Number Letter Counts | #17
#https://projecteuler.net/problem=17

#Thank god for stackoverflow copypasting
numDict19 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
numDictDouble = {20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety'}
thousand = 'Thousand'

nList = list(range(1,1000))
strTotal = 0
for num in nList:
    #fast
    if num < 20:
        strTotal += len(numDict19[num])
    else:
        nStr = str(num)
        nLen = len(nStr)
        if nLen == 2:
            firstN,lastN = nStr[0],nStr[1]
            firstN,lastN = int(firstN),int(lastN)
            firstN *= 10
            strTotal += len(numDictDouble[firstN])
            if lastN != 0:
                strTotal += len(numDict19[lastN])
        elif nLen == 3:
            firstN,secondN = nStr[0],nStr[1:]
            firstN,secondN = int(firstN),int(secondN) 
            strTotal += len(numDict19[firstN]) + 7
            if secondN < 20 and secondN !=0:
                strTotal += len(numDict19[secondN]) + 3
            elif secondN >= 20 and secondN !=0:
                secondN = str(secondN)
                tenthP,oneP = secondN[0],secondN[1]
                tenthP = int(tenthP) * 10
                strTotal += len(numDictDouble[tenthP]) + 3

                oneP = int(oneP)
                if oneP != 0:
                    strTotal += len(numDict19[oneP])

print(strTotal)
'''


'''
#Power Digit Sum | #16
#https://projecteuler.net/problem=16

def powerDigitSum(num,exp):
    str(digits) = num**exp
    digits = str(digits)
    result = 0
    for n in digits:
        result+= int(n)
    return result

result = powerDigitSum(2,1000)
print(result)
'''


'''
#Lattice Paths | #15
#https://projecteuler.net/problem=15
import math as m
#Using simple binomial coefficient route
def determinePaths(latW,latH):
    n = latW+latH
    totalPaths = (m.factorial(n)) / (m.factorial(latH)*m.factorial(n-latH))
    return totalPaths

result = determinePaths(20,20)
print(result)
'''


'''
#Longest Collatz Sequence | #14
#https://projecteuler.net/problem=14

def findLongestCollatz(EndNumLim):
    end = EndNumLim - 1
    seqStart = 13
    highestSeq = 0
    while seqStart < end:
        seqCt = 1
        n = seqStart
        while n != 1:
            if n % 2 == 0:
                n = n/2
                seqCt +=1
            else:
                n = (3*n)+1
                seqCt +=1
        seqStart +=1
        if seqCt > highestSeq:
            highestSeq = seqCt
    return highestSeq

result = findLongestCollatz(1000000)
print(result)
'''
'''
#Largest Sum | #13
#https://projecteuler.net/problem=13


#Took longer than I thought
f = open('/home/psu3d0/Desktop/Programming Projects/Education/#13Data.txt')
result = 0
for line in f:
    n = line.split()
    n = n.pop()
    n = int(n)
    result = result + n

print(result)
'''


'''
#Highly Divisible Triangular Number | #12
#https://projecteuler.net/problem=12
def numFactors(n):
    if n == 0: return 0
    if n == 1: return 1
    i=1
    factorNum = 0
    while i <= (n**.5):
        if n%i ==0:
            if (n / i) == i:
                factorNum+=1
            else:
                factorNum+=2
        i+=1
    return factorNum
#My weakness is factorization! Took entire day to figure above method


def generateTriangleNums(divisorLimit):
    

    triNums = []
    numOfDivisors = 0
    while numOfDivisors < divisorLimit:
        numOfDivisors = 0
        triNums.append(sum(range(len(triNums)+1)))
        numOfDivisors = numFactors(max(triNums))
    return max(triNums)
        
value =generateTriangleNums(500)
print(value)
'''



'''
# Largest Product in a Grid | # 11
#https://projecteuler.net/problem=11

def product(nums):
    if 0 in nums: return 0
    result = 1
    for x in nums:
        result *= x
    return result

def gridProduct(data):
    #Works only for horizontal,vertical
    ct = 0
    highestNum = 0
    for ln in data:
        while ct < (len(ln)-3):
            prod = product(ln[0+ct:4+ct])
            if prod > highestNum:
                highestNum = prod
                ct+=1
            else: ct+=1
    return highestNum

def diagProduct(data,maxNum):
    #Products to right
    for ln in data:
        lnCount = data.index(ln)
        ct = 0
        i = 0
        while ct < (len(ln)-3) and lnCount <= 16 :
            lnIndex = data.index(ln)
            prod = []
            diagCt = 1
            prod.append(ln[0+ct])
            i = ct
            ct +=1
            while len(prod) < 4:
                prod.append(data[1+lnIndex][1+i])
                i+=1
                lnIndex+=1
            dResult = product(prod)
            if dResult > maxNum:
                maxNum = dResult
    #Products to left
    data = [row[::-1] for row in data]
    for ln in data:
        lnCount = data.index(ln)
        ct = 0
        i = 0
        while ct < (len(ln)-3) and lnCount <= 16 :
            lnIndex = data.index(ln)
            prod = []
            diagCt = 1
            prod.append(ln[0+ct])
            i = ct
            ct +=1
            while len(prod) < 4:
                prod.append(data[1+lnIndex][1+i])
                i+=1
                lnIndex+=1
            dResult = product(prod)
            if dResult > maxNum:
                maxNum = dResult
    return maxNum



data = []
highestNum = 0
#Read File and create 2d Array
f = open('/home/psu3d0/Desktop/Programming Projects/Education/#11Data.txt')
data = [[int(i) for i in line.split()] for line in f]


#Iterate Horizontally
hMax = gridProduct(data)

#Iterate vertically
vList = list(zip(*data))
vMax = gridProduct(vList)

#Iterate Diagonally
maxNum = max(hMax,vMax)
print(diagProduct(data,maxNum))
'''