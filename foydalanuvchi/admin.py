from django.contrib import admin
from .models import ichres, istres, sotres,  hisobot_ich, hisobot_ist, hisobot_uzat, hisobot_item, allfaqir, his_ich,hisobot_full, TexnikTadbir, VVP
from .models import plan_umumiy, plan_ich, plan_ist, plan_uzat, TTT_reja, TTT_umumiy_reja, qtemholat, taklif,sex
admin.site.register(ichres)
admin.site.register(istres)
admin.site.register(sotres)

#SHartnomaviy miqdorlar
admin.site.register(plan_ich)
admin.site.register(plan_ist)
admin.site.register(plan_uzat) 
admin.site.register(plan_umumiy)

#Davriy ma'lumotlar
admin.site.register(hisobot_ich)
admin.site.register(hisobot_ist)
admin.site.register(hisobot_uzat) 

class ITEM_his(admin.ModelAdmin):    
    ordering = ('owner', 'title')
    search_files = ('owner')    

admin.site.register(hisobot_item, ITEM_his)



admin.site.register(his_ich)
admin.site.register(hisobot_full)

admin.site.register(allfaqir)
admin.site.register(TexnikTadbir)
admin.site.register(VVP)
admin.site.register(TTT_reja)
admin.site.register(TTT_umumiy_reja)
admin.site.register(qtemholat)
admin.site.register(taklif)
admin.site.register(sex)