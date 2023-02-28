from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Til(models.Model):
    nomi=models.TextField("Jumla")  
    tarjimonlar=models.ManyToManyField(to=User, verbose_name=("Tarjimonlar"), blank=True)
    bayroq=models.ImageField("Bayroq",upload_to='bayroq', blank=True, max_length=255)
    vaqt=models.DateTimeField("Vaqti", auto_now_add=True, blank=True, null=True)
    
    class Meta:
        verbose_name = ("Til")
        verbose_name_plural = ("02_Tillar")

    def __str__(self):
        return self.nomi

    def get_absolute_url(self):
        return reverse("03_Til_detail", kwargs={"pk": self.pk})

class Tarjima(models.Model):
    nomi=models.TextField("Tarjima")
    til=models.ForeignKey(Til, verbose_name=("Tili"), on_delete=models.CASCADE)     
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)    
    vaqt=models.DateTimeField("Vaqti", auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = ("Tarjima")
        verbose_name_plural = ("03_Tarjimalar")

    def __str__(self):
        return self.nomi

    def get_absolute_url(self):
        return reverse("Tarjima_detail", kwargs={"pk": self.pk})

class jumla(models.Model):
    nomi=models.TextField("Jumla")        
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    vaqt=models.DateTimeField("01_Vaqti", auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = ("jumla")
        verbose_name_plural = ("01_jumlalar")

    def __str__(self):
        return self.nomi

    def get_absolute_url(self):
        return reverse("jumla_detail", kwargs={"pk": self.pk})
    
class Tarjimon(models.Model):
    nomi=models.ForeignKey(jumla, verbose_name=("Jumla"), on_delete=models.CASCADE)
    tarjimasi=models.ManyToManyField(Tarjima, verbose_name=("Tarjimalari"), blank=True)

    class Meta:
        verbose_name = ("Tarjimon")
        verbose_name_plural = ("04_Tarjimon")

    def __str__(self):
        return self.nomi.nomi

    def get_absolute_url(self):
        return reverse("Tarjimon_detail", kwargs={"pk": self.pk})

