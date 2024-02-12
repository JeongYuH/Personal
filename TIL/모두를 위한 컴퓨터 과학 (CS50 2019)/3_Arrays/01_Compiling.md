# 1. 컴파일링

# 들어가기 전에

- 우리가 작성한 C 코드를 실행하기 위해서는 컴파일링을 해줘야 합니다. 
- C문법로 작성된 텍스트 형식의 파일은 컴파일링시 구체적으로 어떤 단계를 거쳐서 컴퓨터가 해석 가능한 파일로 변환될까요?

## 학습 목표

- 컴파일링의 네 단계를 설명할 수 있습니다.

## 핵심 단어

- 컴파일링
- 어셈블링
- 링킹

---

# 강의 듣기

지금까지는 아무것도 모른채 마구잡이로 쓴 코드가 잘 돌아갔다면 이제부터 연습과 응용을 통해 동작 원리를 이해

첫 수업에 봤던 예제를 다시 살펴보며 지금 사용하는 방법이 우리가 사용한 방법과 어떻게 다른지 알아봅시다.

## Code 1
```c
#include <studio.h>     

int main(void)
{
    printf('hello world\n');
}
```

### 명령어 설명

- studio.h
    - 프로그래밍에 필요한 여러 함수들이 정의되어 있는 라이브러리
    - 다른 사람이 작성한 파일로 'studio.h'는 c 언어로 작성된 '.h'로 끝나는 파일
        - printf에 대한 설명이 들어가 있어 Clang 컴파일러 실행시 명령어를 이해하게 하는 역할 수행


- '~\n'
    - 다음 줄로 넘어가도록 하는 명령어(파이썬과 동일)

- main 
    - 프로그램의 시작점으로써 실행 버튼을 클릭하는 것과 같습니다.

- printf -> python에서의 print 함수와 동일
    - printf는 출력을 담당하는 함수
    - printf 함수를 사용하기 위해서는 stdio.h 라이브러리가 필요


---

### Compile

#### Case 1
```cmd
clang hello.c
./a.out
```
- 설명
    1. hello.c 파일을 clang으로 컴파일
    2. a.out 파일 실행(컴파일된 파일의 이름-> 자동 설정값인듯?)

#### Case 2
```cmd
clang -o hello hello.c
./hello
```
- 설명
    1. '-o hello' 구문은 컴파일된 파일의 이름을 변경
    - 'a.out' 이 아닌 'hello' 라는 파일명으로 저장되도록 설정

---

## Code 2
```c
#include <cs50.h>     
#include <studio.h>

int main(void)
{
    string name = get_string("What's your name?\n");
    printf("hello %s/n", name);
}
```

### 명령어 설명

- cs50.h 
    - 추가적인 명령어를 쓸 수 있는 라이브러리
    - 이 경우, string과 get string을 선언할 수 있게 해줌.

- string name
    - string
        - 데이터의 종류
        - get_string 함수는 이 데이터 형에서 파생되는 함수임
        - python에서 input에 문자열을 넣는 경우

    - name
        - 변수
    
    - string 데이터형의 name 이라는 변수를 선언

- %s 
    - 형식 지정자
    - 들어가야 하는 변수의 형식을 지정함(이 경우에는 'name')

### Compile

#### Case 1

```cmd
clang -o hello hello.c -lcs50
./hello
```
- 이전 방식과 동일하나, 뒤에 추가적인 명령어가 삽입되어야 함.
- '-lcs50'
    - 'cs50.h' 라이브러리를 사용하기 위해서 clang에 추가해야함.
    - 앞에 위치한 '-l'은 link의 약어로, cs50을 연결하라는 의미임.

#### Case 2
```cmd
make hello
./hello
```
- 위에서 언급한 것들을 한방에 해결해주는 명령어
    - 자동으로 컴파일링을 실행하고, 파일을 만들어서 실행함.

- 파이썬을 쓰게 되면, 컴파일링은 필요하지 않음.
---


## 프로그램 실행의 4가지 단계

: 다음과 같은 4 단계로 구성됨
- Preprocessing
- Compiling
- Assembling
- Linking

- 예시(Code 2) -> hello.c 파일
```c
#include <cs50.h>     
#include <studio.h>

int main(void)
{
    string name = get_string("What's your name?\n");
    printf("hello %s/n", name);
}
```
### 1. Preprocessing
```c
#include <cs50.h>     
#include <studio.h>
```
- clang이 '#' 영역에 해당하는 코드를 파일에서 가져와서 내용을 붙여줌
    - 라이브러리를 사용할 수 있도록 한다고 이해하면 됨
    - python의 import 구문과 동일함

### 2. Compiling
- 소스코드를 머신코드로 변환하는 단계
- 코드가 clang에 의해서 컴파일
    - C로 작성된 코드는 어셈블리 언어로 변환됨

- 어셈블리 언어
    - 기계어에 보다 가까운 언어
    - cpu가 이해하는 기초적 언어
        - c 언어보다 이해하기 어려운 방식으로 수행됨(알 필요는 없음.)
        - **clang이 이 모든 과정을 수행하주기 때문**

### 3. Assembling
- 어셈블리 코드를 입력받아서 머신 코드로 변환하는 과정
- clang이 어셈블리 코드를 0과 1로 구성된 머신코드(기계어)로 변환함.

### 4. Linking
- hello.c 코드 외에도 다른 파일들 또한 기계어로 변환하는 과정을 거침.
- 라이브러리를 완전히 변환한 후에 모든 파일들을 하나의 파일로 결합
- 해당 파일이 바로 a.out / hello 가 됨.


**이 모든 과정들을 결합하여 Compiling이라고 부르게 됨**
