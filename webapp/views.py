from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.template.loader import render_to_string

from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# Create your views here.
# def BASE(request):
#     return render(request,'base.html')
BASE =lambda request:render(request,'base.html')


def Home(request):
    sliders=slider.objects.all().order_by("-id")[0:3]
    banners=Banner_area.objects.all().order_by("-id")[0:3]
    main_category = Main_Category.objects.all().order_by("-id")
    product = Product.objects.filter(section__name="Top Deals Of The Day")

    context={
        'sliders':sliders,
        'banners':banners,
        'main_category':main_category,
        'product':product,
    }
    return render(request,'main/home.html',context)


def Product_Details(request,slug):
    product = Product.objects.filter(slug=slug)
    if product.exists():
        product = Product.objects.get(slug=slug)
    else:
        return redirect('404')

    context = {
        'product' : product
    }
    return render(request,'product/product_detail.html',context)


def Error404(request):
    return render(request,'errors/404.html')

def My_Account(request):
    return render(request,'account/my_account.html')

def REGISTER(request):
    # get username & password
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # username name exist or not
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username is already exists")
            return redirect('login')

        # email name exist or not
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email id is already exists")
            return redirect('login')

        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('login')

def LOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Email & Password are Invalid')
            return redirect('login')

@login_required(login_url='/accounts/login/')
def PROFILE(request):
    return render(request,'profile/profile.html')

@login_required(login_url='/accounts/login/')
def PROFILE_UPDATE(request):
    if request.method =='POST':
        username =request.POST.get('username')
        first_name =request.POST.get('first_name')
        last_name =request.POST.get('email')
        email =request.POST.get('username')
        password =request.POST.get('password')
        user_id =request.user.id

        user =User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password !=None and password !="":
            user.set_password(password)
            user.save()
            messages.success(request,"Profile are successfully updated")
            return redirect('profile')

def ABOUT(req):
    return render(req,'main/about.html')


def CONTACT(req):
    return render(req,'main/contact.html')


def PRODUCT(request):
    category=Category.objects.all()
    product=Product.objects.all()
    context2={
        'category': category,
        'product': product,
              }

    return render(request,'product/product.html',context2)


def filter_data(request):
    categories = request.GET.getlist('Category[]')
    brands = request.GET.getlist('brand[]')

    allProducts = Product.objects.all().order_by('-id').distinct()
    if len(categories) > 0:
        allProducts = allProducts.filter(Categories__id__in=categories).distinct()

    if len(brands) > 0:
        allProducts = allProducts.filter(Brand__id__in=brands).distinct()

    t = render_to_string('ajax/product.html', {'product': allProducts})

    return JsonResponse({'data': t})










