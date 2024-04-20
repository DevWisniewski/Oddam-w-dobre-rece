from django.contrib import admin
from .models import Category, Institution, Donation


class CategoryAdmin(admin.ModelAdmin):
    """
    Konfiguracja panelu administracyjnego dla modelu Category, ułatwiająca zarządzanie kategoriami darów.
    """
    list_display = ('name',)  # Wyświetla nazwę kategorii w panelu listy.
    search_fields = ('name',)  # Umożliwia wyszukiwanie kategorii po nazwie.


class InstitutionAdmin(admin.ModelAdmin):
    """
    Konfiguracja panelu administracyjnego dla modelu Institution, umożliwiająca efektywne zarządzanie instytucjami.
    """
    list_display = ('name', 'type', 'description')  # Określa, które pola modelu są wyświetlane w panelu listy.
    list_filter = ('type',)  # Dodaje filtry po typie instytucji na panelu bocznym.
    search_fields = ('name', 'description')  # Umożliwia wyszukiwanie instytucji po nazwie i opisie.
    ordering = ('name',)  # Ustawia domyślne sortowanie instytucji po nazwie.
    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'description')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('categories',),
        }),
    )  # Organizuje pola formularza w sekcje, w tym rozwijaną sekcję opcji zaawansowanych.


class DonationAdmin(admin.ModelAdmin):
    """
    Konfiguracja panelu administracyjnego dla modelu Donation, umożliwiająca zarządzanie informacjami o darowiznach.
    """
    list_display = ('quantity', 'institution', 'pick_up_date')  # Wyświetla kluczowe informacje o darowiznach.
    list_filter = ('institution',)  # Umożliwia filtrowanie darowizn po instytucjach.
    search_fields = ('institution__name', 'pick_up_date')  # Umożliwia wyszukiwanie darowizn po nazwie instytucji i dacie odbioru.
    date_hierarchy = 'pick_up_date'  # Dodaje hierarchię dat, ułatwiającą nawigację po datach.


# Rejestracja modeli wraz z klasami konfiguracyjnymi w panelu administracyjnym
admin.site.register(Category, CategoryAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Donation, DonationAdmin)
