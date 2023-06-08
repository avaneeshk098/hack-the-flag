from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Player

# Register your models here.
class PlayerAdmin(UserAdmin):
    list_display = (
        'first_name', 'last_name', 'username', 'email', 'score'
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Score', {
            'fields': ('score',)
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ( 'first_name', 'last_name', 'email')
        }),
        ('Score Info', {
            'fields': ('score',)
        })
    )
admin.site.register(Player, PlayerAdmin)