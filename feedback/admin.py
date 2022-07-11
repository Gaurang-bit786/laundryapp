from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class ReviewAdmin(ImportExportModelAdmin):
    resource_class = Review


admin.site.register(Review,ReviewAdmin)
