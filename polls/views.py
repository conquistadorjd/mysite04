from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def second(request):
    return render(request, 'polls/second.html')

def third(request):
    return render(request, 'polls/third.html')

def fourth(request):
    return render(request, 'polls/fourth.html')

def fifth(request):
    return render(request, 'polls/fifth.html')

def sixth(request):
    return render(request, 'polls/sixth.html')