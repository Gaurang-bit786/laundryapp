from distutils.command import register
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin,ExportActionMixin

class PremiumCLothCategoryAdmin(ImportExportModelAdmin):
    list_display = ['image','cloth_category_name']

class PremiumClothNameAdmin(ImportExportModelAdmin):
    list_display = ['cloth_name','cloth_category_name']

class PremiumClothServiceAdmin(ImportExportModelAdmin):
    list_display = ['name','premium_services_price']


class PremiumOrdersSummaryAdmin(ImportExportModelAdmin):
    list_display = ['user','cloth_name','cloth_image','quantity','ironing','hot_water','cold_water','washing_liquid','softern','puckup_date','delivery','instruction','paid']

admin.site.register(PremiumClothCategory,PremiumCLothCategoryAdmin)
admin.site.register(PremiumClothName,PremiumClothNameAdmin)
admin.site.register(PremiumClothService,PremiumClothServiceAdmin)
admin.site.register(PremiumOrdersSummary,PremiumOrdersSummaryAdmin)
admin.site.register(PremiumServicePrice)