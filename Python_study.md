# 파이썬 기초문법

※파이썬은 인터프리터 언어


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

```python 
print("나는 %d 살 입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요. " % 20)
# %s 사용하면 다 출력가능

# 방법1
print("나는 %s색과 %s색을 좋아해요." %("파란","빨간"))

# 방법2

print("나는 {}색과 {}색을 좋아해요." .format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란","빨간"))

# 방법3
print("나는 {age}살이며 {color}색을 좋아해요." .format(age=24,color="빨간"))

# 방법4
age = 20
color = "빨간"
print(f"나는 {age}살이며 {color}색을 좋아해요.")
```

## 탈출문자
```python
# \n : 줄바꿈
print("백문이 불여일결 \n 백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩"입니다.
print("저는 '나도코딩'입니다.")
print("저는\"나도코딩\"입니다.")
print("저는\'나도코딩\'입니다.")

# \\ " 문장내에서 \
print("C:\\Users\\Nadocoding\\desktop\\Pyhonworkspace")

# \r : 커서를 맨 앞으로 이동
```

### Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com    
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙 3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글 자내 'e' 갯수 + "!"로 구성
예) 생성된 비밀번호 : nav51!

```python
url = "http://naver.com"

python = url.replace("http://","") # 규칙1

python = python[0:python.index(".")] # 규칙2

password = "{}{}{}!".format(python[0:3], len(python), python.count("e")) #규칙3

print("{0}의 생성된 비밀번호는 {1} ".format(url,password))

```
![Alt text](<images/파이썬 예제 출력4.png>)

## 리스트

```python
subway = [10,20,30]
print(subway)

subway=["유재석", "조세호", "박명수"]
print(subway)

#조세호씨가 몇번째 칸에 타고 있는가?
print(subway.index("조세호"))

#하하씨가 다음 정류장에서 다음칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1,"정형돈")
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list=[5,4,3,2,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

 #모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호",20,True]

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

```

## Dictionary

```python
cabinet = {3:"유재석",100:"김태호"}
print(cabinet[3])
# 대괄호를 써서 키의 값을 가져올때는 키가 없을때는 오류가발생하여 프로그램을 강제종료한다
print(cabinet.get(3))
# 하지만 get을 쓰면 프로그램을 강제종료시키지않고 None을 출력한다

print(cabinet.get(3,"사용가능"))

print(3 in cabinet) # True

# 새 손님
cabinet["c-20"]="조세호"

# 간 손님(삭제)
del cabinet["유재석"]

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

#모든값 삭제
cabinet.clear()
```

## 튜플

```python
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

(name,age,hobby) = ("김종국", 20, "코딩")
print(name,age,hobby)
```

 ## Set
 ```python
# 집합(set)
# 중복 안됨, 순서없음

my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

java = {"유재석","김태호","양세형"}
python=set(["유재석","박명수"])

#교집합(java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (java 할 수 있거나 python 할수 있는 개발자)
print(java|python)
print(java.union(python))

# 차집합(java 할수 있지만 python은 할 줄 모르는 개발자)
print(java- python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
# java를 까먹음
java.remove("김태호")
 ```

Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
--축하합니다--

```python
from random import *
users=range(1,21)
users=list(users)

shuffle(users)

winners = sample(users,4) # 4명을 추출

print("치킨 {0}".format(winners[0]))
print("커피 {0}".format(winners[1:]))
```

## if

```python
weather = input("오늘 날씨는 어때요?") # input은 문자열을 입력받음

if weather =="비" or weather =="눈":
    print("우산을 챙기세요")
elif weather =="미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요없어요")

temp = int(input("기온은 어때요? "))
if 30<=temp:
    print("너무 더워요")
elif 10<= temp and temp <30:
    print("괜찮은 날씨에요")
elif 0<= temp <10:
    print("괜찮은 날씨에요")
else:
    print("너무 추워요")

```

## for , while , continue , break 


for
```python
for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no))

# 대기번호 : 0
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4

for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))

# 대기번호 : 0
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4

for waiting_no in range(1,6):
    print("대기번호 : {0}".format(waiting_no))

# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4
# 대기번호 : 5

starbucks = ["아이언맨","토르","그루트"]

for customer in starbucks:
    print("{0} 커피 준비됐습니다".format(customer))
```

while
```python
customer ="토르"
person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person=input("이름이 어떻게되세요?")

```

continue, break
```python
absent = [2,5] # 결석
ni_book = [7]
for student in range(1,11):
    if student in absent:
        continue # continue는 아래 코드들을 실행시키지 않고 다음 반복으로 계속 진행함
    elif student in ni_book:
        print("오늘 수업 여기까지 {0}는 교무실로 따라와".format(student))
        break # 바로 반복문을 끝냄
    print("{0} 책을 읽어봐".format(student))

```

한줄 for
```python
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101,102,103,104
students=[1,2,3,4]
students= [i+100 for i in students]
print(students)

#학생 이름을 길이로 변환
students=["Iron man","Thor","I am groot"]

students=[len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students=["Iron man","Thor","I am groot"]
students=[i.upper() for i in students]
print(students)
```

