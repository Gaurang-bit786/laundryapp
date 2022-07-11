from django.contrib import admin

from .models import Routing

class RoutingAdmin(admin.ModelAdmin):
    change_list_template = 'routing.html'

admin.site.register(Routing,RoutingAdmin)




