from re import T
from django.shortcuts import render, redirect
from orders.models import *
from django.contrib.auth.models import User
from userauthentication.models import *
from premium.models import *
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from datetime import datetime
import time


# Create your views here.

def order(request):
    if request.user.is_authenticated:
        cloth = ClothCategory.objects.all()
        return render(request,'orders.html',{"cloth":cloth})
    else:
        return redirect("login")



def place_order(request,id):
    if request.user.is_authenticated:
        cloth = ClothCategory.objects.get(id=id)
        all_cloth = ClothName.objects.filter(cloth_category_name=cloth).all()
        print(all_cloth)
        return render(request,'place_orders.html',{"cloth":all_cloth,"cat":cloth})
    else:
        return redirect("login")


def confirm_order(request):
    if request.user.is_authenticated:

        data = [request.POST.get("ironing"),
                request.POST.get("hotwater"),
                request.POST.get("coldwater"),
                request.POST.get("washing"),
                request.POST.get("softern")
            ]
        cloth = request.POST.get("cloth")
        pick_up_time = request.POST.get("puck_up_time")
        delivery_time = request.POST.get("delivery_time")
        h1 = int(pick_up_time.split(":")[0])
        m1 = int(pick_up_time.split(":")[1])
        h2 = int(delivery_time.split(":")[0])
        m2 = int(delivery_time.split(":")[1])
        s1 = (h1*3600) + (m1*60)
        s2 = (h2*3600) + (m2*60)

        pick_up_date = request.POST.get("puck_up_date")
        delivery = request.POST.get("delivery")
        price = ClothName.objects.get(cloth_name=request.POST.get("cloth"))
        p = price.price



        print(pick_up_date)
        quantity = request.POST.get("qunatity")
        total_cost = int(quantity) * p
        if pick_up_date == delivery:
            if(s2-s1<=7200):
                total_cost += 15
            elif(s2-s1>7200  and  s2-s1<18000):
                total_cost += 10
            else:
                total_cost +=5

        newData = []
        for ele in data:
            if ele is not None:
                newData.append(ele)
        print(newData)

        return render(request,'confirm_order.html',{"data":newData,"price":p,"pick_up_time":pick_up_time,"delivery_time":delivery_time,"quantity":quantity,"total_cost":total_cost,"pick_up_date":pick_up_date,"cloth":cloth,"delivery":delivery})
    else:
        return redirect("login")

