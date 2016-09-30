from django.contrib import admin

from .models import Myidea
# Register your models here.
class MyideaAdmin(admin.ModelAdmin):
    list_display=['f00','f01']
admin.site.register(Myidea,MyideaAdmin)