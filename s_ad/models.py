from django.db import models
from django.contrib.auth.models import User

#Hududlarb bo'yicha ma'lumotlar**************************

class davlatlar(models.Model):
    davlat_kodi = models.IntegerField('Davlat kodi', unique=True)
    davlat_nomi = models.TextField('Davlat nomi', unique=True)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.davlat_nomi
    
    class Meta:
        ordering: ['-davlat_kodi']
        verbose_name_plural = '01_Davlatlar'
        
class viloyatlar(models.Model):
    viloyat_davlati = models.CharField('Viloyat davlati', max_length=50)
    viloyat_kodi = models.FloatField('Tuman kodi')
    viloyat_nomi = models.CharField('Viloyat nomi', max_length=100)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.viloyat_nomi
    
    class Meta:
        ordering: ['-viloyat_kodi']
        verbose_name_plural = '02_Viloyatlar'
        
class tumanlar(models.Model):
    tuman_davlati = models.CharField('Tuman/shahar nomi', max_length=100)
    tuman_viloyati = models.CharField('Tuman/shahar nomi', max_length=100)
        
    tuman_kodi = models.IntegerField('Tuman/shahar kodi')
    tuman_nomi = models.CharField('Tuman/shahar nomi', max_length=100)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tuman_nomi
    
    class Meta:
        ordering: ['-tuman_kodi']
        verbose_name_plural = '03_Tumanlar'
        
#Kodlar****************************************************************************

class IFTUM(models.Model):
    bolim = models.CharField('Bo`lim', max_length=2)
    bob = models.IntegerField('Bob')
    guruh = models.IntegerField('Guruh')
    sinf = models.IntegerField('Sinf')
    tartib = models.IntegerField('Tartib')
    nomi = models.TextField('IFTUM nomi', unique=True)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomi
    
    class Meta:
        verbose_name_plural = '04_IFTUM kodi'
        
class DBIBT(models.Model):
    dbibt = models.CharField('KTUT kodi', max_length=15)
    ktut = models.CharField('KTUT kodi', max_length=15)
    nomi = models.TextField('DBIBT nomi', unique=True)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomi
    
    class Meta:
        verbose_name_plural = '05_DBIBT kodi'
    
class THST(models.Model):
    bolim = models.CharField('Klassifikator bo`limi', max_length=15)    
    tur = models.CharField('Klassifikator bo`limi', max_length=15)
    nomi = models.TextField('DBIBT nomi', unique=True)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomi
    
    class Meta:
        verbose_name_plural = '06_THShT kodi'
        
class birliklar(models.Model):
    birlik = models.CharField('Birlik', max_length=20)
    asos = models.CharField('Asosi', max_length=20)
    farq = models.FloatField('Farq')
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.birlik
    
    class Meta:
        verbose_name_plural = '07_Birliklar'

class resurslar(models.Model):
    nomi = models.TextField('Resurs nomi')
    birlik = models.CharField('Resurs birligi', max_length=20)    
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nomi} : {self.birlik}"
    
    class Meta:
        verbose_name_plural = '08_Resurslar'

