# 메인영역 모듈화 하기

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

## 다대다 관계 구현하기

여러 요소와 동시에 연결 될 수 있는 관계를 다대다 관계라고 한다
이런 관계를 장고로 구현하려면 ManyToManyField를 사용하면 된다

Post모델에 tags 필드를 추가
ForeingKey가 아니라 ManyToManyField를 사용해 Tag 모델을 연결
tags 필드를 빈 칸으로 남겨둘 수 있도록 null = True와 blank=True로 설정한다 하지만 on_delete=models.SET_NULL은 tag에선 설정하지 않는다. 그 이유는 연결된 태그가 삭제되면 해당 포스트의 tags필드는 알아서 빈칸으로 바뀌기 때문이다.

```python
tags = models.ManyToManyField(Tag, null=True,blank=True)
```

하지만 null has no effect on ManyToManyField. 라는 경고 메시지가 뜬다
ManyToManyFieldsms는 기본적으로 null=True가 설정되어 있어 따로 입력한 null=True는 효과가 없다는 의미입니다

```python
tags = models.ManyToManyField(Tag, blank=True)
```

이렇게 수정을 한다

- ManyToManyField로 만든 태그는 포스트와 다대다 관계를 가진다.
- 즉 하나의 포스트에 여러개의 태그와 연결 될 수 있고, 반대로 하나의 태그가 여러개의 포스트와 연결될수 있다. 이때 태그하나가 데이터베이스에서 삭제된다고해서 연결된 포스트가 전부 삭제되면 곤란해지기때문에 기본적으로 null=True로 설정 되어있다

이제 Tag도 admin.py에 등록시키자

admin.py

```python
from django.contrib import admin
from .models import Post, Category, Tag

admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category,CategoryAdmin)

admin.site.register(Tag,TagAdmin)
```

# 폼으로 포스트 작성과 수정 기능 구현하기

포스트 작성 페이지에는 방문자가 포스트의 제목과 내용 등을 입력 할 수 있고, 입력한 값을 서버로 전송해서 데이터 베이스에 저장 할 수 있는 빈 칸이 있어야 한다

웹 개발에서 이런 빈 칸을 폼(form)이라고 한다.

먼저 views.py 에 장고가 제공하는 CreateView를 상속 받아서 PostCreate라는 클래스를 만든다

model = Post 로 Post모델을 사용한다고 선언하고 Post 모델에 사용할 필드명을 리스트로 작성에서 fields에 저장한다

```python
from django.voew.generic import ListView, DetailView, CreateView
class PostCreate(CreateView):
    model = Post
    fields = ['title', 'hook_text','content','head_image','file_upload','category']
```

urls.py

```python
from .import views

urlpatterns = [
    path('create_post/',view.PostCreate.as_view()),
    path('tag/<str:slug>',view.tag_page),
    path('<int:pk>/', views.PostDetail.as_view()),
]
```

{% csrf_token %}는 웹사이트를 CSRF공격으로부터 보호하기 위해 장고가 제공하는 기능이다. 장고에서 폼을 이용할때는 {% csrf_token %}을 <form> 태그안에 꼭 넣어야한다

## 포스트를 로그인한 방문자만 작성할 수 있게 만들기

Post모델에서 author(writer)필드는 작성자 정보를 담는 필드 이므로 필수 항목이다.
로그인한 방문자에 한해 포스트 작성 페이지에 접근 할 수 있게 하면 자동으로 author필드를 채울수 있다. 만약 로그인한 사용자에 한해 글쓰기 권한을 부여하지 않는다면 어느날 악의적인 광고봇이 웹사이트를 스팸성 게시글로 도배해버릴수도 있다
따라서 로그인한 경우에만 포스트 작성 페이지에 접근이 가능하도록 수정하겠습니다.

### views.py 의 PostCreate에 LoginRequiredMixin 추가하기

PostCreate클래스에 매개변수로 LoginRequiredMixin 클래스를 추가하면 로그인 했을때만 정상적으로 페이지가 보이게 된다. LoginRequiredMixin은 장고에서 제공하는 클래스로 views.py에서 임포트하고 사용하면 된다.

view.py

```python
from django.contrib.auth.mixins import LoginRequiredMixin

Class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'hook_text','content','head_image','file_upload','category']
```

※Mixin 클래스로 추가 상속받기

- 이미 PostCreate 클래스는 장고가 제공하는 CreateView 클래스를 상속 받았는데, LoginRequiredMixin 클래스를 또 상속 받은 것 처럼 LoginRequiredMixin의 메서드로 사용하고있다. 이는 Mixin이라는 개념 때문에 가능하다
- 클래스에서 Mixin을 사용하면 다른 클래스의 메서드를 추가 할 수 있습니다. CBV로 뷰를 구성하는 경우에 로그인했을 때만 작동하는 LoginRequiredMixin을 장고에서 이미 제공하고 있으니 단순히 PostCreate에 추가하는 것 만으로 기능을 구현할 수 있다

## 자동으로 author 필드 채우기

author(writer)필드를 자동으로 채우기 위해 CreateView에서 제공하는 form_valid()를 활용

- CreateView는 form_valid()함수를 기본적으로 탑재하고 있음
- PostCreate 클래스는 CeateView를 상속받아 만들었으므로 PostCreate(커스터마이징)에서 제공한 폼에 사용자가 제대로 내용을 입력하면 form_valid()함수가 실행된다.
- form_valid()함수는 방문자가 폼에 담아 보낸 유효한 정보를 사용해 포스트를 만들고, 이 포스트의 고유 경로로 보내주는(redirect)역할을 한다

```python
from django.contrib.auth.mixins import LoginRequiredMixin

Class PostCreate(LoginRequiredMixin,CreateView):
    model=Post
    fields = ['title', 'hook_text','content','head_image','file_upload','category']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')
```

- self.request.user는 웹 사이트의 방문자를 의미한다. 웹 사이트의 방문자가 로그인한 상태인지 아닌지는 is_authenticated로 알수있다
- 로그인을 한 상태라면 form에서 생성한 instance(새로 생성한 포스트)의 author필드에 current_user(현재 접속한 방문자)를 담는다
- 그상태에서 CreateView의 기본 form_valid()함수에 현재의 form을 인자로 보내 처리한다
- 만약 방문자가 로그인 하지 않은 상태라면 redirect()함수를 사용해 /blog/경로로 돌려보낸다

## 스태프만 포스트를 작성할 수 있게 만들기

views.py에서 UserPassesTestMixin을 인자로 추가후, test_func()함수를 추가해 이 페이지에 접근 가능한 사용자를 superuser또는 staff로 제한 한다. form_valid()에서도 로그인 한 사용자가 superuser이거나 staff인 경우에만 동작하도록 수정

```python
from django.contrib.auth.mixins import LoginRequiredMixin

Class PostCreate(LoginRequiredMixin,CreateView):
    model=Post
    fields = ['title', 'hook_text','content','head_image','file_upload','category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')
```

## 새 포스트 작성 버튼 만들기

로그인이 되어 있는 경우에 사용자가 최고 관리자 이거나 스태프일 때만 이 버튼이 보이도록 설정한다.

```html
{% if user.is_authenticated %} {% if user.is_superuser or user.is_staff %}
<a
  class="btn btn-info btn-sm float-right"
  href="/blog/create_post/"
  role="button"
  ><i class="fas fa-pen"></i>&nbsp;&nbsp;New Post</a
>
{% endif %} {% enif %}
```

## 포스트 작성자만 수정할 수 있게 구현하기

포스트를 수정하는 페이지는 작성자 본인만 접근할 수 있어야 한다. 방문자가 포스트의 작성자와 동일한지 확인하고 아닌 경우에는 권한이 없다고 오류 메시지를 나타내야 한다
이를 구현하기 위해 CBV에서 제공하는 dispatch() 메서드를 활용

- dispatch() 메서드는 방문자가 웹사이트 서버에 GET방식으로 요쳥했는지 POST 방식으로 요청했는지 판단하는 기능을 한다. CreateView나 현재 사용하고 있는 UpdateView의 경우 방문자가 서버에 GET방식으로 들어오면 포스트를 작성 할 수있는 폼 페이지를 보내준다. 반면 같은 경로로 폼에 내용을 담아 POST방식으로 들어오는 경우에는 폼이 유효한지 확인하고, 문제가 없다면 데이터 베이스에 내용을 저장하도록 되어있다.

만약 권한이 없는 사용자가 PostUpdate를 사용하려고 한다면 서버와 통신하는 방식이 GET방식이든 POST방식이든 상관없이 접근할 수 없게 해야한다.
따라서 dispatch()가 실행되는 순간 방문자가 포스트의 작성자가 맞는지 확인하도록 다음과 같이 수정한다

view.py

```python
from django.core.exceptions import PermissionDenied

class PostUpdate(LoginRequiredMixin, UpdateView):
    def dispatch(self, request,*args,**kwargs):
        if request.user.is_authenticated and request.user. == self.get_object().author:
            return super(PostUpdate, self).dispatch(request,*args,**kwargs)
        else:
            raise PermissionDenied
```

방문자(request.user)는 로그인한 상태여야 한다. self.get_object().author에서 self.get_object()는 UpdateView의 메서드로 Post.objects.get(pk=pk)과 동일한 역할을 한다. 이렇게 가져온 Post인스턴스의 author필드가 방문자와 동일한 경우에만 dispatch() 메서드가 원래 역할을 해야한다. 만약 이조건을 만족시키지 못한다면 권한이 없음을 나타내기 위해 raise PermissionDenied를 실행한다.
장고는 이런 경우에 활용 할 수 있는 PermissionDenied을 미리 만들어서 제공한다.

### ※CreateView, UpdateView는 모델명 뒤에 \_form.html이 붙은 템플릿 파일을 사용하도록 기본으로 설정되어있다. 그래서 PostUpdate에서도 PostCreate를 작성할때 만들어 둔 Post_form.html을 자동으로 찾아서 사용한것이다.

### ※CBV로 뷰를 만들때 template_name을 지정해 원하는 html파일을 템플릿 파일로 설정할 수 있다

<Edit Post> 버튼을 추가하는 과정을 포스트 목록 페이지에서 <New Post>버튼을 만든 과정과 거의 똑같다. if 문을 활용해 웹사이트 방문자가 로그인되어 있는 상태이고, 해당 포스트의 작성자일 경우에만 버튼이 보이도록 한다

```html
{% if user.is_authenticated and user == post.author %}
<a
  class="btn btn-info btn-sm float-right"
  href="/blog/update_post/{{post.pk}}/"
  role="button"
  ><i class="fas fa-pen"></i> Edit Post</a
>
{% endif %}
```
