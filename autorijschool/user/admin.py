from django.contrib import admin
from .models import Gebruiker
from django.contrib.auth.admin import UserAdmin

@admin.register(Gebruiker)
class GebruikerAdmin(UserAdmin):
    model = Gebruiker
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('adres', 'woonplaats', 'postcode', 'huisnummer', 'rol', 'tussenvoegsel', 'exameninformatie', 'geslaagd')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('username', 'first_name', 'last_name', 'email', 'adres', 'woonplaats', 'postcode', 'huisnummer', 'rol', 'password')}),
    )
    list_display = ['username', 'first_name', 'last_name', 'email', 'adres', 'woonplaats', 'postcode', 'huisnummer', 'rol', 'geslaagd']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    ordering = ['username']
