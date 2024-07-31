import random
from unicodedata import category
from SellPurchase.models.student import Student
from SellPurchase.models.category import Category
from SellPurchase.models.product import  Product
from django.views import  View
from django.contrib.auth import authenticate, logout, login
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')


 
def student_login(request):
    error = ""
    if request.method == 'POST':
        e = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=e, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'student_login.html', locals())

 
def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin/dashboard.html', locals())

def addcategory(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    error = None
    if request.method == "POST":
        categoryname = request.POST['categoryname']

        try:
            Category.objects.create(name=categoryname)
            # error = "no"
        except:
            error = "Category is Not Valid"
        return redirect('managecategory')

    return render(request, 'admin/addcategory.html', locals())


def managecategory(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.all()
    return render(request, 'admin/managecategory.html', locals())


def editcategory(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    
    category = Category.objects.get(id=pid)
    if request.method == "POST":
        categoryname = request.POST['categoryname']

        category.name = categoryname
        try:
            category.save()
            error = "no"
        except:
            error = "yes"
        return redirect('managecategory')   
    return render(request, 'admin/editcategory.html', locals())


def deletecategory(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.get(id=pid)
    category.delete()
    return redirect('managecategory')


 
def regstudents(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = Student.objects.all()
    return render(request, 'admin/registerstudent.html', locals())


def deletestudent(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = Student.objects.get(id=pid)
    student.delete()
    return redirect('regstudents')


def listedproducts(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    product = Product.objects.all()
    return render(request, 'admin/listedproducts.html', locals())



def deleteproduct(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    product = Product.objects.get(id=pid)
    product.delete()
    return redirect('listedproducts')
     
 
def Logout(request):
    logout(request)
    return redirect('index')

 