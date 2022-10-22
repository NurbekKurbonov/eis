from django.contrib import admin
from .models import filtr_faqir, guruh, ensamfiltr, tur, klassifikator

# Register your models here.
admin.site.register(filtr_faqir)
admin.site.register(guruh)
admin.site.register(ensamfiltr)
admin.site.register(tur)
admin.site.register(klassifikator)