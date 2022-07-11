from django.contrib import admin
from .models import Data

class NameAdmin(admin.ModelAdmin):
    change_list_template = 'change_list_graph.html'

admin.site.register(Data,NameAdmin)

