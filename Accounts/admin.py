from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from Accounts.models import User, CustomerProfile, SellerProfile

# Register your models here.

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'last_login')}),
        ('Permissions', {'fields': (
            'is_customer',
            'is_seller',
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'name','is_customer', 'is_seller', 'is_staff', 'is_superuser', 'is_active', 'is_staff', 'last_login')
    list_filter = ('is_customer', 'is_seller', 'is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address1','address2','address3', 'phone','city','zipcode', 'country']

admin.site.register(CustomerProfile,UserProfileAdmin)

class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address', 'phone1', 'phone2','city','zipcode', 'country']

admin.site.register(SellerProfile, SellerProfileAdmin)