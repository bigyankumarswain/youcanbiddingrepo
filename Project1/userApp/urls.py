"""Project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path
from Project1 import settings
from userApp import views

urlpatterns = [
    path('register/',views.user_register,name="register"),
    path('userlogin/',views.userLogin,name="login"),
    path('user_welcome/',views.user_welcome,name="user_welcome"),
    path('userlogout/',views.userLogout,name="logout"),
    path('selling/',views.selling,name="selling"),
    path('buying/',views.buying,name="buying"),
    path('add_product/',views.add_product,name="add_product"),
    path('view_all_product/',views.view_all_product,name="viewallproduct"),
    path('product_not_bid/',views.product_not_bid,name="product_not_bid"),
    path('product_bid/',views.product_bid,name="product_bid"),
    path('product_sold/',views.product_sold,name="product_sold"),
    path('add_to_bid<int:pid>/',views.add_to_bid,name="add_to_bid"),
    path('bidding_product/',views.bidding_product,name="bidding_product"),
    path('bidding_info<int:pid>/',views.bidding_info,name="bid_info"),
    path('bid_details/',views.bid_Details,name="bid_details"),
    path('change_pswd/',views.change_pswd,name="change_pswd"),
    path('bid_prices<int:pid>/',views.bid_prices,name="bid_prices"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
