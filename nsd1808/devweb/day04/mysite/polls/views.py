from django.shortcuts import render, HttpResponse
from .models import Question

def index(request):
    # 形参request名称随便定义，但是必须提供，用户的请求将作为实参传入
    # return HttpResponse('<h1>投票首页</h1>')
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'detail.html', {'question': question})

def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})
