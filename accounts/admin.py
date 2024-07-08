from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser , OTP
from .forms import CustomUserChangeForm , CustomUserCreationForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None , {'fields' : ('age' , 'img' ,)} ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None , {'fields' : ('age' , 'img' ,)} ),
    )

admin.site.register(CustomUser , CustomUserAdmin)
admin.site.register(OTP)

