# 문제 설명

- 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
- s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
- 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 
- 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

- 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

## 제한사항
- 문자열 s의 길이 : 50 이하의 자연수
- 문자열 s는 알파벳으로만 이루어져 있습니다.
# 입출력 예
|s|answer|
|--|--|
|"pPoooyY"|true|
|"Pyy"|false|

## 입출력 예 설명
### 입출력 예 #1
- 'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.

### 입출력 예 #2
- 'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.

---

# 풀이과정

## 내 풀이
```python
def solution(s):
    s = s.lower()       # 대, 소 유무 관계없이 카운트되어 소문자로 통일해 진행
    num = 0             # 숫자로 +1, -1 로 p와 y 개수를 계산하였음.
    for st in s:
        if st == 'p':   # p 일 경우 num + 1
            num += 1
        elif st == 'y': # y 일 경우 num - 1
            num -= 1
    if num == 0:        # num = 0 -> True / num != 0 -> False
        return True
    else:
        return False
```

## 다른 사람 풀이

```python
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
```
- 집계함수를 이용하여 p와 y 개수를 비교
- 이 방법이 가장 효율적인 것 같음!