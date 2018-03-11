"""
개미 수열 만들기 (Look and say sequence)
1
11 (1이 한 개)
12 (1이 두 개)
1121 (1이 한 개, 2가 한 개)
122111 (1이 두 개, 2가 한 개, 1이 한 개)
and goes on...
"""

def antSequence(s):
    length = len(s)
    bufferValue = ""
    count = 0
    result = ""
    for i in range(length):
        if bufferValue == "":
            count = 1
            bufferValue = s[i]
        else:
            if bufferValue == s[i]:
                count += 1
            else:
                result += "{0}{1}".format(bufferValue, count)
    print(result)

def makeAntSequence(size):
    # size는 몇 번째 개미수열까지 가져올 것인지?
    s = "1"
    arr = [s]
    result = ""

    for i in range(size):
        j = 0 # 다음 문자를 찾으러 다닐 index
        length = len(s)
        while j < length:
            bufferString = s[j]
            count = 1
            while j+1 < length and bufferString == s[j+1]:
                count += 1
                j += 1
            result += "{0}{1}".format(bufferString, count)
            j += 1
        arr.append(result)
        s = result # 다음 문자열로
        result = "" # 초기화
    return arr[size-1]

print(makeAntSequence(5))
