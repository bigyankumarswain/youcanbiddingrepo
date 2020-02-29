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
from adminApp import views

urlpatterns = [
    path('admin_login/',views.adminlogin,name="admin_login"),
    path('admin_logout/',views.adminlogout,name="admin_logout"),
    path('pending_reqst/',views.pending_reqst,name="pending_reqst"),
    path('approved_list/',views.approved_list,name="approved_list"),
    path('decline_list/',views.decline_list,name="decline_list"),
    path('approve<int:uid>/',views.approvePendingUser,name="approve"),
    path('approve_decline<int:uid>/',views.approveDeclineUser,name="approve_decline"),
    path('decline<int:uid>/',views.declineUser,name="decline"),
    path('admmin_welcom/',views.admmin_welcom,name="admmin_welcom"),
    path('delete_decline<int:uid>/',views.delete_decline,name="delete_decline"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)