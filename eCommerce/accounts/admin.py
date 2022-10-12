from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.
from .models import GuestEmail
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email','admin')
    list_filter = ('admin','staff','active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),

        ('Permissions', {'fields': ('admin', 'staff', 'active',)}),
    )

    add_fieldsets = (
        (None, {
                'classes': ('wide',),
                'fields':('email', 'password', 'password2')}
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


class GuestEmailAdmin(admin.ModelAdmin):
    search_fields = ('email',)
    class Meta:
        model = GuestEmail



admin.site.register(GuestEmail,GuestEmailAdmin)