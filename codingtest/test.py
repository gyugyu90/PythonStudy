#-*- coding: utf-8 -*-

def hello():
    print("안녕".encode('utf-8'))

# hello()


s1 = 'abcdcbaaa'
def getStartingPoints(s):
    arr = []
    for x in range(1, len(s)-1):
        if s[x-1] == s[x+1]:
            arr.append(x)
    return arr

print(getStartingPoints(s1))
