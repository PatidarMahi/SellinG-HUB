import http
from unicodedata import category
from django.shortcuts import render,redirect
from django.http import HttpResponse
from SellPurchase.models.student import Student
from django.contrib.auth.hashers import make_password
from django.views import View
import re


 

class Signup(View):
    def get(self,request):
       return render(request,'signup.html')
    
    
    def post(self,request):
       postData=request.POST
       name=postData.get('name')
       branch=postData.get('branch')
       hostel_name=postData.get('hostel_name')
       room_no=postData.get('room_no')
       phone_no=postData.get('phone_no')
       email=postData.get('email')
       password=postData.get('password')
       password2=postData.get('pswd')
       if request.FILES:
            image=request.FILES['image']

       
       student=Student(name=name,branch=branch,hostel_name=hostel_name,
       room_no=room_no,phone_no=phone_no,email=email,password=password,image=image)
       
       error_message=self.validateStudent(student)

       if(password != password2):
          error_message="Password does not matches!!"

       value={
             'name':name,
             'branch':branch,
             'hostel_name':hostel_name,
             'room_no':room_no,
             'phone_no':phone_no,
             'email':email, 
             'image':image    
          }
 
      
       if not error_message:
           student.password=make_password(student.password)
           student.register()
           return redirect('student_login')
       else:
           data={
                  'error':error_message,
                  'values':value
              }
           return render(request,'signup.html',data)

            

    def validateStudent(self,student):
        error_message=None
        if(not student.name):
           error_message="Name Required !!"
        elif len(student.name) < 4:
           error_message="Name is Too Short !!"
        elif(not student.branch):
           error_message="Branch/Course Name Required !!"
        elif(not student.hostel_name):
           error_message="Hostel Name Required !!"
        elif(not student.phone_no):
           error_message="Phone No. Required !!"
        elif(len(student.phone_no) != 10):
           error_message="Invalid Phone No !!"
        elif(not student.email):
           error_message="Email Required !!"
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', student.email):
            error_message = "Invalid email format! Please enter a valid email address." 
        elif(not student.password):
           error_message="Password Required !!"
        elif(len(student.password)<6):
           error_message="Password Must be 6 char Long"
        elif(student.isExists()):
           error_message="Email Already Registered ...!!"
        
        return error_message



 