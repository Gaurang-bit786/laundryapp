from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class UserDetailAdmin(ImportExportModelAdmin):
    resource_class = UserDetail

admin.site.register(UserDetail,UserDetailAdmin)

