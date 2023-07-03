# Django_ZIP

## 장고 특징
- Python 웹 프레임워크
- MTV 디자인 패턴
- 오픈 소스
- 앱(App)단위로 프로젝트 구성
    - 앱이란 장고 프로젝트 구성하는 모듈을 의미
    - 장고 프로젝트 관점에서 관련된 기능을 모아둔 파이썬 파일
    - 앱 이름은 영문 복수형으로 생성
    - ![Alt text](images/%EC%9E%A5%EA%B3%A0%EC%BA%A1%EC%B3%901.png)

## 장고 핵심 요소
![Alt text](images/%EC%9E%A5%EA%B3%A0%EC%BA%A1%EC%B3%902.png)

### ORM
- Object-Relational Mapping
- 객체지향 언어와 관계형 데이터베이스를 연결해주는 기술
- 장고 자체에 ORM이라는 기술이 내장되어있음
- Models, QuerySet API 등이 ORM에 포함

### Templates
- 자체 템플릿 시스템으로 디자인과 로직을 분리하여 독립적 개발 가능
- HTML 파일을 분리하여 재사용, 체계적으로 관리할 수 있음
- HTML 파일에 include,if,for 등 템플릿 언어를 사용가능
  
### Forms
- 데이터의 유효성 검사
- 구성하고자 하는 형태 렌더링(HTML태그 생성)
- 제출하는 폼 데이터의 변경 확인

### Authentication
- 시스템 인증과 권한부여 기본 제공
- 인증과 권한의 차이
- 인증: 사용자가 누구인지 판별
- 권한: 인증된 사용자가 어떤 일을 할 수 있는지 결정
- 구성요소 : 사용자, 권한, 그룹(권한을 둘 이상 적용하는 방법)

### Admin
- 관리자 인터페이스 제공
- 등록된 모델의 기본적인 조회,추가,수정,삭제 기능제공(CRUD)
- 사용자 관리, 사용자 그룹관리, 사용자 별 권한 기본 제공

### Internationalization(국제화)
- 동일한 소스코드로 텍스트의 번역,날짜/시간/숫자의 포맷, 타임존의 지정 등 가 같은 다국어 환경 제공
- 개발자와 템플릿 작성자는 언어 및 문화에 맞게 번역하거나 형식 지정 가능
- 특정 사용자의 기본 설정에 따라 웹 앱을 현지화화


### Security
- 대표적인 보안사항 기능 제공
  - CSRF(교차 사이트 요청 위조)보호
  - 호스트 헤더 유효성 검사
  - SQL 주입 보호
  - 리퍼러 정책
  - XSS(교차 사이트 스크립팅)보호
  - 교차 출저정책
  - 클릭재킹 방지
  - 세션 보안
  - SSL/HTTPS

## 장고의 기본 구조
![Alt text](images/%EC%9E%A5%EA%B3%A0%EC%BA%A1%EC%B3%903.png)

![Alt text](images/%EC%9E%A5%EA%B3%A0%EC%BA%A1%EC%B3%904.png)

![Alt text](images/%EC%9E%A5%EA%B3%A0%EC%BA%A1%EC%B3%905.png)

Model과 Template는 선택사항이다

View만으로도 요청받고 응답할수도있다

## manage.py
 -> 장고한테 명령어를 쓸수있도록 하는 파이썬 파일이다(직접적으로 건들지는 않음)

## config.py 
-> 실무에서 현업을 할때에는 유지보수가 유리하게 config라는 이름을 붙힘


명령어로만든 폴더나 파일들은 자신이 임의로 건들면 안된다.
-  ex) manage.py config.py

## config.py 안에
__init__.py가 있다는것은 파이썬 패키지다 라고 약속되어있는 것이다

## settings.py
장고가 실행되어짐에 있어서 설정값들이 다 들어가있다

장고 프로젝트가 실행될때 필요한 변수, 값들이 들어와있다


## urls.py
urls.py 파일 안에 url이 정이가 되어야 view가 그 코드를 받아 실행할수있다

## models.py, migrations
데이터를 정의하고 정의한 데이터를 기반으로 데이터베이스를 만들때 기록을 남기는것을 migrations폴더

## admin.py
관리자 인터페이스를 제공해주는 파일

## views.py
컨트롤러 역할을하는 비즈니스로직이다.

# ※앱을 만들면 무조건 앱을 추가해주어야한다
![Alt text](images/%EC%9E%A5%EA%B3%A0%EC%BA%A1%EC%B3%906.png)

settings.py 파일에 있는 
저부분에 앱을 무조건 추가시키고 ,(콤마) 까지 붙혀야한다