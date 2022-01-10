from django.contrib import admin
from .models import davlatlar

class davAdmin(admin.ModelAdmin):
    list_display = ('davlat_kodi', 'davlat_nomi')
    orderinh = ('davlat_kodi',)
    search_fields = ('davlat_kodi','davlat_nomi')
    
admin.site.register(davlatlar, davAdmin)

