from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from userdata.models import *

User = get_user_model()

class UserDataInline(admin.StackedInline):
    model = UserData
    can_delete = False

class ShippingAddressInline(admin.StackedInline):
    model = ShippingAddress
    extra = 1

class UserAdmin(BaseUserAdmin):
    inlines = (UserDataInline, ShippingAddressInline)
    list_display = ('email', 'username', 'get_user_phone')
    search_fields = ('email', 'username', 'userdata__phone')

    def get_user_phone(self, obj):
        return obj.userdata.phone if hasattr(obj, 'userdata') else None

    get_user_phone.short_description = 'Phone Number'

admin.site.register(User, UserAdmin)
