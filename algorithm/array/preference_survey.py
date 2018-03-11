"""
선호도 조사 문제
[1, 3]은 '1번 직원이 3번을 선호한다'는 조사결과
array 내에서 서로 선호하는 관계찾기
"""

survey1 = ([1,3],[3,1],[3,5],[2,5],[5,3])

count = 0
survey_dict = {}
for element in survey1:
    if "{0}-{1}".format(element[1], element[0]) in survey_dict:
        count += 1
    else:
        survey_dict.update({"{0}-{1}".format(element[0], element[1]):0})
        print("{0}-{1}".format(element[0], element[1]))
print(survey_dict)
print(count) # return this!
