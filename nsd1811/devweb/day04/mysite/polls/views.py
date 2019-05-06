from django.shortcuts import render
from .models import Question

# 用户发送请求时，将会把请求作为第一个参数传递
def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

def detail(request, question_id):
    return render(request, 'detail.html', {'question_id': question_id})

def result(request, question_id):
    return render(request, 'result.html', {'question_id': question_id})
