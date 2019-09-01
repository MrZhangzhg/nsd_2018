from django.shortcuts import render, redirect
from .models import Question

def index(request):
    # 函数至少有一个参数，用户的请求将会自动发给它
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    # 返回的字典，key将成为模板的变量，val是值
    question = Question.objects.get(id=question_id)
    return render(request, 'detail.html', {'question': question})

def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    choice_id = request.POST.get('choice_id')
    # 通过问题取出相应的选项实例
    choice = question.choice_set.get(id=choice_id)
    choice.votes += 1
    choice.save()

    return redirect('result', question_id)
