from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def calculator(request):
    # return HttpResponse('계산기 기능 구현 시작입니다.')

    # 1. 데이터 확인
    num1= request.GET.get('num1')
    num2= request.GET.get('num2')
    operators = request.GET.get('operators')

    # 2. 계산
    if operators == '+':
            result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0

    #3. 응답
    return render(request, 'calculator.html',{'result':result})

def lotto_index(request):
    return render(request, 'lotto_index.html')

def lotto_result(request):
    lotto_number=list()
    game=request.GET.get('game',1)
    pull_number=[index for index in range(1,46)]

    for _ in range(int(game)):
        lotto_number.append(random.sample(pull_number,6))#sample 함수는 값을 뽑아낼때 중복값도 없애줌

    lotto_number.sort()

    return render(request, 'lotto_result.html',{'lotto_number':lotto_number,'game':game})