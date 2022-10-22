from django.contrib import admin
from .models import Page, Book, Section, Subject, Savol, Javob, Test

class PageAdmin(admin.ModelAdmin):
  list_display = ('title', 'update_date')
  ordering = ('title',)
  search_fields = ('title',)

admin.site.register(Page)
admin.site.register(Book)
admin.site.register(Section)
admin.site.register(Subject)
admin.site.register(Savol)
admin.site.register(Javob)
admin.site.register(Test)