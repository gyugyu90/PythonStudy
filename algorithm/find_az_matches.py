"""
문자열 내에서 'a와 z' 혹은 'z와 a' 사이에 다른 a나 z가 없는 쌍이 몇개 있는지 찾는 문제
'az' ==> 1개
'zza' => 1개
'abcde' => 0개
'abczeaz' => 3개
"""

def solution(s):
    result = 0
    for i in range(len(s)):
        if s[i] == 'a':
            z_index = s.find('z', i+1)
            a_index = s.find('a', i+1)
            if (z_index != -1 and a_index == -1) or a_index > z_index and z_index != -1:
                result += 1
        elif s[i] == 'z':
            a_index = s.find('a', i+1)
            z_index = s.find('z', i+1)
            if (a_index != -1 and z_index == -1) or (a_index < z_index and a_index != -1):
                result += 1
    print("result:", result)

solution('zz')
solution('hello')
solution('abcz')
solution('zabzczxa')
solution('abcd')
solution('abcdzz')
solution('abcdzaz')
solution('za')
solution('abz')
solution('zczxa')
