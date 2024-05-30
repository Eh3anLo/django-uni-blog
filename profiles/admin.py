from django.contrib import admin
from .models import UserProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + ('major' , 'profession',)
    
admin.site.register(UserProfile , UserProfileAdmin)