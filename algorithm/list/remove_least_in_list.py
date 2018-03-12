#-*- coding: utf-8 -*-
"""
https://programmers.co.kr/learn/challenge_codes/121
리스트 내에서 가장 작은 숫자를 없앤 리스트를 반환하기
"""
def rm_small(mylist):
    import sys
    least = sys.maxsize # max number
    index = -1
    for i, x in enumerate(mylist):
        if least > x:
            least = x
            index = i
    mylist.pop(index)
    return mylist
