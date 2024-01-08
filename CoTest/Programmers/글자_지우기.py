'''
문제 설명
문자열 my_string과 정수 배열 indices가 주어질 때, my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

제한사항
1 ≤ indices의 길이 < my_string의 길이 ≤ 100
my_string은 영소문자로만 이루어져 있습니다
0 ≤ indices의 원소 < my_string의 길이
indices의 원소는 모두 서로 다릅니다.

예시
my_string    ->    "apporoograpemmemprs"	
indices      ->    [1, 16, 6, 15, 0, 10, 11, 3]
result       ->    "programmers"
'''

# 풀이
def solution(my_string, indices):
    str = list(my_string)    # 먼저 문자열(my_string)을 리스트로 만들어준다.
    for i in indices:
        str[i] = '-'         # 문자열에서 제거해야할 문자를 '-'로 변환해준다.
    li = [value for value in str if value != "-"]  # li라는 리스트를 새로 만들어 리스트에서 '-'가 아닌 값만 담아준다. 
    # for value in str:
    #     if value != '-':        => 이런 뜻이라고 생각하면 됨.
    #         li.append(value)
    return ''.join(li)       # 리스트를 다시 문자열로 바꿔줌.

# 다른 풀이
'''
def solution(my_string, indices):
    answer = '' 
    for i in range(len(my_string)):
        if i not in indices:answer+=my_string[i]
    return answer

-> 빈 문자를 만들어서 indices에 걸리지 않는 문자만 더하도록 해서 문제를 풀음
'''

# 배운 것
'''
1. .join() 매서드에 대해서 배움
(문자 사이에 넣을 것).join(합칠 리스트, 딕셔너리 등등...)
2. 2개 이상의 조건/반복문이 결합된 리스트 컴프리헨션
-> 이건 직접 해봐야 할듯함.
'''
