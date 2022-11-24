from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from foydalanuvchi.models import allfaqir
from s_ad.models import birliklar, resurslar

# Create your models here.
class filtr_faqir(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    E_ID=models.CharField('E_ID',blank=True, max_length=50)
    fqr=models.ForeignKey(allfaqir, verbose_name=("Korxonalar"), on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = ("Filtr korxonasi")
        verbose_name_plural = ("01_Filtr uchun Korxonalar")

    def __str__(self):
        return f"{self.owner}//{self.fqr}"

    def get_absolute_url(self):
        return reverse("filtr_faqir_detail", kwargs={"pk": self.pk})

class guruh(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    E_ID=models.CharField('E_ID',blank=True, max_length=50)
    nomi = models.TextField('nomi', )
    fqr=models.ManyToManyField(filtr_faqir, verbose_name=("Foydalanuvchilar"), blank=True)

    class Meta:
        verbose_name = ("guruh")
        verbose_name_plural = ("02_guruhlar")

    def __str__(self):
        return self.nomi

    def get_absolute_url(self):
        return reverse("guruh_detail", kwargs={"pk": self.pk})

class klassifikator(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    E_ID=models.CharField('E_ID',blank=True, max_length=50)
    klass=models.TextField('Turi', )

    class Meta:
        verbose_name = ("klassifikator")
        verbose_name_plural = ("klassifikatorlar")
    
    def __str__(self):
        return f"{self.klass}"

    def get_absolute_url(self):
        return reverse("tur_detail", kwargs={"pk": self.pk})

class tur(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    E_ID=models.CharField('E_ID',blank=True, max_length=50)
    tur=models.TextField('Turi')

    class Meta:
        verbose_name = ("tur")
        verbose_name_plural = ("turlar")

    def __str__(self):
        return f"{self.tur}"

    def get_absolute_url(self):
        return reverse("tur_detail", kwargs={"pk": self.pk})

class his_res(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    E_ID=models.CharField('E_ID',blank=True, max_length=50)
    resurs=models.ForeignKey(resurslar, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("hisobot resursi")
        verbose_name_plural = ("hisobot resurslari")

    def __str__(self):
        return f"{self.resurs}//{self.E_ID}"

    def get_absolute_url(self):
        return reverse("tur_detail", kwargs={"pk": self.pk})

class ensamfiltr(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    E_ID=models.CharField('E_ID',blank=True, max_length=50)
    nomi = models.TextField('nomi')
    vaqt=models.DateTimeField("Vaqti", auto_now_add=False, blank=True, null=True)

    filtr_faqir=models.ManyToManyField(filtr_faqir, verbose_name=("Foydalanuvchilar"), blank=True)    
    guruh=models.ManyToManyField(guruh, verbose_name=("Guruhlar"), blank=True)    
    klassifikator=models.ManyToManyField(klassifikator, verbose_name=("klassifikator"), blank=True)    
    tur=models.ManyToManyField(tur, verbose_name=("tur"), blank=True)  
    his_res=models.ManyToManyField(his_res, verbose_name=("tur"), blank=True)
    
    dan=models.DateField("dan", auto_now_add=False, blank=True, null=True)
    gacha=models.DateField("gacha", auto_now_add=False, blank=True, null=True)    
    olchov=models.TextField('O`lchov birliklari', blank=True, null=True)
    shakl=models.TextField('Hisobot shakli', blank=True, null=True)
    
    #michpar:
    #hajm_mich= models.IntegerField("Hajm")    
    #jadval_mich = models.BooleanField("Jadvalni ko'rsatish")

    #michpar:
    #hajm_sarf= models.IntegerField("Hajm")    
    #jadval_sarf = models.BooleanField("Jadvalni ko'rsatish")

    #ssk:
    #hajm_ssk= models.IntegerField("Hajm")    
    #jadval_ssk = models.BooleanField("Jadvalni ko'rsatish")

    class Meta:
        verbose_name = ("ensamfiltr")
        verbose_name_plural = ("0_Universal filtr bazasi")

    def __str__(self):
        return f"{self.nomi}: {self.owner}"

    def get_absolute_url(self):
        return reverse("ensamfiltr_detail", kwargs={"pk": self.pk})

#**********Chizma parametrlari****************************
class michpar(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    hajm= models.IntegerField("Hajm")
    
    Jadval = models.BooleanField("Jadvalni ko'rsatish")
    
    class Meta:
        verbose_name = ("ensamfiltr")
        verbose_name_plural = ("0_Universal filtr bazasi")

    def __str__(self):
        return f"{self.nomi}: {self.owner}"

    def get_absolute_url(self):
        return reverse("ensamfiltr_detail", kwargs={"pk": self.pk})


#*****************IQTISODIY SAMARA*********************
class ver(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    nomi= models.TextField("Savol")
    MB= models.FloatField("Bajarilish bosqichlari", blank=True, null=True)
    TS= models.FloatField("Takrorlanishlar soni", blank=True, null=True)
    TO= models.FloatField("Takrorlanishlar oralig'i", blank=True, null=True)
    tj= models.FloatField("Bajarish uchun joriy ketgan vaqt", blank=True, null=True)
    tk= models.FloatField("Dastur bajarish vaqti", blank=True, null=True)
    i0= models.FloatField("Bajaruvchining kunlik ish haqqi", blank=True, null=True)

    class Meta:
        verbose_name = ("variant")
        verbose_name_plural = ("variantlar")

    def __str__(self):
        return self.nomi

    def get_absolute_url(self):
        return reverse("kriteriya_detail", kwargs={"pk": self.pk})


class kriteriya(models.Model):
    nomi= models.TextField("Savol")
    ver=models.ManyToManyField(ver, verbose_name=("Variantlar"), blank=True)
    kp=models.FloatField("Dasturga inson aralashuvi koeffitsiyenti", blank=True, null=True)
    class Meta:
        verbose_name = ("kriteriya")
        verbose_name_plural = ("kriteriyalar")

    def __str__(self):
        return self.nomi

    def get_absolute_url(self):
        return reverse("kriteriya_detail", kwargs={"pk": self.pk})

class miqdorlar(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)

    ichres= models.TextField("Ishlab chiqarish resurslari miqdori", blank=True, null=True)
    istres= models.TextField("Ishlab chiqarish resurslari miqdori", blank=True, null=True)
    sotres= models.TextField("Ishlab chiqarish resurslari miqdori", blank=True, null=True)
    his= models.TextField("Hisobotlar miqdori", blank=True, null=True)
    
    ver=models.ManyToManyField(ver, verbose_name=("Variantlar"), blank=True)
    kp=models.FloatField("Dasturga inson aralashuvi koeffitsiyenti", blank=True, null=True)
    class Meta:
        verbose_name = ("kriteriya")
        verbose_name_plural = ("kriteriyalar")

    def __str__(self):
        return self.nomi

    def get_absolute_url(self):
        return reverse("kriteriya_detail", kwargs={"pk": self.pk})
