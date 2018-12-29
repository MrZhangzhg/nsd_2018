from django.shortcuts import render

def index(request):    # 用户访问web发来的请求将作为参数request的值
    return render(request, 'index.html')

def detail(request, question_id):
    return render(request, 'detail.html', {'question_id': question_id})

def result(request, question_id):
    return render(request, 'result.html', {'question_id': question_id})
