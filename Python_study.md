# 파이썬 기초

파이썬에서 주석은 # 그리고 여러문장을 주석하려면 ```으로 감싸야함

```python
age = 24
print(str(age)+"이민재")

# 또는

print(age,"이민재")

```

출력하려면 문자형으로 바꿀때 파이썬에선 str로 감싸는데 정수형뒤에 ','를 붙혀서도 할수있다.
,를 쓰면 뒤에 한글자 공백이 추가된다

## 연산자
```python
print(2**3) # 2^3=8

print(5//3) # 목만 구하고싶을때 1

print(5%3) # 나머지만 구하고싶을대 2

print(not(1 !=3)) # False

print((3>0) and (3<5)) # True

print((3>0) & (3<5)) #True

print((3>0) or (3<5)) # True

print((3>0) | (3<5)) #True

print(5 > 4 > 3) # True

print(5 > 4 > 7) # False

```

## 숫자처리함수

```python
print(abs(-5)) # 5 절댓값 함수
print(pow(4,2)) # 4^2
print(max(5,12)) # 12
print(min(5,12)) # 5
print(round(3.14)) # 3  반올림
print(round(4.99)) # 5

from math import * # math라이브러리에있는 모든걸 이용하겠다

print(floor(4.99)) # 내림 4
print(ceol(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 (루트) 4

```

## 랜덤함수

```python
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성

print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성

print(int(random()*10)) # 0~10 미만의 임의의 값 생성 

print(int(random()*10)+1) # 1~10 이하의 임의의 값 생성 

print(randrange(1,46)) # 1~46 미만의 임의의값 생성

print(randint(1,45)) # 1~45 이하의 임의의값 생성
```

### Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다. 월 4회 스터디를 하는데 3번은 온라인으로하고 1번은 오프라인으로 하기로 했습니다. 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오. 

조건1 : 랜덤으로 날짜를 봅아야함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 X 일로 선정되었습니다.

```python
from random import *

print("오프라인 스터디 모임 날짜는 매월"+str(randint(4,28))+"일로 선정되었습니다.")
```

## 문자열

```python
sentence = '나는 소년입니다'

sentence2 = "파이썬은 쉬워요"

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""

print(sentence3)

```
![Alt text](<images/파이썬 예제 출력1.png>)

## 슬라이싱 

```python
jumin = "990120-1234567"

print("성별 : " + jumin[7]) # 성별 : 1
print("연 : " + jumi[0:2])# 0부터 2 직전까지 (0,1)

print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지

print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지 

print("뒤 7자리 : " + jumin[-7:]) # 뒤에서부터 인덱스를셈 -1부터 시작
```
 ## 문자열 처리함수 

```python
python = "Python is Amazing"
print(python.lower()) # 문자열 전부 소문자로
print(python.upper()) # 문자열 전부 대문자로
print(python[0].isupper()) # 0번째 인덱스의 문자열이 대문자인가 Bool 이문장은 True
print(len(python)) # 문자열의 총 길이
print(python.replace("Python","Java"))
# 문자열 교체
index = python.index("n")# 해당 문자열의 인덱스 위치
print(index)
index = python.index("n", index + 1)#해당 문자열의 2번째 문자열의 인덱스 위치
print(index)

print(python.find("Java")) # 없다면 -1을 출력
print(python.index("Java")) # 없다면 오류를 출력 -> 프로그램이 종료됨
print(python.count("n")) # 문자열에서 n 이 몇번 등장하는지
```
![Alt text](<images/파이썬 예제 출력2.png>)
![Alt text](<images/파이썬 예제 출력3.png>)

## 문자열포맷

