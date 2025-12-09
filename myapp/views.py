from django.shortcuts import render, HttpResponse
# user A

def test(request):
    return HttpResponse("Hello!")

def aWeb(request):
    print("hello world")
    return HttpResponse("Hello!, aweb.完成")
