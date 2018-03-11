#-*- coding: utf-8 -*-

def hello():
    print("안녕".encode('utf-8'))

# hello()



def getStartingPoints(s):
    arr = []
    for x in range(0, len(s)-1):
        if s[x-1] == s[x+1] or s[x] == s[x+1]:
            arr.append(x)
    return arr

# print(getStartingPoints(s1))

def getPalindrome(s, start):
    length = 1
    maximum = len(s)-1
    minimum = -1
    isEven = False
    while True:
        if (start-length >= minimum or start == 0) and (start+length <= maximum):
            if start-length >= 0 and s[start-length] == s[start+length]: # odd
                isEven = False
                length += 1
            elif s[start-length+1] == s[start+length]: # even
                isEven = True
                length += 1
            else:
                break
        else:
            print("hello", maximum)
            break

    length -= 1
    if isEven:
        print(start, length)
        # print(s[start-(length-1):start+length+1])
        return Palindrome(start, 2*length, True)
    else:
        # print(start, length)
        # print(2*(length-1)+1)
        # print(s[start-length:start+length+1])
        return Palindrome(start, (2*length)+1, False)

def getOdd(s, start):
    length = 1
    minimum = 0
    maximum = len(s) - 1
    while start-length >= minimum and start + length <= maximum and s[start-length] == s[start+length]:
        length += 1
    return 2*(length-1)+1

def getEven(s, start):
    length = 1
    minimum = 0
    maximum = len(s) - 1
    while start-length+1 >= minimum and start + length <= maximum and s[start-length+1] == s[start+length]:
        length += 1
    return 2*(length-1)

class Palindrome:
    def __init__(self, starting_point, length, isEven):
        self.starting_point = starting_point
        self.length = length
        self.isEven = isEven

def solution(s):
    candidate = None
    arr = []
    for startingPoint in getStartingPoints(s):
        result = getPalindrome(s, startingPoint)
        if candidate is None or result.length > candidate.length:
            candidate = result
    if candidate is None:
        return 0
    else:
        return candidate.length

def solution2(s):
    candidate = None
    arr = []
    for startingPoint in getStartingPoints(s):
        odd = getOdd(s, startingPoint)
        even = getEven(s, startingPoint)
        # print(startingPoint, ":", odd, even)
        result = 0
        isEven = False
        if odd > even:
            result = odd
        else:
            result = even
            isEven = True
        if candidate is None or result > candidate.length:
            candidate = Palindrome(startingPoint, result, isEven)

    if candidate is None:
        return 0
    else:
        return candidate.length

print(solution2('abcdcbaaa'))
print(solution2(''))
print(solution2('abba'))

print(solution2('aaaaa'))
print(solution2('azzaa'))
print(solution2('aazbzaaazbzaa'))
print(solution2('aabbbcccdddd'))
print(solution2('abcdaa'))
print(solution2('abcdaaa'))
print(solution2('abcdaaaa'))
print(solution2('abcdaaaab'))
print(solution2('abcdaaaabbbb'))
print(solution2('xxxxxxxxxx'))
print(solution2('xxxxxxxxxxx'))
print(solution2('xxxxxxaxxxxx'))
print(solution2('abbaabba'))
print(solution2('abbacabbaabba'))
print(solution2('abababab'))
