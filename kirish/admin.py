from django.contrib import admin

from .models import sahifa

class sahifaAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    orderinh = ('title',)
    search_fields = ('title',)
    
admin.site.register(sahifa, sahifaAdmin)