def save_order(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            cloth = request.POST.get("cloth")
            price = request.POST.get("price")
            quantity = request.POST.get("quantity")
            ironing = request.POST.get("Ironing")
            hot_water = request.POST.get("Hot Water")
            cold_water = request.POST.get("Cold Water")
            washing_liquid = request.POST.get("Washing Liquid")
            total_cost = request.POST.get("total_cost")
            softern = request.POST.get("Softern")
            pick_up_date = request.POST.get("pick_up_date")
            delivery = request.POST.get("delivery")
            pick_up_time = request.POST.get("pick_up_time")
            delivery_time = request.POST.get("delivery_time")
            user = User.objects.get(id = request.user.id)
            cloth_name = ClothName.objects.get(cloth_name=cloth)
            order_summary = request.POST.get("order_summary")
            cloth_image = request.FILES.get("cloth_image")
            print(delivery)
            iron=False
            if ironing is not None:
                iron = True

            hot_w = False
            if hot_water is not None:
                hot_w = True

            cold_w = False
            if cold_water is not None:
                cold_w = False

            wash_liq = False
            if washing_liquid is not None:
                wash_liq = True

            soft = False
            if softern is not None:
                soft = True
            print(cloth_image)
            order = OrdersSummary(user=user,cloth_name=cloth_name,cloth_image=cloth_image,price=total_cost,quantity=quantity,ironing=iron,hot_water=hot_w,cold_water=cold_w,washing_liquid=wash_liq,softern=soft,puckup_date=pick_up_date,pickup_time=datetime.strptime(pick_up_time,"%H:%M").time(),delivery_time=datetime.strptime(delivery_time,"%H:%M").time(),delivery=delivery,instruction=order_summary)
            order.save()
            return redirect("order")
    else:
        return redirect("login")



def order_details(request):
    if request.user.is_authenticated:
        user = User.objects.get(id = request.user.id)
        print(user)
        cloth_summary = OrdersSummary.objects.filter(user = user)
        premium_cloth_summary = PremiumOrdersSummary.objects.filter(user = user)
        print(cloth_summary)
        return render(request,"order_list.html",{"cloth":cloth_summary,'premium_cloth':premium_cloth_summary})
    else:
        return redirect("login")


def card_details(request,id):
    if request.user.is_authenticated:
        user = User.objects.get(id = request.user.id)
        account = AccountDetail.objects.filter(user=user)
        print(id)
        return render(request,"card_details.html",{"account":account,"id":id})
    else:
        return redirect("login")

def check_out(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            id = request.POST.get("id")
            order_id = request.POST.get("order_id")
            name = request.POST.get("name")
            card_number = request.POST.get("card_number")
            month = request.POST.get("month")
            year = request.POST.get("year")
            cvv = request.POST.get("cvv")
            user = User.objects.get(id = request.user.id)
            print(user)
            order = OrdersSummary.objects.get(id=order_id)
            print(order.price)
            if id is None:
                account = AccountDetail(user = user,name=name,card_number=card_number,card_month=month,card_year=year,cvv=cvv)
            else:
                account = AccountDetail.objects.get(id=id)
                account.user = user
                account.name = name
                account.card_number = card_number
                account.card_month = month
                account.card_year = year
                account.cvv = cvv
            account.save()
            details = UserDetail.objects.get(username=user)

            return render(request,"checkout.html",{"name":name,"details":details,"price":order.price,"order_id":order_id})
        else:
            return redirect("order_details")
    else:
        return redirect("login")


def payment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            order_id = request.POST.get("order")
            otp  = request.POST.get("otp")
            if order_id:
                order = OrdersSummary.objects.get(id=order_id)
                order.paid = True
                order.save()
                user = User.objects.get(id = request.user.id)
                detail = UserDetail.objects.get(username=user)

                html_content = ("   <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com'/'bootstrap'/'4.3.1'/'css'/'bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'>"+
                                "<div class='container'>"+
                    "<div class='row text-center'>"+
                        "<div class='col'>"+
                            "<h5>Thank you for Order......</h5>"+
                        "</div>"+
                    "</div>"+
                    "<div class='row text-center mt-4'>"+
                        "<div class='col'>"+
                            "<h6>Order Details</h6>"+
                        "</div>"+
                    "</div>"+
                    "<div class='row'>"+
                        "<div class='col'>"+
                            "<h5>Name : "+ request.user.first_name +" "+ request.user.last_name +"</h5>"+
                            "<h5>Email : "+ request.user.email +"</h5>"+
                        "</div>"+
                    "</div>"+
                    "<div class='row'>"+
                        "<div class='col'>"+
                            "<table class='table'>"+
                                "<thead class='table table-dark'>"+
                                    "<tr>"+
                                        "<th>ID</th>"+
                                        "<th>Cloth Name</th>"+
                                        "<th>Price</th>"+
                                        "<th>Ironing</th>"+
                                        "<th>HotWater</th>"+
                                        "<th>Cold Water</th>"+
                                        "<th>Washing Liquid</th>"+
                                        "<th>Softern</th>"+
                                        "<th>Pickup Date and time</th>"+
                                        "<th>Delivery Date and Time</th>"+
                                        "<th>Instruction</th>"+
                                    "</tr>"+
                                "</thead>"+
                                "<tbody>"+
                                    "<tr>"+
                                        "<td>"+ str(order.id)+"</td>"+
                                        "<td>"+ str(order.cloth_name)+"</td>"+
                                        "<td>"+ str(order.price)+"</td>"+
                                        "<td>"+ str(order.ironing) +"</td>"+
                                        "<td>"+ str(order.hot_water) +"</td>"+
                                        "<td>"+ str(order.cold_water) +"</td>"+
                                        "<td>"+ str(order.washing_liquid) +"</td>"+
                                        "<td>"+ str(order.softern) +"</td>"+
                                        "<td>"+ str(order.puckup_date) +" "+ str(order.pickup_time) +"</td>"+
                                        "<td>"+ str(order.delivery) +" "+ str(order.delivery_time) +"</td>"+
                                        "<td>"+ order.instruction +"</td>"+
                                    "</tr>"+
                                "</tbody>"+
                            "</table>"+
                        "</div>"+
                    "</div>"+
                "</div>")


                subject, from_email, to = 'Order Details', settings.EMAIL_HOST_USER, request.user.email
                text_content = 'Thank you for the Order \n Your Order Summary'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                payment = PaymentDetail(image=order.cloth_image,name=request.user.first_name +" " +request.user.last_name,cloth_name=order.cloth_name,price=order.price,phone=detail.phone_number,mobile=detail.mobile_number,address=detail.address,quantity=order.quantity,pick_up_date=order.puckup_date,delivery=order.delivery,ironing=order.ironing,hot_water=order.hot_water,cold_water=order.cold_water,washing_liquid=order.washing_liquid,softern=order.softern)
                payment.save()
            return render(request,"payment_done.html")
    else:
        return redirect("login")




def premium_order(request):
    if request.user.is_authenticated:
        price = request.POST.get('price')
        print(price)
        p = PremiumServicePrice.objects.get()
        user = User.objects.get(id=request.user.id)
        detail = AccountDetail.objects.get(user=user)
        return render(request,'premium_card_detail.html',{'account':detail,"price":p})
    else:
        return redirect('home')


def premium_order_checkout(request):
    if request.user.is_authenticated:
        price = request.POST.get('price')
        user = User.objects.get(id=request.user.id)
        service = PremiumClothService.objects.get(name=user)
        service.premium_services_price=5
        service.save()
        return render(request,'premium_checkout.html',{'price':price})
    else:
        return redirect('home')

def pay_premium_order(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        return render(request,'payment_done.html')
    else:
        return redirect('home')
