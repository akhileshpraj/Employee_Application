from django.contrib import admin

# Register your models here.

from .models import Emp , Testimonial

class EmpAd(admin.ModelAdmin):
    list_display=('name','working','address','emp_id','phone','department')
    search_fields=('name',)
admin.site.register(Emp, EmpAd)


admin.site.register(Testimonial)