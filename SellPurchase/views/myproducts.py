from email.mime import image
from itertools import product
from django.shortcuts import render , redirect
from SellPurchase.models.student import Student
from SellPurchase.models.category import Category
from django.views import  View
from SellPurchase.models.product import  Product
from django.core.files.storage import FileSystemStorage
 
 

class Myproducts(View):
    def get(self ,request):
        student=request.session.get('student')
        products = Product.get_products_by_student(student)
        return render(request , 'myproducts.html' , {'products' : products} )


    def post(self ,request):
          product_id=request.POST.get('product')
          Product.delete_product_by_id(product_id)
          student=request.session.get('student')
          products = Product.get_products_by_student(student)
          return render(request , 'myproducts.html' , {'products' : products} )

           
         
   

     