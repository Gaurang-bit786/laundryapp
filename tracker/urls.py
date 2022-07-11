from django.urls import path,include
from .views import tracker


urlpatterns = [
    path('tracker/<int:id>',tracker,name="tracker"),
]