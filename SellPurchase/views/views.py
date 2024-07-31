# views.py
from mailbox import Message
from pyexpat.errors import messages
from django.shortcuts import render, redirect

from SellPurchase.models import student


def payment_gateway(request, seller_id):
    # Logic for payment gateway functionality
    return render(request, 'payment_gateway.html', {'seller_id': seller_id})
def message_seller(request, seller_id):
    # Logic for payment gateway functionality
    return render(request, 'message_seller.html', {'seller_id': seller_id})
def send_message(request, seller_id):
    if request.method == 'POST':
        # Extract message data from the form
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        
        # Get the seller object using the seller_id
        seller = student.objects.get(id=seller_id)
        
        # Create and save the message
        message = Message(subject=subject, body=body, sender=request.user, recipient=seller)
        message.save()
        
        # Optionally, you can add a success message
        messages.success(request, 'Your message has been sent successfully.')
        
        # Redirect the user to a confirmation page or another appropriate URL
        return redirect('index')
    
    # If the request method is not POST, render the message form
    return render(request, 'message_seller.html')