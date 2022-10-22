from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField, TimeField

class Page(models.Model):
  title = models.CharField(max_length=60)
  permalink = models.CharField(max_length=12, unique=True)
  update_date = models.DateTimeField('Last Updated')
  bodytext = models.TextField('Page Content')

  def __str__(self):
      return self.title

#****************BOOK**********************************************

class Subject(models.Model):
  owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
  nomi = models.CharField(max_length=120)
  text = models.TextField(blank=True)
  holat=models.BooleanField("Aktivligi")
  fayl=models.FileField("Fayl", upload_to=None, blank=True, default='settings.MEDIA_ROOT/None/1-maruza')
  
  vaqt=models.DateField(auto_now=True, auto_now_add=False)
  def __str__(self):
      return self.nomi

  class Meta:
    verbose_name = "Mavzu"
    verbose_name_plural = "00_3_Mavzular"
    
class Section(models.Model):
  owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
  nomi = models.CharField(max_length=120, blank=True)
  icon = models.TextField('Icon', blank=True)  

  mavzu=models.ManyToManyField(Subject, verbose_name=("Mavzu"), blank=True)

  def __str__(self):
      return self.nomi

  class Meta:
    verbose_name = "Bo'lim"
    verbose_name_plural = "00_2_Bo'limlar"

class Book(models.Model):
  owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
  nomi = models.CharField(max_length=120)
  sana = models.DateField('Published date')

  section=models.ManyToManyField(Section, verbose_name=("Bo'lim"), blank=True)

  vaqt = models.TimeField('Added time')

  emblem=models.ImageField("Emblemasi",upload_to='profile_emb', blank=True, max_length=255, default='profile_emb/book_default.png')
  
  def __str__(self):
      return self.nomi

  class Meta:
    verbose_name = "Kitob"
    verbose_name_plural = "00_1_Kitoblar"

# ------------------------------------ TEST --------------------------------------

class Javob(models.Model):
  javob = models.TextField('Javob')
  #koef = models.IntegerField("Koeffitsiyent")

  def __str__(self):
      return self.javob

  class Meta:
    verbose_name = "Javob"
    verbose_name_plural = "01_1_Javoblar"

class Savol(models.Model):
  owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
  savol = models.TextField('Savol')
  j1 = models.ManyToManyField(Javob, verbose_name="To'g'ri javob", blank=True, related_name='j1')
  j2 = models.ManyToManyField(Javob, verbose_name="Noto'g'ri javob", blank=True, related_name='j2')
  #ball = models.IntegerField('Ball')

  def __str__(self):
      return self.savol

  class Meta:
    verbose_name = "Savol"
    verbose_name_plural = "01_2_Savollar"

class Test(models.Model):
  owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
  nomi = models.CharField(max_length=120)
  sana = models.DateField("Qo'shilgan vaqti")
  davomiylik = models.TimeField('Ishlash vaqti')
  savol = models.ManyToManyField(Savol, verbose_name='Test savoli')

  def __str__(self):
      return self.nomi

  class Meta:
    verbose_name = "Test"
    verbose_name_plural = "01_3_Testlar"