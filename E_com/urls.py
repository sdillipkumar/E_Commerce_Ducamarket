"""
URL configuration for E_com project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from webapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    # error_page
    path('404/', views.Error404, name='404'),
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('', views.Home, name='home'),
    path('about/', views.ABOUT, name='about'),
    path('contact/', views.CONTACT, name='contact'),
    path('product/', views.PRODUCT, name='product'),
    path('product/filter-data',views.filter_data,name="filter-data"),
    path('product/<slug:slug>', views.Product_Details, name='product_detail'),
    path('account/my-account', views.My_Account, name='my-account'),
    path('account/register', views.REGISTER, name='handleregister'),
    path('account/login', views.LOGIN, name='handlelogin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile',views.PROFILE,name='profile'),
    path('accounts/profile/update',views.PROFILE_UPDATE,name='profile_update'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
