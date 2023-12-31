"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demos.views import calculator,lotto_index,lotto_result
urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/',calculator), # 이 url로 들어오면 이 함수를 실행시켜라는 코드
    path('lotto/',lotto_index,name='lotto_index'),
    path('lotto/result/',lotto_result,name='lotto_result'),
]

