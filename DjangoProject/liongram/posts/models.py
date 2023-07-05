from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model() # 나중에 User모델을 새로 커스텀할것이다 그때도 코드를 변경하지 않고 그대로 사용할수있는 방법이라고 보면 됨

# Create your models here.

# 일 대 다 관계에서는 다 쪽에 관계에서 일 쪽의 모델을 참고해야한다. 그리고 to=, on_delete= 이 필수로 들어가주어야한다.

class Post(models.Model):
    image = models.ImageField(verbose_name='이미지',null=True,blank=True)
    content=models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일',auto_now_add=True)
    view_count = models.IntegerField(verbose_name='조회수',default=0)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE,null=True,blank=True)

class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일',auto_now_add=True)
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE,null=True,blank=True)# on_delete=models.CASCADE는 Post가 삭제되었을대 Comment도 자동으로 삭제해준다는 의미
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE)