'''
문제 설명
정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

제한사항
1 ≤ n ≤ 1,000,000
1 ≤ k ≤ min(1,000, n)

입출력 예
n = 10 /	k = 3	/ soltion = [3, 6, 9]
n =  15 /	k = 5	/ soltion = [5, 10, 15]

입출력 예 설명

입출력 예 #1
1 이상 10 이하의 3의 배수는 3, 6, 9 이므로 [3, 6, 9]를 return 합니다.

입출력 예 #2
1 이상 15 이하의 5의 배수는 5, 10, 15 이므로 [5, 10, 15]를 return 합니다.
'''

# 풀이과정
def solution(n, k):
    answer = []    # 배수를 담을 수 있는 빈 리스트를 만든다.
    num = 1        # n의 배수로 증가하기 떄문에 num을 k * num 을 사용하여 표시한다.
    while n >= k * num:    # while문을 이용하여 k 배수가 n 보다 작다면 자동으로 크기가 커지게 설정하였음.
        answer.append(k * num)
        num += 1
    return answer    # n의 배수가 k를 넘으면 answer 리스트를 출력함.

# 다른 풀이
def solution(n, k):
    return [i for i in range(k,n+1,k)]    # range(시작값, 끝값, 간격)을 활용하여 문제를 해결하였음.
