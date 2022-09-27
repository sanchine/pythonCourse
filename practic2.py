# list split join

# methods

def oneSpace(str):
    return ' '.join(str.split())

def mathStr(str):
    l = list(str.split())
    print(l)
    res = 0

    for i, elem in enumerate(l):
        
    
    return res
        
def countWords(s):
    s = s.split()
    return len(s)
            
def stars(s):
    vowel = ["a", "e", "i", "o", "u", "y"]
    s2 = list(s)

    for i, elem in enumerate(s2):
        if elem in vowel:
            s2[i] = "*"
    return "".join(s2)
        
def removeFromStr(s, N):
    s2 = s.split()
    ls = []
    for elem in s2:
        if len(elem) >= N:
            ls.append(elem)

    return " ".join(ls)

def twinList(l1, l2):
    resL = []

    if len(l1) != len(l2):
        return "Bad input! Lists must be have equal length!"

    for i, elem in enumerate(l1):
        resL.append([l1[i], l2[i]])
    return resL

# main
s = "hello   e rrrr a   wassup bonjour\t\t\twhat?"

# N1
print("Task N1")
print(oneSpace(s))

# N2
print("Task N2")
mStr = '5 + 6 - 19'
print(mathStr(mStr))

# N3
print("Task N3")
print(countWords(s))

# N4
print("Task N4")
s2 = "hello"
print(stars(s2))

# N5
print("Task N5")
s3 = "something count has around pip i node react"
print(removeFromStr(s3, 5))

# N6
print("Task N6")
l1 = [1, 2, 3]
l2 = [5, 6, 7]
print(twinList(l1, l2))