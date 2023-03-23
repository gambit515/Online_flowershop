from django.shortcuts import render
from .models import Flowers


def syte(request):
    Goods_from_BD = Flowers.objects.all()
    return render(request, 'mainshit/syte.html',{'Goods_from_BD':Goods_from_BD})


def profile(request):
    return render(request,'mainshit/profile.html')

def test(request):
    Goods_from_BD = Flowers.objects.all()
    return render(request, 'mainshit/test.html',{'Goods_from_BD':Goods_from_BD})