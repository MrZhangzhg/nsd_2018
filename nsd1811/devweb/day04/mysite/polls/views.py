from django.shortcuts import render, redirect
from .models import Question

# 用户发送请求时，将会把请求作为第一个参数传递
def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'detail.html', {'question': question})

def vote(request, question_id):
    question = Question.objects.get(id=question_id)  # 取出问题实例
    choice_id = request.POST.get('choice_id')  # 在表单提交的数据中取出选项id
    choice = question.choice_set.get(id=choice_id)  # 获取选项实例
    choice.votes += 1  # 选票值加1
    choice.save()  # 保存修改

    # 重定向，相当于是打开一个新窗口输入网址，不会再提交表单数据
    # 如果采用render，将会把detail表单提交的数据继承向result.html提交
    return redirect('result', question_id=question.id)

def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})
