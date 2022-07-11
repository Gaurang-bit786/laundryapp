from django.http import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserDetail
from orders.models import *
from premium.models import *
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            authen = authenticate(username=username,password=password)
            if authen is not None:
                login(request,authen)
                return redirect("home")
            else:
                return render(request,'login.html')
        else:
            return render(request,'login.html')
    else:
        return redirect("home")


def home(request):
    if request.user.is_authenticated:
        cloth_cat = ClothCategory.objects.all()
        p_cloth_cat = PremiumClothCategory.objects.all()
        user = User.objects.get(id = request.user.id)
        pre = PremiumClothService.objects.get(name=user)
        price = PremiumServicePrice.objects.all()
        return render(request,'home.html',{"cloth_cat":cloth_cat,"p_cloth_cat":p_cloth_cat,'service':pre,'price':price})
    else:
        return redirect("login")


def clothcat(request,id):
    if request.user.is_authenticated:
        cloth_cat = ClothCategory.objects.get(id=id)
        cloth = ClothName.objects.filter(cloth_category_name=cloth_cat).all()
        return render(request,'clothcat.html',{"cloth":cloth})
    else:
        return redirect("login")


def user_detail_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = User.objects.get(pk=request.POST.get("id"))
            print(user.first_name)
            user.first_name = request.POST.get("firstname")
            user.last_name = request.POST.get("lastname")
            user.email = request.POST.get("email")
            user.save()
            user_detail = UserDetail.objects.get(username=user)
            user_detail.address = request.POST.get("address")
            user_detail.phone_number = request.POST.get("phone")
            user_detail.mobile_number = request.POST.get("mobile")
            user_detail.save()
            return render(request,'userdetails.html',{"user_detail":user_detail})
        else:
            print(request.user.username)

            user = User.objects.get(username=request.user.username)
            user_detail = UserDetail.objects.get(username=user)
            return render(request,'userdetails.html',{"user_detail":user_detail})

    else:
        return redirect("login")



def user_view(request):
    if request.user.is_authenticated:
        return render(request,'user.html')
    else:
        return redirect("login")


def register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            email = request.POST.get("email")
            password = request.POST.get("password")
            address = request.POST.get("address")
            register_user = User.objects.create_user(username=email,first_name=firstname,last_name=lastname,email=email,password=password)
            if register_user is not None:
                register_user.save()
                ud = UserDetail(username=register_user,address=address)
                ud.save()
                pc = PremiumClothService(name=register_user)
                pc.save()
                ad = AccountDetail(user=register_user)
                ad.save()
                return redirect("login")
            else:
                return render(request,'register.html')
        else:
            return render(request,'register.html')
    else:
        return redirect("home")



def logout_user(request):
    logout(request)
    return redirect("login")


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"Password Change Successfuly")
                return redirect('user')
            else:
                fm = PasswordChangeForm(user=request.user)
            return render(request,'change_password.html',{'form':fm})
        else:
            fm = PasswordChangeForm(user=request.user)
            return render(request,'change_password.html',{'form':fm})
    else:
        return render('login')