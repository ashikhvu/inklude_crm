from django.contrib import admin
from.models import SalePunchModel,FME_Model,User

# Register your models here.
class Punch(admin.ModelAdmin):
    list_display = ["id","sp_fme","sp_email","sp_whatsapp_no","sp_status"]
admin.site.register(SalePunchModel,Punch)
admin.site.register(User)
admin.site.register(FME_Model)
