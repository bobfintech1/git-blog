from django.contrib import admin
from omg.models import UserModel

# Register your models here.

class CustomAdmin(admin.ModelAdmin):
    list_display = ('name', "sex")

admin.site.register(UserModel, CustomAdmin)