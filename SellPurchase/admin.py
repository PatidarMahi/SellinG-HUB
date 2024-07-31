from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.student import Student


# Register your models here.

admin.site.register(Product)
admin.site.register(Student)
admin.site.register(Category)

 

