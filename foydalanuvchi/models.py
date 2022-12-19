from email.policy import default
from xmlrpc.client import boolean
from django.db import models
from django.contrib.auth.models import User
from s_ad.models import IFTUM, DBIBT, THST, Tadbir, birliklar, yaxlitlash, res_maqsad, yaxlitlash,elon
from django.urls import reverse

from s_ad.models import resurslar, Valyuta, davlatlar, viloyatlar, tumanlar
from kirish.models import savolnoma

   
#******************************************************
class ichres(models.Model):
    resurs=models.ForeignKey(resurslar, on_delete=models.CASCADE)
    maqsad=models.ForeignKey(res_maqsad, verbose_name=("Ishlatish yo'nalishi"), on_delete=models.CASCADE, blank=True, null=True)
    hajm=models.ForeignKey(yaxlitlash, verbose_name=("hajm"), on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    aktiv=models.BooleanField("Aktivlik")
    
    def __str__(self):
        return f"{self.resurs}-{self.owner.id}"
    
    class Meta:
        verbose_name_plural = '01_0_Ishlab chiqarish resurslari'

class istres(models.Model):
    resurs=models.ForeignKey(resurslar, on_delete=models.CASCADE)  
    maqsad=models.ForeignKey(res_maqsad, verbose_name=("Ishlatish yo'nalishi"), on_delete=models.CASCADE, blank=True, null=True)
    hajm=models.ForeignKey(yaxlitlash, verbose_name=("hajm"), on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    aktiv=models.BooleanField("Aktivlik")
    
    def __str__(self):
        return f"{self.resurs}-{self.owner}"
    
    class Meta:
        verbose_name_plural = '01_1_Iste`mol resurslari'
        
class sotres(models.Model):
    resurs=models.ForeignKey(resurslar, on_delete=models.CASCADE)  
    maqsad=models.ForeignKey(res_maqsad, verbose_name=("Ishlatish yo'nalishi"), on_delete=models.CASCADE, blank=True, null=True)
    hajm=models.ForeignKey(yaxlitlash, verbose_name=("hajm"), on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    aktiv=models.BooleanField("Aktivlik")
    
    def __str__(self):
        return f"{self.resurs}-{self.owner}"
    
    class Meta:
        verbose_name_plural = '01_2_Uzatiladigan resurslar'
        
#Shartnomaviy miqdorlar(PLAN)********************************************************
class plan_ich(models.Model):
    
    title = models.CharField("Hisobot nomi", max_length=100)
    vaqt=models.DateTimeField("Vaqti", auto_now_add=False)
    resurs=models.ForeignKey(ichres, on_delete=models.CASCADE)     
    
    qiymat = models.FloatField("Resurs qiymati")
    qiymat_pul=models.FloatField("Resurs qiymati so`mda")
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"{self.title} // {self.resurs}"
    
    class Meta:
        verbose_name_plural = ("02_1_Ishlab chiqarish rejasi")
        ordering = ('vaqt',)

class plan_ist(models.Model):
    
    title = models.CharField("Hisobot nomi", max_length=100)
    vaqt=models.DateTimeField("Vaqti", auto_now_add=False)
    resurs=models.ForeignKey(istres, on_delete=models.CASCADE)   
    
    qiymat = models.FloatField("Resurs qiymati")
    qiymat_pul=models.FloatField("Resurs qiymati so`mda")
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"{self.title} // {self.resurs}"
    
    class Meta:
        verbose_name_plural = ("02_2_Iste`mol rejasi")

class plan_uzat(models.Model):    
    title = models.CharField("Hisobot nomi", max_length=100)
    vaqt=models.DateTimeField("Vaqti", auto_now_add=False)
    
    nom = models.TextField('Resurs nomi')
    resurs=models.ForeignKey(sotres, on_delete=models.CASCADE)   
    
    qiymat = models.FloatField("Resurs qiymati")    
    qiymat_pul=models.FloatField("Resurs qiymati so`mda")
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"{self.title} // {self.resurs}"
    
    class Meta:
        verbose_name_plural = ("02_3_Uzatilgan resurs rejasi")

class plan_umumiy(models.Model):
    title = models.CharField("Hisobot nomi", max_length=100)
    vaqt=models.DateTimeField("Vaqti", auto_now_add=False) 
    
    ich=models.ManyToManyField(plan_ich, verbose_name=("Ishlab chiqarish"), blank=True)
    ist=models.ManyToManyField(plan_ist, verbose_name=("Iste'mol"), blank=True)
    uzat=models.ManyToManyField(plan_uzat, verbose_name=("Uzatish/Sotish"), blank=True)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} // {self.vaqt}===>>>{self.owner}"
    
    class Meta:
        verbose_name = ("hisobot_shakli")
        verbose_name_plural = ("02_0_Umumiy shartnomaviy miqdorlar")

# hisobotlar********************************************************
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
        verbose_name_plural = ("03_1_Ishlab chiqarish hisoboti")
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
        verbose_name_plural = ("03_2_Iste`mol hisoboti")

class hisobot_uzat(models.Model):
    
    title = models.CharField("Hisobot nomi", max_length=100)
    vaqt=models.DateTimeField("Vaqti", auto_now_add=False)
    
    nom = models.TextField('Resurs nomi')
    resurs=models.ForeignKey(sotres, on_delete=models.CASCADE)   
    
    qiymat = models.FloatField("Resurs qiymati")    
    qiymat_pul=models.FloatField("Resurs qiymati so`mda")
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"{self.title} // {self.resurs}"
    
    class Meta:
        verbose_name_plural = ("03_3_Uzatilgan resurs hisoboti")

class hisobot_item(models.Model):
    title = models.CharField("Hisobot nomi", max_length=100)
    vaqt=models.DateTimeField("Vaqti", auto_now_add=False) 
    
    ich=models.ManyToManyField(hisobot_ich, verbose_name=("Ishlab chiqarish"), blank=True)
    ist=models.ManyToManyField(hisobot_ist, verbose_name=("Iste'mol"), blank=True)
    uzat=models.ManyToManyField(hisobot_uzat, verbose_name=("Uzatish/Sotish"), blank=True)
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} // {self.vaqt}===>>>{self.owner}"
    
    class Meta:
        verbose_name = ("hisobot_shakli")
        verbose_name_plural = ("03_0_Hisobot shakllari")
        
#filtrlash
class his_ich(models.Model):
    resurs=models.ForeignKey(resurslar, verbose_name=("Resurslar"), on_delete=models.CASCADE) 
        
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)    

    class Meta:
        verbose_name = ("hisobot")
        verbose_name_plural = ("04_2_Hisobot_bolasi")

    def __str__(self):
        return f"{self.resurs}===>{self.owner}"

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
    
    koef=models.ForeignKey(yaxlitlash, verbose_name=("Koeffitsient"), on_delete=models.CASCADE, blank=True, null=True)
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("hisobot_full")
        verbose_name_plural = ("04_1_hisobot_full")

    def __str__(self):
        return f"{self.nomi}: {self.oraliq_min} dan {self.oraliq_max} gacha ====>>>> {self.owner}"

    def get_absolute_url(self):
        return reverse("hisobot_full_detail", kwargs={"pk": self.pk})

