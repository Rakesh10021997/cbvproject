from django.contrib import admin
from testapp.models import Company
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=['Company_Name','CEO','Location']

admin.site.register(Company,CompanyAdmin)
