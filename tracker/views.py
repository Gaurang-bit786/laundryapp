from django.shortcuts import render
from django.http import HttpResponse
from orders.models import OrdersSummary

def tracker(request,id):
    order = OrdersSummary.objects.get(id=id)
    return render(request,'track.html',{"order":order})