from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import User
from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    AdminUserCreationForm,
    UserChangeForm
)
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'avatar', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'username', 'avatar')
    
    form = UserChangeForm
    add_form = AdminUserCreationForm 
    change_password_form = AdminPasswordChangeForm
    
    @admin.display(description=_('Аватарка'))
    def get_avatar(self, user):
        if user.avatar:
            return f'<img src="{user.avatar.url}" width="50" height="50" style="border-radius: 50%;">'
        return 'Нет аватарки'