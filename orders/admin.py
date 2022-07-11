from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class ClothCategoryAdmin(ImportExportModelAdmin):
    list_display = ['id','image','cloth_category_name']

class ClothNameAdmin(ImportExportModelAdmin):
    list_display = ['id','cloth_category_name','cloth_name','price','number_of_clothes']

class OrdersSummaryAdmin(ImportExportModelAdmin):
    list_display = ['id','user','cloth_name','quantity','price','ironing','hot_water','cold_water','washing_liquid','softern','puckup_date','delivery','instruction','paid']



class PaymentDetailAdmin(ImportExportModelAdmin):
    list_display = ['id','name','cloth_name','price','phone','mobile','address','quantity','ironing','hot_water','cold_water','washing_liquid','softern','pick_up_date','delivery']




admin.site.register(ClothCategory,ClothCategoryAdmin)
admin.site.register(ClothName,ClothNameAdmin)
admin.site.register(OrdersSummary,OrdersSummaryAdmin)
admin.site.register(AccountDetail)
admin.site.register(PaymentDetail,PaymentDetailAdmin)
