from django.shortcuts import render, redirect
from .models import Question

def index(request):    # 用户访问web发来的请求将作为参数request的值
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'detail.html', {'question': question})

def result(request, question_id):
    return render(request, 'result.html', {'question_id': question_id})

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    choice_id = request.POST.get('choice_id')
    choice = question.choice_set.get(id=choice_id)
    choice.votes += 1
    choice.save()
    return redirect('result', question_id=question_id)