Quiz
```python
from random import *

cnt=0 # 총 탑승 승객수 

for i in range(1,51): #1~50 이라는 수 (승객)
    time=randrange(5,51)# 5분에서 50분 시간 소요
    if 5<=time<=15: # 5~15 분 이내 손님 매칭 성공 탑승 승객 수 증가
        print("[0] {0}번째 손님 (소요시간 :{1})".format(i,time))
        cnt+=1
    else: # 매칭 실패
        print("[] {0}번째 손님 (소요시간 :{1})".format(i,time))

print("총 탑승 승객 : {0}".format(cnt))
```

## 함수
```python
def open_account():
    print("새로운 계좌가 생성되었습니다")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance >=money:
        print("츨금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다 잔액은 {0} 입니다".format(balance))
        return balance
    
def withdraw_night(balance, money):
    commssion=100
    print("{0}".format(balance-money-commssion))
    return commssion, balance-money-commssion


balance =0
balance = deposit(balance,1000)
# balance = withdraw(balance,2000)
# balance = withdraw(balance,500)

commssion, balance=withdraw_night(balance,500)
print(commssion, balance)

```

### 기본값, 키워드값
```python
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t 나이: {1} \t 사용언어: {2}".format(name,age,main_lang))

profile("유재석")

def profile2(name, age, main_lang):
    print("이름 : {0}\t 나이: {1} \t 사용언어: {2}".format(name,age,main_lang))

profile(name="유재석",age=17,main_lang="파이썬")
profile(age=17,name="유재석",main_lang="파이썬")
```
### 가변인자
 - 서로다른 인수의 값을 넣어줄때 가변인자를 사용함
```python
# 가변인자
def profile3(name, age, *language):
    print("이름 : {0}\t 나이: {1} \t ".format(name,age), end=" ")
    for lang in language:
        print(lang,end=" ")
    print()

profile3("유재석", 20, "Python", "Java", "C", "C++","C#","JavaScript")

profile3("김태호",25,"Kotlin","Swift")
```
 Quiz)
 ```python
def std_weight(height,gender):
    if gender == "남자":
        return height*height*22
    elif gender == "여자":
         return height*height*21

height = 175
gender="남자"
weight=round(std_weight(height/100,gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다".format(height,gender,weight))
 ```

 ### 표준입출력
 ,가 들어간자리에 들어감
 ```python
print("python","Java","JavaScript", sep=" vs ")
# python vs Java vs JavaScript
 ```

다양한 출력포맷
![Alt text](images/%EC%BD%94%EB%93%9C%EC%BA%A1%EC%B3%901.png)
![Alt text](images/%EC%BD%94%EB%93%9C%EC%BA%A1%EC%B3%902.png)

소수점 출력
```python
print("{0:f}".format(5/3))
#1.666667

# 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))
#1.67
```

 ### 파일 입출력

파일 50개를 쉽게 만들수 있음

 Quiz) 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다. 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

 - X 주차 주간보고
 - 부서 :
 - 이름 :
 - 업무 요약 :
 - 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오
 - 조거건: 파일명은 '1주차.txt', '2주차.txt',... 와 같이 만듭니다.
  
```python
for i in range(1,51):
    with open(str(i)+"주차.txt","w",encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")
```
## 클래스

init
```python
class Unit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp = hp
        self.damage=damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

marin1=Unit("마린",40,5)
marin2=Unit("마린",40,5)
tank=Unit("탱크",150,35)
```

### 멤버변수
```python
wraith1 = Unit("레이스",80,5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
```

### ※파이썬은 외부에서 클래스의 멤버변수를 생성할수있다
```python
wraith2 = Unit("빼앗은레이스",80,5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))
```

### 메소드
```python
 # 공격유닛
class AttackUnit:
    def __init__(self, name,hp, damage):
        self.name=name
        self.hp=hp
        self.damage=damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name,location,self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp<=0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃",50,16)
firebat1.attack("5시")

firebat1.damaged(25)

firebat1.damaged(25)

```



### 상속,다중상속(상속하는 부모클래스가 2개이상)

```python
class Unit:
    def __init__(self,name,hp):
        self.name=name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name,hp, damage):
        Unit.__init__(self,name,hp)
        self.damage=damage

# 날수있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name,location,self.flying_speed))

# 공중 공격 유닛 클래스

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage,flying_speed):
        AttackUnit.__init__(self,name, hp, damage)
        Flyable.__init__(self,flying_speed)

valkyrie = FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"3시")
# 발키리 : 3시 방향으로 날아갑니다. [속도 5]
```
![Alt text](images/%EA%B7%B8%EB%A6%BC%EC%BA%A1%EC%B3%901.png)


## 메소드 오버라이딩

```python
class Unit:
    def __init__(self,name,hp,speed):
        self.name=name
        self.hp = hp
        self.speed=speed
    def move(self, location):
        print("[지상유닛]")
        print("{0} : {1} 방향으로 갑니다. [속도 {2}]".format(self.name,location,self.speed))

class AttackUnit(Unit):
    def __init__(self, name,hp, speed,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage=damage

# 날수있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name,location,self.flying_speed))

# 공중 공격 유닛 클래스

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage,flying_speed):
        AttackUnit.__init__(self,name, hp, 0,damage) # 지상 스피드 0
        Flyable.__init__(self,flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


vulture = AttackUnit("벌쳐",80,10,20)
battlecruiser = FlyableAttackUnit("배틀 크루저", 500,25,3)

vulture.move("11시")
battlecruiser.move("9시")

```

