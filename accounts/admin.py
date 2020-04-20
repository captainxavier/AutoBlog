from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'date_joined', 'is_admin', 'is_active', 'is_staff', 'last_login')
    search_fields = ('email', 'first_name', 'last_name', 'username')
    readonly_fields = ('email', 'date_joined', 'last_login')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)
