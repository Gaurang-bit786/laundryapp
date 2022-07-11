from dis import Instruction
from django.shortcuts import render,redirect
from .models import *
from userauthentication.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives



def premium_order_y(request):
    if request.user.is_authenticated:
        cloth = PremiumClothCategory.objects.all()
        return render(request,'premium_order.html',{'cloth':cloth})
    else:
        return redirect("login")


def premium_order_service(request,id):
    if request.user.is_authenticated:
        cloth = PremiumClothCategory.objects.get(id=id)
        print(cloth)
        cloth = PremiumClothName.objects.filter(cloth_category_name=cloth).all()
        print(cloth)
        user = User.objects.get(id=request.user.id)
        service = PremiumClothService.objects.get(name=user)
        if service.premium_services_price > 0:
            return render(request,'place_premium_order.html',{'cloth':cloth,'service':service})
        else:
            return redirect('premium_order_y')
    else:
        return redirect("login")

def premium_order_confirm(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        service = PremiumClothService.objects.get(name=user)
        data = [request.POST.get("ironing"),
                request.POST.get("hotwater"),
                request.POST.get("coldwater"),
                request.POST.get("washing"),
                request.POST.get("softern")
            ]
        cloth = request.POST.getlist("cloth")
        print(cloth)
        pick_up_date = request.POST.get("puck_up_date")
        delivery = request.POST.get("delivery")
        print(pick_up_date)
        quantity = request.POST.get("qunatity")
        newData = []
        for ele in data:
            if ele is not None:
                newData.append(ele)
        print(newData)
        return render(request,'premium_order_confirm.html',{"data":newData,"quantity":quantity,"pick_up_date":pick_up_date,"cloth":cloth,"delivery":delivery,'service':service})
    else:
        return redirect("login")



def premium_order_summary(request):
    if request.user.is_authenticated:

        user = User.objects.get(id = request.user.id)
        cloth = request.POST.get("cloth")
        quantity = request.POST.get("quantity")
        ironing = request.POST.get("Ironing")
        hot_water = request.POST.get("Hot Water")
        cold_water = request.POST.get("Cold Water")
        washing_liquid = request.POST.get("Washing Liquid")
        softern = request.POST.get("Softern")
        pick_up_date = request.POST.get("pick_up_date")
        delivery = request.POST.get("delivery")
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
        user = User.objects.get(id=request.user.id)
        details = UserDetail.objects.get(username=user)
        order = PremiumOrdersSummary(user=user ,cloth_name=cloth,address=details.address,cloth_image=cloth_image,quantity=quantity,ironing=iron,hot_water=hot_w,cold_water=cold_w,washing_liquid=wash_liq,softern=soft,puckup_date=pick_up_date,delivery=delivery,instruction=order_summary,paid=True)
        order.save()
        service = PremiumClothService.objects.get(name=user)
        if service.premium_services_price > 0:
            service.premium_services_price = service.premium_services_price-1
        else:
            service.premium_services_price = 0
        service.save()
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
                                        "<th>Cloth Name</th>"+
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
                                        "<td>"+ cloth +"</td>"+
                                        "<td>"+ str(iron) +"</td>"+
                                        "<td>"+ str(hot_w) +"</td>"+
                                        "<td>"+ str(cold_w) +"</td>"+
                                        "<td>"+ str(wash_liq) +"</td>"+
                                        "<td>"+ str(soft) +"</td>"+
                                        "<td>"+ str(pick_up_date)  +"</td>"+
                                        "<td>"+ str(delivery) +"</td>"+
                                        "<td>"+ str(order_summary) +"</td>"+
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
        return render(request,'premium_order_confirm_summary.html')
    else:
        return redirect('login')