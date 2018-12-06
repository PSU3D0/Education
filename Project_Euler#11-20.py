#Project Euler #11-20

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