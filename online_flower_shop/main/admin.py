from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','Tittle','SubCat','Price')
    search_fields = ('id','Tittle','SubCat','Price')


admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','Order_User','Order_Prod','Quantity','Status')
    search_fields = ('id','Order_User','Order_Prod','Quantity','Status')


admin.site.register(Order, OrderAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','Tittle')
    search_fields = ('id','Tittle')


admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','Tittle','Cat')
    search_fields = ('id','Tittle','Cat')


admin.site.register(SubCategory, SubCategoryAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','Tittle','Order_User','Order_Prod','Date_Of_Change','Rating')
    search_fields = ('id','Tittle','Order_User','Order_Prod','Date_Of_Change','Rating')


admin.site.register(Comment, CommentAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','Prof_User','Patronymic')
    search_fields = ('id','Prof_User','Patronymic')


admin.site.register(Profile, ProfileAdmin)