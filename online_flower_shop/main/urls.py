from django.urls import path
from .import views
from .views import *



urlpatterns = [
    path('',STView.as_view(), name = 'start'),
    path('Main/',MainView.as_view(), name = 'main'),
    path('Main/Prod',ProdView.as_view(), name = 'prod'),
    path('Main/Prod/Confirmation',ConfView.as_view(), name = 'conf'),
    path('Auth/',AuthView.as_view(), name = 'auth'),
    path('cat/<int:cat_id>/', show_cat, name='show_cat'),
    path('sub_cat/<int:sub_cat_id>/', show_sub_cat, name='show_sub_cat'),
    path('Prof/',ProfView.as_view(), name = 'prof'),
    path('Deliv/',DelivView.as_view(), name = 'deliv'),
    path('About/',AboutView.as_view(), name = 'about'),
    path('Logout/',Logout.as_view(),name='logout'),
    path('Reg/', RegView.as_view(), name='reg'),
    path('Korz/', KorzView.as_view(), name='korz'),
]
