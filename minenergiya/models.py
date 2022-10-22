from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from foydalanuvchi.models import allfaqir
from s_ad.models import birliklar, resurslar

# Create your models here.
class filtr_faqir(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    
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
    nomi = models.TextField('nomi', unique=True)
    fqr=models.ManyToManyField(filtr_faqir, verbose_name=("Foydalanuvchilar"), blank=True)

    class Meta:
        verbose_name = ("guruh")
        verbose_name_plural = ("02_guruhlar")

    def __str__(self):
        return self.nomi

    def get_absolute_url(self):
        return reverse("guruh_detail", kwargs={"pk": self.pk})

class klassifikator(models.Model):
    owner=models.OneToOneField(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    klass=models.TextField('Turi', unique=True)

    class Meta:
        verbose_name = ("klassifikator")
        verbose_name_plural = ("klassifikatorlar")
    
    def __str__(self):
        return f"{self.klass}"

    def get_absolute_url(self):
        return reverse("tur_detail", kwargs={"pk": self.pk})

class tur(models.Model):
    owner=models.OneToOneField(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    tur=models.TextField('Turi', unique=True)

    class Meta:
        verbose_name = ("tur")
        verbose_name_plural = ("turlar")

    def __str__(self):
        return f"{self.tur}"

    def get_absolute_url(self):
        return reverse("tur_detail", kwargs={"pk": self.pk})

class ensamfiltr(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    nomi = models.TextField('nomi', unique=True)
    fqr=models.ManyToManyField(allfaqir, verbose_name=("Foydalanuvchilar"), blank=True)
    resurs=models.ManyToManyField(resurslar, verbose_name=("Resurs"), blank=True)
    vaqt=models.DateTimeField("Vaqti", auto_now_add=False)
    dan=models.DateField("dan", auto_now_add=False)
    gacha=models.DateField("gacha", auto_now_add=False)    
    olchov=models.ManyToManyField(birliklar, verbose_name=("O`lchov birligi"), blank=True)   

    class Meta:
        verbose_name = ("ensamfiltr")
        verbose_name_plural = ("03_Energiya samaradorlik bazasi")

    def __str__(self):
        return f"{self.nomi}: {self.owner}"

    def get_absolute_url(self):
        return reverse("ensamfiltr_detail", kwargs={"pk": self.pk})

        



