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
        while ct < (len(ln)-4):
            prod = product(ln[0+ct:4+ct])
            if prod > highestNum:
                highestNum = prod
                ct+=1
            else: ct+=1
    return highestNum

def diagProduct(data):
    #Products to right
    ct = 0
    for ln in data:
        while ct < (len(ln)-3):




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
diagProduct(data)