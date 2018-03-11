#-*- coding: utf-8 -*-
"""
https://programmers.co.kr/learn/challenge_codes/77
최적의 행렬 곱셈

5*3행렬, 3*2행렬, 2*6행렬을 표현
(5,3)(3,2)(2,6)

동적 프로그래밍으로 풀어야
S(i, j) = i~j번째의 행렬 곱셈에 필요한 곱셈이라면
i<=k<=j-1인 임의의 k값에 대해서

S(i, j) = minimum(S(i, k) + S(k+1, j) + M) # M = (마지막곱셈) = (i-1번째 차수) * (k번째 차수) * (j번째 차수)
S(i, i) = 0 => 행렬 자기 자신은 곱셈이 필요가 없음

(5,3)(3,2)(2,6)에 대해서
S(1, 2) = minimum(S(1, 1) + S(2, 2) + M) = 30
S(2, 3) = minimum(S(2, 2) + S(3, 3) + M) = 36
S(1, 3) = minimum(S(1, 1) + S(2, 3) + M, S(1, 2) + S(3, 3) + M)
        = minimum(0 + 36 + 5*3*6, 30 + 0 + 5*2*6)
        = minimum(126, 90)
        = 90
"""

m0 = [[5, 3], [3, 2], [2, 6]]

def getMinMulti(matrix, i, j):
    if i == j:
        return 0
    else:
        array = []
        for k in range(i, j):
            minmulti = getMinMulti(matrix, i, k)
            minmulti += getMinMulti(matrix, k+1, j)
            minmulti += matrix[i][0] * matrix[k][1] * matrix[j][1]
            array.append(minmulti)
        return min(array)
print(getMinMulti(m0, 0, len(m0)-1))


m1 = [[5, 2], [2, 3], [3, 6], [6, 6], [6, 4], [4, 7], [7, 1], [1, 1], [1, 8], [8, 4]]
# 정답 : 176
# print(getMinMulti(m1, 0, 9))

m2 = [[2, 10], [10, 1], [1, 3], [3, 3], [3, 4], [4, 5], [5, 5], [5, 5], [5, 4], [4, 7]]
# 정답 : 173
# print(getMinMulti(m2, 0, 9))

m3 =  [[7, 6], [6, 3], [3, 5], [5, 5], [5, 3], [3, 5], [5, 10], [10, 1], [1, 5], [5, 6]]
# 정답 : 252
# print(getMinMulti(m3, 0, 9))

m4 =  [[7, 2], [2, 4], [4, 10], [10, 5], [5, 5], [5, 9], [9, 8], [8, 5], [5, 1], [1, 6]]
# 정답 : 336
# print(getMinMulti(m4, 0, len(m4)-1))
