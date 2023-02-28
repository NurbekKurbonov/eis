from django.contrib import admin
from .models import Til, Tarjima, jumla, Tarjimon

# Register your models here.
class ITEM_his(admin.ModelAdmin):    
    ordering = ('id', 'nomi')
    search_files = ('nomi')    

admin.site.register(Til, ITEM_his)
admin.site.register(Tarjima, ITEM_his)
admin.site.register(jumla, ITEM_his)
admin.site.register(Tarjimon, ITEM_his)