from django.db import models
from django.contrib.auth.models import User

class sahifa(models.Model):

    title = models.CharField("Sarlavha", max_length=50)
    permalink = models.CharField("Link", max_length=12, unique=True)
    update_date = models.DateTimeField("Yangilanish sanasi")
    bodytext = models.TextField("Asosiy qism teksti", blank=True)
    icon = models.CharField("Icon nomi", max_length=30)
                               
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("sahifa")
        verbose_name_plural = ("sahifalar")

    def __str__(self):
        return self.title



