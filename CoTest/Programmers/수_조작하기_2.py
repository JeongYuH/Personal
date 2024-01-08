'''
문제 설명
정수 배열 numLog가 주어집니다. 처음에 numLog[0]에서 부터 시작해 "w", "a", "s", "d"로 이루어진 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.

"w" : 수에 1을 더한다.
"s" : 수에 1을 뺀다.
"d" : 수에 10을 더한다.
"a" : 수에 10을 뺀다.
그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다. 즉, numLog[i]는 numLog[0]로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.

주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성해 주세요.
'''
'''
풀이 접근
- 가장 먼저 코드를 보고 어떤식으로 해야하는지 고민하다가 n번째 위치의 값을 구한다는 가정으로 접근함
=> n 번째 위치의 값 => numLog[i] - numLog[i - 1] 이 되므로 for loop를 활용하여 두 값의 차(변화값) 구함.

- 마지막으로 첫번째 값은 -1이 출력되어 계산이 이상해지므로 이를 막기 위해서 첫 값은 continue로 넘김.
'''


# 정답(내가 풀은 정답)
def solution(numLog):
    solution = ''
    for i in range(len(numLog)):
        if i == 0:  # 첫 번째 항목에 대한 예외 처리
            continue
        if numLog[i] - numLog[i - 1] == 1:
            solution += 'w'
        elif numLog[i] - numLog[i - 1] == -1:
            solution += 's'
        elif numLog[i] - numLog[i - 1] == 10:
            solution += 'd'
        elif numLog[i] - numLog[i - 1] == -10:
            solution += 'a'
    return solution

# 리스트 컴프리핸션을 사용한 답
def solution(numLog):
    return ''.join(['w' if numLog[i] - numLog[i - 1] == 1
                    else 's' if numLog[i] - numLog[i - 1] == -1
                    else 'd' if numLog[i] - numLog[i - 1] == 10
                    else 'a' if numLog[i] - numLog[i - 1] == -10
                    else '' for i in range(1, len(numLog))])
# 최종적으로 컴프리핸션을 쓸 수 있도록 노력하자.
