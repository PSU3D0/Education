#Project Euler - Problems 1-10

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
output = [sum(x) for x in output if x%2 == 0]
print(output)
print(sum(output))







'''
#Multiples of 3 and 5 | #1
#https://projecteuler.net/problem=1

multipleOf3 = [int(x) for x in range(1000) if x%3 == 0]
multipleOf5 = [int(x) for x in range(1000) if x%5 == 0]
print(sum(multipleOf3)+sum(multipleOf5))
'''