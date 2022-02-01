from django.db import models
from django.contrib.auth.models import User

from s_ad.models import resurslar, Valyuta

# user*******************
class allfaqir(models.Model): 
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    nomi=models.CharField("Korxona nomi", max_length=250)
    admin=models.CharField("Boshqaruvchi nomi", max_length=50)
    inn = models.CharField("STIR", max_length=50)
    about=models.TextField("Korxona haqida qisqacha", blank=True)
    emblem=models.ImageField("Emblemasi",upload_to='profile_emb', blank=False, max_length=255)

    class Meta:
        verbose_name = ("Foydalanuvchi")
        verbose_name_plural = ("00_Foydalanuvchilar")

    def __str__(self):
        return f"{self.nomi} - {self.admin} - {self.inn}"

    def get_absolute_url(self):
        return reverse("allfaqir_detail", kwargs={"pk": self.pk})
    
#******************************************************

class ichres(models.Model):
    resurs=models.ForeignKey(resurslar, on_delete=models.CASCADE)  
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.resurs}-{self.owner}"
    
    class Meta:
        verbose_name_plural = '01_0_Ishlab chiqarish resurslari'

class istres(models.Model):
    resurs=models.ForeignKey(resurslar, on_delete=models.CASCADE)  
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.resurs}-{self.owner}"
    
    class Meta:
        verbose_name_plural = '01_1_Iste`mol resurslari'
        
class sotres(models.Model):
    resurs=models.ForeignKey(resurslar, on_delete=models.CASCADE)  
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.resurs}-{self.owner}"
    
    class Meta:
        verbose_name_plural = '01_2_Uzatiladigan resurslar'
        
#hisobotlar********************************************************
class hisobot_ich(models.Model):
    
    title = models.CharField("Hisobot nomi", max_length=100)
    vaqt=models.DateTimeField("Vaqti", auto_now_add=False)
    resurs=models.ForeignKey(ichres, on_delete=models.CASCADE)     
    
    qiymat = models.FloatField("Resurs qiymati")
    qiymat_pul=models.FloatField("Resurs qiymati so`mda")
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"{self.title} // {self.resurs}"
    
    class Meta:
        verbose_name_plural = ("02_1_Ishlab chiqarish hisoboti")
        ordering = ('vaqt',)

class hisobot_ist(models.Model):
    
    title = models.CharField("Hisobot nomi", max_length=100)
    vaqt=models.DateTimeField("Vaqti", auto_now_add=False)
    resurs=models.ForeignKey(istres, on_delete=models.CASCADE)   
    
    qiymat = models.FloatField("Resurs qiymati")
    qiymat_pul=models.FloatField("Resurs qiymati so`mda")
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"{self.title} // {self.resurs}"
    
    class Meta:
        verbose_name_plural = ("02_2_Iste`mol hisoboti")

class hisobot_uzat(models.Model):
    
    title = models.CharField("Hisobot nomi", max_length=100)
    vaqt=models.DateTimeField("Vaqti", auto_now_add=False)
    
    nom = models.TextField('Resurs nomi')
    resurs=models.ForeignKey(sotres, on_delete=models.CASCADE)   
    
    qiymat = models.FloatField("Resurs qiymati")    
    qiymat_pul=models.FloatField("Resurs qiymati so`mda")
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"{self.title} // {self.nom}"
    
    class Meta:
        verbose_name_plural = ("02_3_Uzatilgan resurs hisoboti")

class hisobot_item(models.Model):
    title = models.CharField("Hisobot nomi", max_length=100)
    vaqt=models.DateTimeField("Vaqti", auto_now_add=False) 
    
    ich=models.ManyToManyField(hisobot_ich, verbose_name=("Ishlab chiqarish"), blank=True)
    ist=models.ManyToManyField(hisobot_ist, verbose_name=("Iste'mol"), blank=True)
    uzat=models.ManyToManyField(hisobot_uzat, verbose_name=("Uzatish/Sotish"), blank=True)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} // {self.vaqt}"
    
    class Meta:
        verbose_name = ("hisobot_shakli")
        verbose_name_plural = ("02_0_Hisobot shakllari")
        
#filtrlash
class his_ich(models.Model):
    resurs=models.ForeignKey(resurslar, verbose_name=("Resurslar"), on_delete=models.CASCADE) 
        
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)    

    class Meta:
        verbose_name = ("Davriy hisobot")
        verbose_name_plural = ("04_0_Resurslar filteri")

    def __str__(self):
        return f"{self.resurs}"

    def get_absolute_url(self):
        return reverse("his_ich_detail", kwargs={"pk": self.pk})

class hisobot_full(models.Model):
    nomi=models.CharField("Hisobot nomi", max_length=50)
    
    oraliq_min=models.CharField("Maksimal oraliq", max_length=50)
    oraliq_max=models.CharField("Minimal oraliq", max_length=50)
    
    ich=models.ManyToManyField(hisobot_ich, verbose_name=("Ishlab chiqarish hisobotlari"))
    ist=models.ManyToManyField(hisobot_ist, verbose_name=("Iste'mol hisobotlari"))
    sot=models.ManyToManyField(hisobot_uzat, verbose_name=("Sotish hisobotlari"))
    
    h_item=models.ManyToManyField(hisobot_item, verbose_name=("Umumiy hisobot"))
    
    resurs=models.ManyToManyField(resurslar, verbose_name=("Resurslar"))
    
    cheks=models.CharField("Chart va Birlik", max_length=255)
    tur=models.CharField("Hisobot turi",blank=True, max_length=255)
    valyuta=models.ForeignKey(Valyuta,blank=True, verbose_name=("valyuta"), on_delete=models.CASCADE)
    vaqt=models.DateTimeField("Vaqti", auto_now_add=False) 
    
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("hisobot_full")
        verbose_name_plural = ("04_1_hisobot_full")

    def __str__(self):
        return f"{self.nomi}: {self.oraliq_min} dan {self.oraliq_max} gacha"

    def get_absolute_url(self):
        return reverse("hisobot_full_detail", kwargs={"pk": self.pk})