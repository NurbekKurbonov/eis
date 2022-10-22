from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


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
    viloyat_davlati = models.ForeignKey(davlatlar, on_delete=models.CASCADE)
    viloyat_kodi = models.FloatField('Viloyat kodi')
    viloyat_nomi = models.CharField('Viloyat nomi', max_length=100)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.viloyat_nomi
    
    class Meta:
        ordering: ['-viloyat_kodi']
        verbose_name_plural = '02_Viloyatlar'
        
class tumanlar(models.Model):
    tuman_viloyati = models.ForeignKey(viloyatlar, on_delete=models.CASCADE)       
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
        return f"{self.bolim}{self.bob}{self.guruh}{self.sinf}{self.tartib}"
    
    class Meta:
        verbose_name_plural = '04_IFTUM kodi'
        
class DBIBT(models.Model):
    dbibt = models.CharField('KTUT kodi', max_length=15)
    ktut = models.CharField('KTUT kodi', max_length=15)
    nomi = models.TextField('DBIBT nomi', unique=True)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.dbibt}/{self.ktut}"
    
    class Meta:
        verbose_name_plural = '05_DBIBT kodi'
    
class THST(models.Model):
    bolim = models.CharField('Klassifikator bo`limi', max_length=15)    
    tur = models.CharField('Klassifikator bo`limi', max_length=15)
    nomi = models.TextField('DBIBT nomi', unique=True)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.bolim}{self.tur}"
    
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

class yaxlitlash(models.Model):    
    nomi = models.CharField('Nomi', max_length=50)
    qiymati = models.FloatField('Qiymati')
    checker=models.BooleanField("Tekshirish", blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomi
    
    class Meta:
        verbose_name_plural = '07_Yaxlitlash qiymatlari'

class resurslar(models.Model):
    nomi = models.TextField('Resurs nomi')
    birlik = models.ForeignKey(birliklar, blank=True, null=True, on_delete=models.CASCADE)  
    yaxlit = models.ForeignKey(yaxlitlash, blank=True, null=True, on_delete=models.CASCADE)
    tshy=models.FloatField("TSHY", blank=True, default=0.0)
    tne=models.FloatField("TNE", blank=True, default=0.0)
    gj=models.FloatField("GJ", blank=True, default=0.0)
    gkal=models.FloatField("GKAL",blank=True, default=0.0)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nomi} : {self.yaxlit}{self.birlik}"
    
    class Meta:
        verbose_name_plural = '08_Resurslar'

class Valyuta(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    name = models.TextField('Nomi', blank=True)
    somda = models.FloatField('Necha so`mi', default=0, blank=True)
    qiymati= models.FloatField("Qancha valyuta", default=0, blank=True)    

    checker=models.BooleanField("Tekshirish", blank=True)
    class Meta:
        verbose_name = ("Valyuta")
        verbose_name_plural = ("09_Valyutalar")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("Valyuta_detail", kwargs={"pk": self.pk})

class Tadbir(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    kodi=models.IntegerField(("Tadbir kodi"))
    nomi=models.TextField(("Tadbir nomi"))

    class Meta:
        verbose_name = ("Tadbir")
        verbose_name_plural = ("10_Tadbirlar")

    def __str__(self):
        return f'[{self.kodi}]: {self.nomi}'

    def get_absolute_url(self):
        return reverse("Tadbirlar_detail", kwargs={"pk": self.pk})
