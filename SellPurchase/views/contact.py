# contact.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django import forms
# Redirect to home page with success me
import tkinter as tk
from tkinter import messagebox

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipient_email = 'patidarmahi7047@gmail.com'

            # Send email
            subject = 'New Contact Form Submission'
            message = render_to_string('email_template.html', {'name': name, 'email': email, 'message': message})
            send_mail(subject, message, 'patidarmahi7047@gmail.com',[recipient_email])
            
            

               

            return HttpResponseRedirect('/')  
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
