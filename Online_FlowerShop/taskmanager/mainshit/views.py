from django.shortcuts import render
from django.http import HttpResponse


def syte(request):
    return render(request, 'mainshit/syte.html')


def profile(request):
    return render(request,'mainshit/profile.html')
