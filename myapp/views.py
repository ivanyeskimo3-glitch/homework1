from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

def test(request):
    return HttpResponse("Hello!")
