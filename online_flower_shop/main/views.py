from django.contrib.auth import authenticate, login
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from .models import Comment,SubCategory,Category,Product, Profile, Order
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import ProfileForm, UserForm, RegForm, PostForm, OtklForm

from .forms import AuthUserForm


# Create your views here.

class STView(TemplateView):
    template_name = 'main/ST.html'


class MainView(ListView):
    model = Product
    template_name = 'main/Main.html'
    success_url = reverse_lazy('main')

    def get(self, request):
        products = Product.objects.all()
        cat = Category.objects.all()
        subcat = SubCategory.objects.all()
        context = {
            'products': products,
            'cat': cat,
            'sub_cat': subcat,
            'cat_selected': 0,
            'sub_cat_selected': 0,
        }
        return render(request, 'main/Main.html', context)


class ProdView(CreateView):
    template_name = 'main/Prod.html'


class ConfView(TemplateView):
    template_name = 'main/Conf.html'


class AuthView(LoginView):
    model = User
    template_name = 'main/Auth.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('main')

    def get_success_url(self):
        return self.success_url


class ProfView(ListView):
    model = Profile
    template_name = 'main/Prof.html'


class DelivView(ListView):
    model = Order
    template_name = 'main/Deliv.html'

class KorzView(ListView):
    model = Order
    template_name = 'main/Korz.html'

    def get(self, request):
        orders = Order.objects.all()
        products = Product.objects.all()
        totalprice = list(Order.objects.filter(Order_User=request.user.id).aggregate(Sum('Order_Prod__Price')).values())[0]
        context = {
            'ord': orders,
            'prod': products,
            'tp': totalprice,
        }
        return render(request, 'main/Korz.html', context)

class AboutView(TemplateView):
    template_name = 'main/About.html'


class Logout(LogoutView):
    next_page = reverse_lazy('auth')

class RegView(CreateView): #Класс регистрации
    model = User
    form_class = PostForm
    template_name = 'main/Reg.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        self.object.groups.clear()
        #self.object.groups.add(form.cleaned_data['groups'])
        #self.object.groups.add(name='Пользователь')
        group = Group.objects.get(name='Пользователь')
        self.object.groups.add(group)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid


def show_cat(request,cat_id):
    #anketas = Product.objects.filter(Soft_cat_id=cat_id)
    products = Product.objects.filter(Cat_id=cat_id)
    cat = Category.objects.all()
    subcat = SubCategory.objects.all()
    context = {
        'products': products,
        'cat': cat,
        'sub_cat': subcat,
        'cat_selected': cat_id,
        'sub_cat_selected': 0,
    }

    return render(request, 'main/Main.html', context)


def show_sub_cat(request,sub_cat_id):
    #anketas = Product.objects.filter(Soft_cat_id=cat_id)
    products = Product.objects.filter(SubCat_id=sub_cat_id)
    cat = Category.objects.all()
    subcat = SubCategory.objects.all()
    context = {
        'products': products,
        'cat': cat,
        'sub_cat': subcat,
        'cat_selected': 0,
        'sub_cat_selected': sub_cat_id,
    }

    return render(request, 'main/Main.html', context)

def conf_prod(request,product_id):
    context = {
        'product_id': product_id
    }
    if request.method == 'POST':
        form = OtklForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Order_User = request.user
            instance.Order_Prod = Product.objects.get(id=product_id)
            instance.Quantity = 1;
            instance.Status = False;
            instance.save()
            return render(request, 'main/ST.html')
    else:
        form = OtklForm()

    return render(request,'main/Conf.html', {'form': form} )