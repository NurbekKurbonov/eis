from django.db import models
from django.contrib.auth.models import User

from s_ad.models import resurslar

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
    nom = models.TextField('Resurs nomi', max_length=100, unique=True)
    birlik = models.CharField('Resurs birligi', max_length=100)    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = '01_0_Ishlab chiqarish resurslari'

class istres(models.Model):
    nom = models.TextField('Resurs nomi', max_length=100, unique=True)
    birlik = models.CharField('Resurs birligi', max_length=100)    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name_plural = '01_1_Iste`mol resurslari'
        
class sotres(models.Model):
    nom = models.TextField('Resurs nomi', max_length=100, unique=True)
    birlik = models.CharField('Resurs birligi', max_length=100)    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)   
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nom}: {self.birlik}"
    
    class Meta:
        verbose_name_plural = '01_2_Uzatiladigan resurslar'
#hisobotlar********************************************************
class hisobot_item(models.Model):
    title = models.CharField("Hisobot nomi", max_length=100)
    vaqt=models.DateTimeField("Vaqti",auto_now=True, auto_now_add=False) 
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} // {self.vaqt}"
    
    class Meta:
        verbose_name = ("hisobot_shakli")
        verbose_name_plural = ("02_0_Hisobot shakllari")
    
class hisobot_ich(models.Model):
    
    title = models.CharField("Hisobot nomi", max_length=100)
    vaqt=models.DateTimeField("Vaqti",auto_now=True, auto_now_add=False)
    
    nom = models.TextField('Resurs nomi')
    birlik = models.TextField('Resurs birligi')    
    qiymat = models.FloatField("Resurs qiymati")
    qiymat_pul=models.FloatField("Resurs qiymati")
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"{self.title} // {self.vaqt}"
    
    class Meta:
        verbose_name_plural = ("02_1_Ishlab chiqarish hisoboti")

class hisobot_ist(models.Model):
    
    title = models.CharField("Hisobot nomi", max_length=100)
    vaqt=models.DateTimeField("Vaqti",auto_now=True, auto_now_add=False)
    
    nom = models.TextField('Resurs nomi')
    birlik = models.TextField('Resurs birligi')    
    qiymat = models.FloatField("Resurs qiymati")
    qiymat_pul=models.FloatField("Resurs qiymati")
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"{self.title} // {self.vaqt}"
    
    class Meta:
        verbose_name_plural = ("02_2_Iste`mol hisoboti")

class hisobot_uzat(models.Model):
    
    title = models.CharField("Hisobot nomi", max_length=100)
    vaqt=models.DateTimeField("Vaqti",auto_now=True, auto_now_add=False)
    
    nom = models.TextField('Resurs nomi')
    birlik = models.TextField('Resurs birligi')    
    qiymat = models.FloatField("Resurs qiymati")
    qiymat_pul=models.FloatField("Resurs qiymati")
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"{self.title} // {self.vaqt}"
    
    class Meta:
        verbose_name_plural = ("02_3_Uzatilgan resurs hisoboti")

class his_ich(models.Model):
    nomi=models.CharField("Hisobot nomi", max_length=50)
    
    resurs=models.CharField("Resurs", max_length=50)
        
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)    

    class Meta:
        verbose_name = ("Davriy hisobot")
        verbose_name_plural = ("04_0_Davriy hisobotlar")

    def __str__(self):
        return f"{self.nomi}: {self.resurs}"

    def get_absolute_url(self):
        return reverse("his_ich_detail", kwargs={"pk": self.pk})

class hisobot_full(models.Model):
    nomi=models.CharField("Hisobot nomi", max_length=50)
    
    oraliq_min=models.CharField("Maksimal oraliq", max_length=50)
    oraliq_max=models.CharField("Minimal oraliq", max_length=50)
    
    vaqt=models.DateTimeField("Vaqti",auto_now=True, auto_now_add=False) 
    
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("hisobot_full")
        verbose_name_plural = ("04_1_hisobot_full")

    def __str__(self):
        return f"{self.nomi}: {self.oraliq_min} dan {self.oraliq_max} gacha"

    def get_absolute_url(self):
        return reverse("hisobot_full_detail", kwargs={"pk": self.pk})
    
class newclass(models.Model, under_class):
    name=models.CharField(max_length=50)
    class under_class(models.Model):
        name=models.CharField(max_length=50)
        
    
        class Meta:
            verbose_name = ("under_class")
            verbose_name_plural = ("under_classs")
    
        def __str__(self):
            return self.name
    
        def get_absolute_url(self):
            return reverse("under_class_detail", kwargs={"pk": self.pk})
    

    class Meta:
        verbose_name = ("newclass")
        verbose_name_plural = ("newclasss")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("newclass_detail", kwargs={"pk": self.pk})

