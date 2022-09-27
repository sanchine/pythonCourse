####### funcs

def max1(arr):
    maxD = arr[0]
    for i in arr:
        if maxD < i:
            maxD = i
    return maxD

def longerStr(strs, n):
    for i in strs:
        if len(i) > N:
            print(i)

def honestDigits(arr):
    honestArr = []
    for i in arr:
        if i % 2 == 0:
            honestArr.append(i)
    return honestArr

def honestAndOddDigits(arr):
    oddDigits = []
    for i in arr:
        if i % 2 != 0:
            oddDigits.append(i)
    return honestDigits(arr), oddDigits

def factorial(factorialN):
    fact = 1
    for i in range(1, factorialN - 1):
        fact *= i
    return fact


####### main

arr = [1, 2, 33333333, 4, 5, 6, 7, 2222]

print(max1(arr))

strings = ['a', 'ab', 'more', 'much more']
N = 5

longerStr(strings, N)

print(honestDigits(arr))
print(honestAndOddDigits(arr))

print(factorial(4))