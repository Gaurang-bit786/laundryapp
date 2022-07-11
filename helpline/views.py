from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import OrdersHelp,PaymentHelp,PackageHelp

def order_help(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            user = User.objects.get(id=request.user.id)
            data = request.POST.get('order')
            image = request.FILES.get('image')
            order = OrdersHelp(user=user,order_help=data,image=image)
            order.save()
            
            return redirect('order_help')
        else:
            return render(request,'orders_help.html')
    else:
        return redirect("login")


def pay_help(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            print(request.POST)
            user = User.objects.get(id=request.user.id)
            data = request.POST.get('order')
            image = request.FILES.get('image')
            order = PaymentHelp(user=user,payment_help=data,image=image)
            order.save()
            
            return redirect('pay_help')
        else:
            return render(request,'payment_help.html')
    else:
        return redirect("login")



def pack_help(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            user = User.objects.get(id=request.user.id)
            data = request.POST.get('order')
            image = request.FILES.get('image')
            order = PackageHelp(user=user,package_help=data,image=image)
            order.save()
            
            return redirect('pack_help')
        else:
            return render(request,'pack_help.html')
    else:
        return redirect("login")



