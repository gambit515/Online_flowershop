from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from .models import Comment,SubCategory,Category,Product, Profile, Order
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import ProfileForm, UserForm, RegForm, PostForm

from .forms import AuthUserForm


# Create your views here.

class STView(TemplateView):
    template_name = 'main/ST.html'


class MainView(ListView):
    model = Product
    template_name = 'main/Main.html'


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