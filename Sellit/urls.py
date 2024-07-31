from django.contrib import admin
from django.urls import path
from SellPurchase.views.old import *
from django.conf import settings
from django.conf.urls.static import static # type: ignore
from SellPurchase.views.contact import contact_view




from SellPurchase.views import signup,student_login,index,addproduct,product,seller,myproducts,views,message



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index.index, name='index'),

    
    path('contact/', contact_view, name='contact'),
   
    path('seller/<int:seller_id>/payment/', views.payment_gateway, name='payment_gateway'),
    path('seller/<int:seller_id>/message/', views.message_seller, name='message_seller'),
   path('message',message.Message.as_view(),name='message'),



   
    path('products', product.Products.as_view(), name='product'),
    
    path('addproduct', addproduct.Addproduct.as_view(), name='addproduct'),
    path('student_login',student_login.Login.as_view(), name='student_login'),
    path('logout/',student_login.logout,name='logout'),
    path('signup',signup.Signup.as_view(),name='signup'),

    path('seller',seller.Seller.as_view(),name='seller'),
    path('myproducts', myproducts.Myproducts.as_view() ,name='myproducts'),


    path('admin_login', admin_login, name='admin_login'),
    path('dashboard', dashboard, name='dashboard'),
    path('addcategory', addcategory, name='addcategory'),
    path('managecategory', managecategory, name='managecategory'),
    path('editcategory<int:pid>', editcategory, name='editcategory'),
    path('deletecategory<int:pid>', deletecategory, name='deletecategory'),



    path('regstudents', regstudents, name='regstudents'),
    path('deletestudent<int:pid>', deletestudent, name='deletestudent'),
    path('listedproducts', listedproducts, name='listedproducts'),
    path('deleteproduct<int:pid>', deleteproduct, name='deleteproduct'),


   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
