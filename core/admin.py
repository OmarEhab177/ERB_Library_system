from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Category, Book
# Register your models here.




admin.site.register(Book)
admin.site.register(Category)