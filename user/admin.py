from django.contrib import admin
from user.models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address1','address2','address3', 'phone','city','zipcode', 'country']

admin.site.register(UserProfile,UserProfileAdmin)