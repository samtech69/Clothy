
from django.contrib import admin
from django.urls import path
from mainApp import views as mainApp  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainApp.homepage,name='home'),
    path('about/',mainApp.about,name='about'),
    path('login/',mainApp.LoginPage,name='login'),
    path('logout/',mainApp.logoutPage,name='logout'),
    path('signup/',mainApp.signup,name='signup'),
    path('profile/',mainApp.profile,name='profile'),
    path('checkout/',mainApp.checkoutpage,name='checkout'),
    path('re-payment/<int:id>',mainApp.repaymentPage,name='re-payment'),
    path('payment-success/',mainApp.paymentSuccessPage,name='payment-success'),
    path('confirmation/',mainApp.confirmPage,name='confirmation'),
    path('update-profile/',mainApp.updateprofile,name='update-profile'),
    path('product/<int:id>/',mainApp.product,name='product'),
    path('contact/',mainApp.contact,name='contact'),
    path('shop/<str:mc>/<str:sc>/<str:br>/',mainApp.shop,name='shop'),
    path('cart/',mainApp.cart,name='cart'),
    path('Add-to-cart/',mainApp.addtocart,name='Add-to-cart'),
    path('delete-cart/<str:id>/',mainApp.deletecart,name='delete-cart'),
    path('update-cart/<str:id>/<str:op>/',mainApp.updatecart,name='update-cart'),
    path('favourite/',mainApp.Favourite,name='favourite'),
    path('delete-wishlist/<int:id>/',mainApp.deletewishlist,name='delete-wishlist'),
    path('add-to-wishlist/<int:id>/',mainApp.addtowishlist,name="add-to-wishlist"),
    path('newslatter/subscribe/',mainApp.subscribe,name='subscribe'),
    path('search/',mainApp.searchPage,name='search'),
    path('forget-password1/',mainApp.forgetPassword1,name='forget-password1'),
    path('forget-password2/',mainApp.forgetPassword2,name='forget-password2'),
    path('forget-password3/',mainApp.forgetPassword3,name='forget-password3'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



 
 







