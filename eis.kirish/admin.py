from django.contrib import admin

from .models import sahifa, savolnoma

class sahifaAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    orderinh = ('title',)
    search_fields = ('title',)
    
admin.site.register(sahifa, sahifaAdmin)

class SavAdmin(admin.ModelAdmin):
    list_display = ('owner', 'savol1','savol2')
    orderinh = ('title',)
    search_fields = ('title',)
   
    
admin.site.register(savolnoma, SavAdmin)