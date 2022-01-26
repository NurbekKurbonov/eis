from django.contrib import admin
from .models import davlatlar, viloyatlar, tumanlar,IFTUM, DBIBT, THST, birliklar, resurslar, Valyuta



class davAdmin(admin.ModelAdmin):
    list_display = ('davlat_kodi', 'davlat_nomi')
    ordering = ('davlat_kodi',)
    search_fields = ('davlat_kodi','davlat_nomi')
    
admin.site.register(davlatlar, davAdmin)

class vilAdmin(admin.ModelAdmin):
    list_display = ( 'viloyat_kodi', 'viloyat_nomi','viloyat_davlati')
    ordering = ('viloyat_kodi',)
    search_fields = ('viloyat_davlati', 'viloyat_kodi', 'viloyat_nomi')
    
admin.site.register(viloyatlar, vilAdmin)

class tumAdmin(admin.ModelAdmin):
    list_display = ('tuman_kodi', 'tuman_nomi', 'tuman_viloyati', 'tuman_davlati')
    ordering = ('tuman_kodi',)
    search_files = ('tuman_kodi',' tuman_nomi')
    
admin.site.register(tumanlar, tumAdmin)

class iftumAdmin(admin.ModelAdmin):
    list_display = ('bolim', 'bob', 'guruh', 'sinf','nomi')
    ordering = ('bolim', 'bob', 'guruh', 'sinf', 'nomi')
    search_files = ('bolim', 'bob', 'guruh', 'sinf', 'nomi')    
    
admin.site.register(IFTUM, iftumAdmin)

class DBAdmin(admin.ModelAdmin):
    list_display = ('dbibt', 'ktut', 'nomi')
    ordering = ('dbibt', 'ktut', 'nomi')
    search_files = ('dbibt', 'ktut', 'nomi')    
    
admin.site.register(DBIBT, DBAdmin)

class THSTAdmin(admin.ModelAdmin):
    list_display = ('bolim','tur', 'nomi')
    ordering = ('bolim','tur', 'nomi')
    search_files = ('bolim','tur', 'nomi')    
    
admin.site.register(THST, THSTAdmin)

class birlikAdmin(admin.ModelAdmin):
    list_display = ('birlik', 'asos', 'farq')
    ordering = ('birlik', 'asos', 'farq')
    search_files = ('birlik', 'asos', 'farq')   
    
admin.site.register(birliklar, birlikAdmin)

class resursAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'birlik')
    ordering = ('nomi', 'birlik')
    search_files = ('nomi', 'birlik')  
    
admin.site.register(resurslar, resursAdmin)

admin.site.register(Valyuta)

