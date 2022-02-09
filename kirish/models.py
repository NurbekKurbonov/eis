from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.models import AbstractUser
import random
from phonenumber_field.modelfields import PhoneNumberField

class sahifa(models.Model):

    title = models.CharField("Sarlavha", max_length=50)
    permalink = models.CharField("Link", max_length=12, unique=True)
    update_date = models.DateTimeField("Yangilanish sanasi")
    bodytext = models.TextField("Asosiy qism teksti", blank=True)
    icon = models.CharField("Icon nomi", max_length=30)
                               
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("sahifa")
        verbose_name_plural = ("01_sahifalar")

    def __str__(self):
        return self.title

class savolnoma(models.Model):
    savol1=models.BooleanField("Ishlab chiqarish/servis mavjudmi?")
    savol2=models.BooleanField("Uzatish mavjudmi?")
    
    owner = models.OneToOneField(to=User, on_delete=models.CASCADE, unique=True)
    
    class Meta:
        verbose_name = ("savolnoma")
        verbose_name_plural = ("02_savolnomalar")

    def __str__(self):
        return self.owner.username
    
class CustomUser(models.Model):    
    phone_number=PhoneNumberField("Telefon nomer", blank=True)

class Code(models.Model):
    number=models.CharField(("nomer"), max_length=6, blank=True)
    owner = models.OneToOneField(to=User, on_delete=models.CASCADE, unique=True)    
    
    class Meta:
        verbose_name = ("Code")
        verbose_name_plural = ("Codes")

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse("Code_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items = []
        
        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)
        
        code_string="".join(str(item) for item in code_items)
        self.number = code_string
            
        super().save(*args, **kwargs)
