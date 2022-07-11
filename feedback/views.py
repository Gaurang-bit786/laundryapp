from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import *
from .models import Review
from django.contrib.auth.models import User

def feedback(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            feedback = request.POST.get("feedback")
            print(feedback)
            user = User.objects.get(username=request.user.username)
            review = Review(user=user,review=feedback)
            review.save()
            return render(request, 'feedback.html', {})
        return render(request, 'feedback.html', {})
    else:
        return redirect('login')
    