#**************texnik tadbir****************************************************
class TexnikTadbir(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)

    sana=models.DateField(("Sana"), auto_now=False, auto_now_add=False)
    tadbir=models.ForeignKey(Tadbir, verbose_name=("Tadbir nomi"), on_delete=models.CASCADE, default="",blank=True, null=True)
    izoh=models.TextField("Izoh", blank=True)
    resurs=models.ForeignKey(resurslar, verbose_name=("Tejalgan resurs"), on_delete=models.CASCADE, default="",blank=True, null=True)
    tejaldi=models.FloatField(("Tejalgan energiya miqdori"), blank=True)
    

    class Meta:
        verbose_name = ("TexnikTadbir")
        verbose_name_plural = ("05_Texnik Tadbirlar")

    def __str__(self):
        return f'{self.owner}: {self.sana} // {self.tadbir}'

    def get_absolute_url(self):
        return reverse("TexnikTadbir_detail", kwargs={"pk": self.pk})
        
class TTT_reja(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    T_ID=models.IntegerField(("T_ID"), blank=True)
    sana=models.DateField(("Sana"), auto_now=True, auto_now_add=False, blank=True)
    aktiv=models.BooleanField(("Aktivlik"), default=False)

    guruh=models.ForeignKey(Tadbir, verbose_name=("Tadbir guruhi"), on_delete=models.CASCADE, default="",blank=True, null=True)
    nomi=models.TextField("Nomi", blank=True)

    dan=models.DateField(("dan"), auto_now=False, auto_now_add=False, blank=True, null=True)
    gacha=models.DateField(("gacha"), auto_now=False, auto_now_add=False, blank=True, null=True)
    
    tejaladi=models.FloatField(("Tejaladigan energiya miqdori"), blank=True, default=0)
    tejaladi_pul=models.FloatField(("Tejaladigan energiya miqdori"), blank=True, default="0")
    izoh=models.TextField("Izoh", blank=True)

    #*********BAJARILISH HOLATI**********************
    tejaldi=models.FloatField(("Tejalgan energiya miqdori"), blank=True, default=0)
    tejaldi_pul=models.FloatField(("Tejalgan energiya miqdori"), blank=True, default="0")
    tugadi_sanasi=models.DateField(("Tugash sanasi"), auto_now=False, auto_now_add=False, blank=True, null=True)
    bajarilishi=models.FloatField(("Bajarilishi"), blank=True, default=0)
    nega=models.TextField("Nega bajarilmadi", blank=True)

    

    class Meta:
        verbose_name = ("TTT_reja")
        verbose_name_plural = ("05_TTT_rejalar")

    def __str__(self):
        return f'{self.nomi} // {self.owner}: {self.T_ID} // '

    def get_absolute_url(self):
        return reverse("TexnikTadbir_detail", kwargs={"pk": self.pk})

class oraliq(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    dan=models.DateField(("dan"), auto_now=True, auto_now_add=False, blank=True)
    gacha=models.DateField(("dan"), auto_now=True, auto_now_add=False, blank=True)

    class Meta:
        verbose_name = ("oraliq")
        verbose_name_plural = ("oraliqlar")

    def __str__(self):
        return self.owner

    def get_absolute_url(self):
        return reverse("oraliq_detail", kwargs={"pk": self.pk})

class TTT_umumiy_reja(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    T_ID=models.IntegerField(("Tejalgan energiya miqdori"), blank=True)
    sana=models.DateField(("Sana"), auto_now=True, auto_now_add=False)
    
    resurs=models.ForeignKey(resurslar, verbose_name=("Tejalgan resurs"), on_delete=models.CASCADE, default="",blank=True, null=True)

    tejaladi=models.FloatField(("Tejaladigan energiya miqdori"), blank=True)
    tejaladi_pul=models.FloatField(("Tejaladigan energiya miqdori"), blank=True)

    dan=models.DateField(("dan"), auto_now=False, auto_now_add=False, blank=True)
    gacha=models.DateField(("gacha"), auto_now=False, auto_now_add=False, blank=True)

    TTT_rejalar=models.ManyToManyField(TTT_reja, verbose_name=("TTT lar"), blank=True)
    #Bajarilishi***********************************

    tugatildi=models.BooleanField(("Tugatildi"), default=False)
    tejaldi=models.FloatField(("Tejalgan energiya miqdori"), blank=True, default=0)
    tejaldi_pul=models.FloatField(("Tejlgan energiya miqdori"), blank=True, default="0")
    tugash_sanasi=models.DateField(("Tugash sanasi"), auto_now=False, auto_now_add=False, blank=True, null=True)
    
    bajarilishi=models.FloatField(("Bajarilishi"), blank=True, default=0)

    
    class Meta:
        verbose_name = ("TTT_umumiy_reja")
        verbose_name_plural = ("05_TTT_umumiy_rejalar")

    def __str__(self):
        return f'{self.owner}: {self.T_ID} //{self.tugatildi}'

    def get_absolute_url(self):
        return reverse("TexnikTadbir_detail", kwargs={"pk": self.pk})


class VVP(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    sana=models.DateField(("Sana"), auto_now=False, auto_now_add=False )

    nomi=models.TextField("Mahsulot nomi", blank=True)
    VVP=models.FloatField(("IShlab chiqarilgan mahsulot miqdori"))
    birlik=models.ForeignKey(birliklar, verbose_name=("birlik"), on_delete=models.CASCADE)
    pul=models.FloatField(("Ishlab chiqarilgan mahsulot miqdori pul birligida"))
    pul_birlik=models.ForeignKey(Valyuta, verbose_name=("Pul birlik"), on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("VVP")
        verbose_name_plural = ("06_VVP")

    def __str__(self):
        return f'{self.owner}//{self.nomi}'

    def get_absolute_url(self):
        return reverse("VVP_detail", kwargs={"pk": self.pk})

class qtemholat(models.Model):
    owner=models.ForeignKey(to=User, verbose_name=("Egasi"), on_delete=models.CASCADE)
    sana=models.DateField(("Sana"), auto_now_add=True )

    aktiv=models.BooleanField("Aktivlik")
    
    panel=models.FloatField(("O'rnatilgan panel"), blank=True, null=True)
    kollektor=models.FloatField(("O'rnatilgan kollektor"), blank=True, null=True)

    yypanel=models.FloatField(("Yil yakunigacha o'rnatiladigan panel"), blank=True, null=True)
    yykollektor=models.FloatField(("Yil yakunigacha o'rnatiladigan kollektor"), blank=True, null=True)

    panel23=models.FloatField(("2023 yilda o'rnatiladigan panel"), blank=True, null=True)
    kollektor23=models.FloatField(("2023 yilda o'rnatiladigan kollektor"), blank=True, null=True)    

    class Meta:
        verbose_name = ("qtemholat")
        verbose_name_plural = ("qtemholatlar")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("qtemholat_detail", kwargs={"pk": self.pk})




# user*******************
    
class allfaqir(models.Model): 
    owner=models.OneToOneField(to=User, verbose_name=("Xodimlar"), on_delete=models.CASCADE, null=True, blank=True)
    inn = models.CharField("STIR", max_length=50)
    funksiya=models.ForeignKey(savolnoma, verbose_name=("Funksiyalari"), on_delete=models.CASCADE, blank=True, null=True)
    nomi=models.CharField("Korxona nomi", max_length=250, blank=True)    
    iftum=models.ForeignKey(IFTUM, verbose_name=("IFTUM"), on_delete=models.CASCADE, default="",blank=True, null=True)
    dbibt=models.ForeignKey(DBIBT, verbose_name=("DBIBT"), on_delete=models.CASCADE, default="",blank=True, null=True)    
    thst=models.ForeignKey(THST, verbose_name=("THST"), on_delete=models.CASCADE, default="",blank=True, null=True)    
    
    mobil=models.CharField("Ish boshqaruvchi raqami", max_length=12, blank=True)
    tel=models.CharField("Korxona raqami", max_length=12, blank=True)
    
    dav=models.ForeignKey(davlatlar, verbose_name=("Davlat"), on_delete=models.CASCADE, default="",blank=True, null=True)
    vil=models.ForeignKey(viloyatlar, verbose_name=("Viloyat"), on_delete=models.CASCADE, default="",blank=True, null=True)
    tum=models.ForeignKey(tumanlar, verbose_name=("Tuman"), on_delete=models.CASCADE, default="",blank=True, null=True)
    manzil=models.TextField("Manzil", blank=True)

    about=models.TextField("Korxona haqida qisqacha", blank=True)
    emblem=models.ImageField("Emblemasi",upload_to='profile_emb', blank=True, max_length=255, default='profile_emb/login_emb.jpg')
    
    ichres=models.ManyToManyField(ichres, verbose_name=("Ish chiq/xizmat ko'rsatish resurslari"), blank=True)
    istres=models.ManyToManyField(istres, verbose_name=("Iste'mol resurslari"), blank=True)
    sotres=models.ManyToManyField(sotres, verbose_name=("Uzat/sot resurslari"), blank=True)

    reja=models.ManyToManyField(plan_umumiy, verbose_name=("Reja hisobotlari"), blank=True)
    fakt=models.ManyToManyField(hisobot_item, verbose_name=("Fakt hisobotlari"), blank=True)
    TexnikTadbir=models.ManyToManyField(TTT_umumiy_reja, verbose_name=("Texnik tadbirlar"), blank=True)
    VVP=models.ManyToManyField(VVP, verbose_name=("Ishlab chiqarilgan mahsulotlar"), blank=True)
    hisobot=models.ManyToManyField(hisobot_full, verbose_name=("Ishlab chiqarilgan mahsulotlar"), blank=True)
    elon=models.ManyToManyField(elon, verbose_name=("Xabarlar"), blank=True)

    class Meta:
        verbose_name = ("Foydalanuvchi")
        verbose_name_plural = ("00_Foydalanuvchilar")

    def __str__(self):
        return f"{self.nomi} - {self.inn}//{self.owner.id}"

    def get_absolute_url(self):
        return reverse("allfaqir_detail", kwargs={"pk": self.pk})

