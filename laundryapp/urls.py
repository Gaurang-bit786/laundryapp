from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userauthentication.urls')),
    path('', include('feedback.urls')),
    path('', include('orders.urls')),
    path('', include('premium.urls')),
    path('',include('helpline.urls')),
    path('',include('data.urls')),
    path('',include('tracker.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
