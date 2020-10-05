from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from appUser.models import UserType, UserExtend

# Register your models here.


class UsuarioInline(admin.StackedInline):
    model = UserExtend
    can_delete = False
    verbose_name = 'extención usuario'
    verbose_name_plural = 'extención usuarios'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (UsuarioInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserType)
