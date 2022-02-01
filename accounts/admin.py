from django.contrib import admin

# Register your models here.
from django.contrib import admin
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'roll', 'is_staff', 'date_joined']

    def save_model(self, request, obj, form, change):
        obj.set_password(obj.password)
        obj.save()
        super(CustomUser, self).save_model(request, obj, form, change)
