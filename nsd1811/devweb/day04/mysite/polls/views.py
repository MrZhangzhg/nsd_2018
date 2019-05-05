from django.shortcuts import render

# 用户发送请求时，将会把请求作为第一个参数传递
def index(request):
    return render(request, 'index.html')

def detail(request, question_id):
    return render(request, 'detail.html', {'question_id': question_id})
