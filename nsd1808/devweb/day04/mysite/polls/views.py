from django.shortcuts import render, redirect, HttpResponse
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

def vote(request, question_id):
    choice_id = request.POST.get('choice_id')
    question = Question.objects.get(id=question_id)
    choice = question.choice_set.get(id=choice_id)
    choice.votes += 1
    choice.save()
    return redirect('result', question_id=question_id)
