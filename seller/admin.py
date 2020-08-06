from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#from .forms import CustomUserCreationForm, CustomUserChangeForm
#sfrom .models import Account
#from user.forms import CreateUserForm, UserUpdateForm

# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     add_form = CreateUserForm
#     form = UserUpdateForm
#     model = Account
#     list_display = ('email','is_customer', 'is_seller', 'is_staff', 'is_active',)
#     list_filter = ('email','is_customer', 'is_seller', 'is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2','is_customer', 'is_seller', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)


# admin.site.register(Account, CustomUserAdmin)