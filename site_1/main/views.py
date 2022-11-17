from django.shortcuts import render
from django.http import HttpResponse


def general(request):
    return render(request, 'main/general.html')


def about(request):
    return render(request, 'main/about.html')


def labs(request):
    return render(request, 'main/mygithub.html')




