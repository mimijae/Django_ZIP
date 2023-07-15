## 메인영역 모듈화 하기

## 다대일 관계 구현하기

다대일 관계는 여러개의 모델이 하나의 모델에 연결되는 관계를 말한다.
블로그를 예를 들어 설명하자면 블로그 사용자로 등록된 사람은 A,B,C 3명이다.
이들은 각자 여러개의 포스트를 작성할 수 있다. 세명의 사용자는 각각의 서로다른 갯수의 포스트를 작성한다고 하면 정보를 담기위해선 Post모델에 작성자가 누구인지 담을수 있는 필드가 있어야하고 , 각 필드에는 하나의 사용자 정보만 담을 수 있다.
즉 포스트와 작성자의 관계는 다 대 일이다

작성자 정보하나에 여러 포스트를 연결하는 다대일 관계에는 ForeignKey를 활용하면 된다

### 방법1. ForeignKey로 연결된 다른 모델의 레코드가 삭제 되었을때 함께 삭제되는 방식

User 모델을 사용해야 하므로 from django.contrib.auth.models import User로 User를 임포트한다. User는 장고에서 기본적으로 제공하는 모델이다.

User를 사용해 author필드를 만드는데 on_delete=models.CASCADE는 포스트의 작성자가 데이터베이스에서 삭제 되었을때 이 포스트도 같이 삭제한다는 의미이다

### 방법2. 연결된 사용자가 삭제되면 빈칸으로 두기

on_delete=models.SET_NULL을 사용하면 이 포스트의 작성자가 데이터베이스에서 삭제 되었을때 작성자명을 빈 칸으로 둔다는 의미이다. null=Ture를 추가해주어야 에러가 없다

### 포스트 목록 페이지와 포스트상세 페이지에 author 반영하기

{{ p.author|upper }}

## 카테고리 기능 구현하기

포스트는 하나의 카테고리만 지정할수 있다. 반대로 카테고리에는 여러개의 포스트가 포함될 수 있다. 포스트와 카테고리도 포스트와 작성자처럼 다대일 관계이다. 이역시 ForeignKey로 구현 가능하다.

```python
from django.contrib.auth.models import User
from django.db import models
import os

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=200,unique=True,allow_unicode=True)

    def __str__(self):
        return self.name
```

Category 모델에는 name과 slug라는 이름의 필드를 만들었다. name은 각 카테고리의 이름을 담는 필드이다. unique=Ture로 설정하면 동일한 name을 갖는 카테고리를 또 만들 수 없다. slug필드를 만들때 사용한 SlugField는 사람이 읽을 수 있는 텍스트로 고유 URL을 만들고 싶을 때 주로 사용한다

- Category모델도 Post모델 처럼 pk(premary key)를 활용해 URL을 만들수 있지만 카테고리는 포스트만큼 개수가 많지 않을 것 이므로 사람이 읽고 그뜻을 알 수 있게 고유 URL을 사용한다

name필드와 마찬가지로 unique=True가 있고 SlugField는 한글을 지원하지 않지만 allow_unicode=True로 설정해 한글로도 만들수 있게 한다

## Post모델에 category 필드 추가

카테고리가 미분류인 포스트도 있을 수 있으므로 null=True로 한다
그리고 ForeignKey로 연결되어 있던 카테고리가 삭제된 경우 연결된 포스트까지 삭제 되지않고해당 포스트의 category 필드만 null이 되도록 on_delete=models.SET_NULL로 설정한다

```python
category=models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
```

## admin.py에 Category 모델 등록하기

admin.py

```python
from django.contrib import admin
from .models import Post, Category

admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category,CategoryAdmin)
```

Post모델을 등록할 때와는 다르게 CategoryAdmin이라는 클래스도 추가로 만든다
그리고 prepopulated_fields = {'slug': ('name',)}으로 지정한다. 이렇게 하면 Category 모델의 name필드에 값이 입력됐을때 자동으로 slug가 만들어 진다.

### get_context_data()메서드로 category 관련 인자 넘기기

ListView나 DetailView와 같은 클래스는 기본적으로 get_context_data 메서드를 내장하고 있다. ListView를 상속 받은 PostList에서 단지 model = Post 라고 선언하면 get_context_data 에서 자동으로 post_list = Post.objects.all()을 명령한다
그래서 list.html에서 {% for p in post_list %}와 같은 명령어를 바로 활용 할 수 있다
이제 get_context_data를 정의해 오버라이딩한 다음 몇가지 정보를 추가해보자
