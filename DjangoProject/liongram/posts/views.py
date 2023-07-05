from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Post

def index(request):
    return render(request,'index.html')

def post_list_view(request):
    return render(request,'posts/post_list.html')

def post_detail_view(request,id):
    return render(request,'posts/post_detail.html')

def post_create_view(request):
    return render(request,'posts/post_form.html')

def post_update_view(request,id):
    return render(request,'posts/post_form.html')

def post_delete_view(request,id):
    return render(request,'posts/post_comform_delete.html')



# Create your views here.
def url_vew(request):
    data = {'code':'001','msg':'ok'}
    return HttpResponse(data)

def url_parameter_vew(request,username):
    print(username)


    return HttpResponse(username)

def function_view(request):
    print(f'request.GET: {request.GET}')

    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request,'view.html')

class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'