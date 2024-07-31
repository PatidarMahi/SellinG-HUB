from unicodedata import category
from django.db import models

from SellPurchase.models.student import Student
from .category import Category

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200,default='',null=True,blank=True)
    image=models.ImageField(upload_to='uploads/products/',null=True,blank=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products();


    @staticmethod
    def get_product_by_id(product):
            return Product.objects.get(id=product)
   
    
    @staticmethod
    def get_products_by_student(student):
        return Product.objects.filter(student=student)


    @staticmethod
    def delete_product_by_id(product_id):
        Product.objects.filter(id=product_id).delete()

            