![Alt text](images/%EC%BD%94%EB%93%9C%EC%BA%A1%EC%B3%903.png)


![Alt text](images/%EA%B7%B8%EB%A6%BC%EC%BA%A1%EC%B3%904.png)

## pass
일단 그냥 넘어 가는것
```python
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot = BuildingUnit("서플라이 디폿",500,"7시")

def game_start():
    print("알림 새로운 게임을 시작합니다.")

def game_over():
    pass


game_start()
game_over()

```

## super

상속 2가지 버전

원래
```python
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        Unit.__init__(self,name,hp,0)
        self.location=location
```
super

차이점 : ()를 붙혀야하고 self를 안써도됨
```python
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name,hp,0)
        self.location=location
```
class FlyableUnit(Flyable, Unit):
 def __init__(self):
  super().__init__()
위처럼 다중 상속 코드를 작성했을 때, super() 를 쓰면 순서상 맨 "마지막" 이 아닌, 맨 "처음" 클래스(예제에서는 Flyable) 에 대해서 _init_ 함수가 호출 됩니다.

다중상속을 할때에는 super를 권장하지 않음


## 상속추가
```python
class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self,"탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.seize_mode ==False:
            print("{0}: 시즈모드로 전환합니다.".format(self.name))
            self.damage*=2
            self.seize_mode=True

        else:
            print("{0}: 시즈모드로 해제합니다.".format(self.name))
            self.damage/=2
            self.seize_mode=False

```
이 객체가 특정클래스의 인스턴스인지 확인하는 함수
isinstance(,)
```python 
for unit in attack_units:
    if isinstance(unit,Marine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()
```

![Alt text](images/%EA%B7%B8%EB%A6%BC%EC%BA%A1%EC%B3%905.png)

### Quiz

```python
class House:
    def __init__(self, location, house_type,deal_type, price,completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)


H1=House("강남", "아파트", "매매", "10억","2010년")
H2=House("마포","오피스텔","전세","5억","2007년")
H3=House("송파","빌라","월세","500/50","2000년")

house=[]
house.append(H1)
house.append(H2)
house.append(H3)

print("총 {0}대의 매물이 있습니다.".format(len(house)))

for i in house:
    i.show_detail()

```

## 예외처리
```python
try:
    print("나누기 전용 계산기입니다")
    nums=[]
    nums.append(int(input("첫 번재 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))  
    nums.append(int(nums[0]/nums[1]))
    print("{0}/{1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("잘못된 입력입니다")
except ZeroDivisionError as arr:
    print(arr)
except Exception as err:
    print(err)

# 에러 발생시키기
try:
    print("나누기 전용 계산기입니다")
    nums=[]
    nums.append(int(input("첫 번재 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))  
    nums.append(int(nums[0]/nums[1]))
    if nums[0] >= 10 or nums[1] >= 10:
        raise ValueError
    print("{0}/{1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("잘못된 입력입니다")


# 사용자정의 예외처리
class BigNumberError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

# 에러 발생시키기
try:
    print("나누기 전용 계산기입니다")
    nums=[]
    nums.append(int(input("첫 번재 숫자를 입력하세요: ")))
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))  
    nums.append(int(nums[0]/nums[1]))
    if nums[0] >= 10 or nums[1] >= 10:
        raise BigNumberError("{0} {1}".format(nums[0],nums[1]))
    print("{0}/{1} = {2}".format(nums[0],nums[1],nums[2]))   
except ValueError:
    print("잘못된 입력입니다")
except BigNumberError as arr:
    print("잘못된 입력입니다")
    print(arr)
finally:
    print("계산이 완료되었습니다") # 무조건 실행되는 문장
```

## Quiz

Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
대기 손님의치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다
시스템 코드를 확인하고 적절한 예외처리구문을 넣으시오.

조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
출력 메시지 "잘못된 값을 입력하였습니다"
조건2: 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
치킨 소진 시 사용자 정의 에러 [SoldOutError]를 발생시키고 프로그램 종료
출력 메시지 "재고가 소진되어 더이상 주문을 받지 않습니다"


```python
class SoldOutError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
    


chicken =10
waiting = 1
while(True):
    try:
        print("[남은 치킨] : {0}".format(chicken))
        order = int(input("치킨 몇 마리 주문 하시겠습니까?"))
        if order > chicken:
           print("재료가 부족합니다")
        elif order <=0:
            raise ValueError
        else:
            print("대기번호 [{0}]:{1} 마리 주문이 완료되었습니다".format(waiting,order))
            waiting = waiting + 1
            chicken = chicken - order

        if chicken == 0:
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
    except ValueError:
        print("잘못된 값을 입력하였습니다")
    except SoldOutError as arr:
        print(arr)
        break
```


