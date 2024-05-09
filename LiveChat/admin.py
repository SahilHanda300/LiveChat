from django.contrib import admin
from LiveChat.models import SupportForm
# Register your models here.

class AdminReg(admin.ModelAdmin):
    list_display=("name","email","phoneNumber","queryTitle")

admin.site.register(SupportForm,AdminReg)