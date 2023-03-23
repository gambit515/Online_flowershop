from django.urls import path
from . import views

urlpatterns = [
    path('',views.syte),
    path('profile', views.profile),
    path('test', views.test),
]
