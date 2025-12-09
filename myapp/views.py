from django.shortcuts import render, HttpResponse
# user A
# user B

def test(request):
    return HttpResponse("Hello!")

def aWeb(request):
    print("hello world")
    return HttpResponse("Hello!, aweb.完成")
def bWeb(request):
    return HttpResponse("Hello!, bweb")
