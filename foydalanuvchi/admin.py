from django.contrib import admin
from .models import ichres, istres, sotres,  hisobot_ich, hisobot_ist, hisobot_uzat, hisobot_item, allfaqir, his_ich,hisobot_full

admin.site.register(ichres)
admin.site.register(istres)
admin.site.register(sotres)
    


class ITEM_his(admin.ModelAdmin):    
    ordering = ('owner', 'title')
    search_files = ('owner')    

admin.site.register(hisobot_item, ITEM_his)

admin.site.register(hisobot_ich)
admin.site.register(hisobot_ist)
admin.site.register(hisobot_uzat)

admin.site.register(his_ich)
admin.site.register(hisobot_full)

admin.site.register(allfaqir)