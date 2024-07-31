

from django.shortcuts import render,redirect,HttpResponseRedirect
from SellPurchase.models.product import Product
from SellPurchase.models.category import Category
from SellPurchase.models.student import Student
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    return_url=None
    def get(self,request):
        Login.return_url=request.GET.get('return_url')
        return render(request,'student_login.html')

    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        student=Student.get_student_by_email(email)
        error_message = None
        if student:
            flag = check_password(password,student.password)
            if flag:
                request.session['student']=student.id
                
                if Login.return_url:
                   return HttpResponseRedirect(Login.return_url)
                else:
                   Login.return_url=None
                   return redirect('index')
            else:
                error_message = 'Email or Password Invalid ...!!'
                
        else:
            error_message = 'Email or Password Invalid ...!!'
        return render(request,'student_login.html',{'error':error_message})


def logout(request):
    request.session.clear()
    return redirect('index')





 