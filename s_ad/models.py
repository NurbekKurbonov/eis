from django.db import models
from django.contrib.auth.models import User

class davlatlar(models.Model):
    davlat_kodi = models.IntegerField('Davlat kodi')
    davlat_nomi = models.CharField(max_length=100)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.davlat_nomi
    
    class Meta:
        ordering: ['-davlat_kodi']
        verbose_name_plural = '01_Davlatlar'