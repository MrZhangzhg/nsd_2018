from django.shortcuts import render

# Create your views here.

def index(request):
    # 函数至少有一个参数，用户的请求将会自动发给它
    return render(request, 'index.html')

def detail(request, question_id):
    # 返回的字典，key将成为模板的变量，val是值
    return render(request, 'detail.html', {'question_id': question_id})

def result(request, question_id):
    return render(request, 'result.html', {'question_id': question_id})
