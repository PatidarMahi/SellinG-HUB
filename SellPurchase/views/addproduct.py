import http
from unicodedata import category
from django.shortcuts import render,redirect
from django.http import HttpResponse
from SellPurchase.models.product import Product
from SellPurchase.models.student import Student
from SellPurchase.models.category import Category
from django.views import View
from SellPurchase.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


 
class Addproduct(View):

    @method_decorator(auth_middleware)    #@auth_decorator -> decorator -> direct apply functions.(function v/s method) 
    def get(self,request):
       categories = Category.get_all_categories()
       return render(request , 'addproduct.html'  , {'categories' : categories} )

 
    def post(self,request):
        name=request.POST.get('name')
        price=request.POST.get('price')
        category_name=request.POST.get('category')
        
        category= Category.get_category_id_by_name(category_name)
        
        description=request.POST.get('description')

        if request.FILES:
            image=request.FILES['image']
        
        student = request.session.get('student')
        
        print(Category(id=category))

        product=Product(name=name,price=price,category=Category(id=category),
                        description=description,image=image,
                        student=Student(id=student))

        product.save()
        return redirect('product')

    
    

 