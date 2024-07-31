import http
from unicodedata import category
from django.shortcuts import render,redirect
from django.http import HttpResponse
from SellPurchase.models.product import Product
from SellPurchase.models.category import Category
from SellPurchase.models.student import Student
from django.views import View

 
class Products(View):
    def post(self,request):
       product=request.POST.get('product')
       remove =request.POST.get('remove')

       cart=request.session.get('cart')
       if cart:
         quantity=cart.get(product)
         if quantity:
            if remove:
                if quantity<=1:
                    cart.pop(product)
                else:
                    cart[product]=quantity-1
            else:
                cart[product]=quantity+1
         else:
            cart[product]=1
       else:
            cart = {}
            cart[product]=1

       request.session['cart']=cart
       print(request.session['cart'])
       return redirect('product')
       


    def get(self,request):
       cart = request.session.get('cart')
       if not cart:
          request.session['cart']={}
       products=None
       categories=Category.get_all_categories();
       catagoryID=request.GET.get('category')
       if catagoryID:
           products=Product.get_all_products_by_category_id(catagoryID)
       else:
           products=Product.get_all_products();
       data={}
       data['products']=products
       data['categories']=categories
       return render(request,'product.html',data)


 
    





 

 
