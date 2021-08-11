from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import User
<<<<<<< HEAD
=======

>>>>>>> 8a344c846abef330b47cfc3a375ac60101599f5b

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'instrument', 'genre','nickname', 'instrument', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('instrument',)},{'fields': ('nickname',)},{'fields': ('genre',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'instrument', 'genre','nickname','password1', 'password2')}
         ),
    )
    search_fields = ('email','nickname','genre','instrument',)
    ordering = ('email',)
    filter_horizontal = ()
<<<<<<< HEAD
=======


>>>>>>> 8a344c846abef330b47cfc3a375ac60101599f5b
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#         'nickname',
#         'email',
#         'genre',
#     )
#     list_display_links = (
#         'nickname',
#         'email',
#         'genre',
#     )