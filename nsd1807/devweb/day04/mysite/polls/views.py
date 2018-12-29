from django.shortcuts import render

def index(request):    # 用户访问web发来的请求将作为参数request的值
    return render(request, 'index.html')

def detail(request):
    return render(request, 'detail.html')
