from django.contrib import admin
from .models import ichres, istres, sotres,  hisobot_ich, hisobot_ist, hisobot_uzat, hisobot_item, allfaqir, his_ich,hisobot_full, newclass

class ichAdmin(admin.ModelAdmin):    
    search_files = ('nom')
    ordering = ('nom', 'birlik')
    
admin.site.register(ichres, ichAdmin)

class istAdmin(admin.ModelAdmin):    
    search_files = ('nom', 'birlik')  
    ordering = ('nom', 'birlik')
    
    
admin.site.register(istres, istAdmin)

class SotAdmin(admin.ModelAdmin):    
    search_files = ('sotres.resurs.nomi')
admin.site.register(sotres, SotAdmin)

admin.site.register(hisobot_item)
admin.site.register(hisobot_ich)
admin.site.register(hisobot_ist)
admin.site.register(hisobot_uzat)

admin.site.register(his_ich)
admin.site.register(hisobot_full)

admin.site.register(allfaqir)

admin.site.register(newclass)