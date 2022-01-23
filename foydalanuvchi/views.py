from django.shortcuts import render, redirect


from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
import datetime

#modelsdan chaqirish******************
from s_ad.models import resurslar
from .models import ichres, istres, sotres, hisobot_item, hisobot_ich, hisobot_ist, hisobot_uzat, allfaqir, hisobot_full, his_ich
from kirish.models import savolnoma

#____***_____Bosh sahifa_____***_____________________
def home(request):    
    hammasi = allfaqir.objects.filter(owner=request.user)
    
    vaqt=timezone.now()
    
    h_ich=hisobot_ich.objects.filter(owner=request.user)
    h_ist=hisobot_ist.objects.filter(owner=request.user)
    h_uzat=hisobot_uzat.objects.filter(owner=request.user)
    
    full_ich=0
    for v in h_ich:
        full_ich += v.qiymat_pul
    
    full_ist=0
    for v in h_ist:
        full_ist += v.qiymat_pul
    
    titleown="Bosh menyu"
    
    context ={
        'hammasi':hammasi,
        'h_ich':h_ich,
        'h_ist':h_ist,
        'h_uzat':h_uzat,
        'titleown':titleown,
        "full_ist":full_ist,
        'full_ich':full_ich
    }
    return render(request, '03_foydalanuvchi/00_0_home.html', context)

#____***_____ASosiy_settings_____***_____________________
def asosiyset(request, id):
    check=savolnoma.objects.filter(owner=request.user)
    
    mich=0
    uzat=0
    
    for v in check:
        if v.savol1==True:
            mich=1
        if v.savol2==True:
            uzat=1
    #Korxona ma'lumotlarini o'zgartirish
    
    h = allfaqir.objects.get(pk=id)
    
    context ={
        'active0':'active',
        'mich':mich,
        'uzat':uzat,
        'hammasi':h
    }
    if request.method=="GET":
        return render(request, '03_foydalanuvchi/01_0_asosiy_setting.html', context)
    if request.method=="POST":
        h.nomi=request.POST['nomi']
        h.about=request.POST['about']
        
        
        if not request.POST['emblem']:
            h.save()
        else:
            h.emblem=request.POST['emblem']
            h.save()
                
        
        
        return render(request, '03_foydalanuvchi/01_0_asosiy_setting.html', context)
        

#ishlab chiqarish bo'limi***********************
def mich(request):
    titleown = 'Energiya resurs/mahsulot ishlab chiqarish bo`yicha ma`lumotlar'
    resurs=resurslar.objects.all()
    ich = ichres.objects.filter(owner=request.user)
    
    check=savolnoma.objects.filter(owner=request.user)
    
    mich=0
    uzat=0
    
    for v in check:
        if v.savol1==True:
            mich=1
        if v.savol2==True:
            uzat=1
    
    hammasi = allfaqir.objects.get(pk=1)
    
    context={
        'titleown':titleown,
        'resurs':resurs,
        'ich':ich,
        'active1': 'active',
        'pageid':'1',
        'mich':mich,
        'uzat':uzat,
        'hammasi':hammasi
    }
    
    return render(request, '03_foydalanuvchi/01_setting.html', context)

#iste'mol qilish bo'limi***********************
def ist(request):
    titleown = 'Energiya resurs/mahsulot iste`mol qilish bo`yicha ma`lumotlar'
    resurs=resurslar.objects.all()
    ich = istres.objects.filter(owner=request.user)
    check=savolnoma.objects.filter(owner=request.user)
    
    mich=0
    uzat=0
    
    for v in check:
        if v.savol1==True:
            mich=1
        if v.savol2==True:
            uzat=1     
            
    hammasi = allfaqir.objects.get(pk=1)
    context={
        'titleown':titleown,
        'resurs':resurs,
        'ich':ich,
        'active2': 'active',
        'pageid':'2',
        'mich':mich,
        'uzat':uzat,
        'hammasi':hammasi
    }
    
    return render(request, '03_foydalanuvchi/01_setting.html', context)

def addist(request):
    nom = request.POST['nom']  
    resurs=resurslar.objects.all()
     
    for i in resurs:
        if nom==i.nomi:
            blik = i.birlik
            
    if istres.objects.filter(birlik = blik).first():
        messages.error(request, "Hurmatli foydalanuvchi ushbu resurs allaqachon qo'shilgan!")
        return redirect('mich')  
          
    istres.objects.create(owner=request.user, nom=nom, birlik=blik)
    
    messages.success(request, 'Siz yangi ishlab chiqarish resurs/mahsulotni muvofaqqiyatli qo`shdingiz! Rahmat! Charchamang! :)')
    return redirect('mich')  

#Sotish********************************************************************************
def sot(request):
    titleown = 'Energiya resurs/mahsulot sotish qilish bo`yicha ma`lumotlar'
    resurs=resurslar.objects.all()
    ich = sotres.objects.filter(owner=request.user)
    
    check=savolnoma.objects.filter(owner=request.user)
    
    mich=0
    uzat=0
    
    for v in check:
        if v.savol1==True:
            mich=1
        if v.savol2==True:
            uzat=1
   
    hammasi = allfaqir.objects.get(pk=1)
    context={
        'titleown':titleown,
        'resurs':resurs,
        'ich':ich,
        'active3': 'active',
        'pageid':'3',
        'mich':mich,
        'uzat':uzat,
        'hammasi' :hammasi
    }
    
    return render(request, '03_foydalanuvchi/01_setting.html', context)

def add(request):
    
    sahnom = request.POST['sahifanomi'] 
    resurs=resurslar.objects.all()  
    nom = request.POST['nom'] 
    for i in resurs:
            if nom==i.nomi:
                blik = i.birlik
                
    if sahnom=='1':  
        if ichres.objects.filter(nom = nom).first():
            messages.error(request, "Hurmatli foydalanuvchi ushbu resurs allaqachon qo'shilgan!")
            return redirect('mich')  
            
        ichres.objects.create(owner=request.user, nom=nom, birlik=blik)        
        
        messages.success(request, 'Siz yangi ishlab chiqarish resurs/mahsulotni muvofaqqiyatli qo`shdingiz! Rahmat! Charchamang! :)')
        return redirect('mich')
    
    if sahnom=='2':
        if istres.objects.filter(nom = nom).first():
            messages.error(request, "Hurmatli foydalanuvchi ushbu resurs allaqachon qo'shilgan!")
            return redirect('ist')  
          
        istres.objects.create(owner=request.user, nom=nom, birlik=blik)
        
        messages.success(request, 'Siz iste`mol resurs/mahsulotni muvofaqqiyatli qo`shdingiz! Rahmat! Charchamang! :)')
        return redirect('ist')
    
    if sahnom=='3':
        if sotres.objects.filter(nom = nom).first():
            messages.error(request, "Hurmatli foydalanuvchi ushbu resurs allaqachon qo'shilgan!")
            return redirect('sot')  
          
        sotres.objects.create(owner=request.user, nom=nom, birlik=blik)
        
        messages.success(request, 'Siz sotish bo`limi chiqarish resurs/mahsulotni muvofaqqiyatli qo`shdingiz! Rahmat! Charchamang! :)')
        return redirect('sot')
    
#*****************************Ma'lumotlarni kiritish*********************

def davr(request):
    titleown = 'Davriy ma`lumotlarni yuborish'
    his = hisobot_item.objects.filter(owner=request.user)
    ist = istres.objects.filter(owner=request.user)    

    context={
        'titleown':titleown,        
        'values':ist,
        'his':his
    }
    return render(request, '03_foydalanuvchi/02_0_davr.html', context)

def adddavr(request):
    ich = ichres.objects.filter(owner=request.user)
    ist = istres.objects.filter(owner=request.user)
    sot = sotres.objects.filter(owner=request.user)
    
    vaqt=timezone.now()
    sana = vaqt.strftime("%d-%m-%Y")
    yil = vaqt.strftime("%Y")
    
    m =vaqt.strftime("%m")
    oylar = ['YANVAR', 'FEVRAL', 'MART', 'APREL', 'MAY', 'IYUN', 'IYUL', 'AVGUST','SENTYABR', 'OKTYABR', 'NOYABR', 'DEKABR']
        
    title = str(oylar[int(m)-2])+'-'+yil
    titleown = title+' OYI UCHUN HISOBOT'    
    
    context={
            'titleown':titleown,        
            'ich':ich,
            'ist':ist,
            'sot':sot,
            'sana':sana
        }
    
    if request.method=="GET":
        return render(request, '03_foydalanuvchi/02_1_adddavr.html', context)
    
    if request.method=="POST":
        if hisobot_item.objects.filter(title = title).first():
            messages.success(request, 'Siz allaqachon uchbu davr uchun hisobot yuborgansiz, agar xatoliklar yuzasidan murojaatingiz bo`lsa murojaat bo`limidan murojaat qilishingiz mumkin! Rahmat! Charchamang! :)')            
            return redirect('davr')
          
        for v in ich:                        
            qiymat=request.POST[str(v.nom)+'1']
            qiymat_pul=request.POST[str(v.nom+'pul1')]
            hisobot_ich.objects.create(owner=request.user, 
                                    title=title,
                                    vaqt=vaqt,
                                    nom=v.nom,
                                    birlik=v.birlik,
                                    qiymat=qiymat,
                                    qiymat_pul=qiymat_pul)
        for v in ist:                        
            qiymat=request.POST[str(v.nom)+'2']
            qiymat_pul=request.POST[str(v.nom+'pul2')]
            hisobot_ist.objects.create(owner=request.user, 
                                    title=title,
                                    vaqt=vaqt,
                                    nom=v.nom,
                                    birlik=v.birlik,
                                    qiymat=qiymat,
                                    qiymat_pul=qiymat_pul)
        for v in sot:                        
            qiymat=request.POST[str(v.nom)+'3']
            qiymat_pul=request.POST[str(v.nom+'pul3')]
            hisobot_uzat.objects.create(owner=request.user, 
                                    title=title,
                                    vaqt=vaqt,
                                    nom=v.nom,
                                    birlik=v.birlik,
                                    qiymat=qiymat,
                                    qiymat_pul=qiymat_pul)
        
        hisobot_item.objects.create(owner=request.user, 
                                    title=title,
                                    vaqt=vaqt,
                                    )   
            
        messages.success(request, 'Hisobot muvofaqqiyatli yuborildi! Rahmat! Charchamang! :)')
        return redirect('davr')

def checkdavr(request, id):
    h_item=hisobot_item.objects.get(pk=id)
    
    h_ich=hisobot_ich.objects.filter(owner=request.user, title=h_item.title)
    h_ist=hisobot_ist.objects.filter(owner=request.user, title=h_item.title)
    h_uzat=hisobot_uzat.objects.filter(owner=request.user, title=h_item.title)
    
    titleown=h_item.title+' oyi uchun ma`lumotlarni tekshirish'
    
    context ={
        'h_item':h_item,
        'h_ich':h_ich,
        'h_ist':h_ist,
        'h_uzat':h_uzat,
        'titleown':titleown,
        'val':h_item        
    }
    
    if request.method=="GET":
        return render(request, '03_foydalanuvchi/02_2_checkdavr.html', context)
    
def hisobot(request):
    titleown = 'Davriy hisobotlar'
    
    his = hisobot_full.objects.filter(owner=request.user)  
        
    ist = istres.objects.filter(owner=request.user)    
    
    context={
        'titleown':titleown,        
        'values':ist,
        'his':his
    }
    
    return render(request, '03_foydalanuvchi/03_0_hisobot.html', context)

def addhisobot(request):
    titleown = 'Davriy hisobotlarni shakllantirish'
    ich_res = ichres.objects.filter(owner=request.user)
    ist = istres.objects.filter(owner=request.user)    
    
    his_oraliq = hisobot_full.objects.filter(owner=request.user)  
    his_res = his_ich.objects.filter(owner=request.user)
    
    vaqt=timezone.now()
    sana = vaqt.strftime("%d-%m-%Y")
    
    m =vaqt.strftime("%m")
    oylar = ['YANVAR', 'FEVRAL', 'MART', 'APREL', 'MAY', 'IYUN', 'IYUL', 'AVGUST','SENTYABR', 'OKTYABR', 'NOYABR', 'DEKABR']
    
    
    context={
        'titleown':titleown,        
        'values':ist,
        'his_res':his_res,
        'ich_res':ich_res,
        'oylar':oylar
    }
    if request.method=="GET":
        return render(request, '03_foydalanuvchi/03_1_addhisobot.html', context)

    if request.method=="POST":
        oraliq=request.POST['oraliq']
        
        if not oraliq:
            messages.error(request, 'Iltimos oraliqni kiriting?! ')           
            return redirect('addhisobot')
        
        oraliq=oraliq.split(" <<>> ")
            
        oraliq_min=oraliq[0]
        if len(oraliq)==1:
            oraliq_max=oraliq_min
        else:
            oraliq_max=oraliq[1]
        
        vaqt=timezone.now()
        sana = vaqt.strftime("%d-%m-%Y")
        yil = vaqt.strftime("%Y")
        
        nomi=sana+' hisoboti'
        
        if hisobot_full.objects.filter(nomi = nomi).first():
            messages.error(request, "Hurmatli foydalanuvchi ushbu bugungi hisobot allaqachon tayyorlangan. Kunida bitta hisobot tayyorlash mumkin!")
            return redirect('hisobot') 
        
        resurs=[]
        for v in his_res:
            resurs.append(v.resurs)
        
        hisobot_full.objects.create(
           owner=request.user,
           nomi=nomi,
           oraliq_min=oraliq_min,
           oraliq_max=oraliq_max,
           resurs=resurs,
           vaqt=vaqt            
        )
        messages.success(request, 'Hisobot muvofaqqiyatli tayyorlandi! ')
        return redirect('hisobot')
        
def addichresforhis(request):
    if request.method=="POST":
        
        vaqt=timezone.now()
        sana = vaqt.strftime("%d-%m-%Y")
        yil=vaqt.strftime("%Y")
        nomi=sana+' hisoboti'
        resurs=request.POST['resurs_id']
        
        if his_ich.objects.filter(resurs = resurs).first():
            messages.error(request, "Hurmatli foydalanuvchi ushbu resurs allaqachon qo'shilgan!")
            return redirect('addhisobot')
    
        his_ich.objects.create(
            nomi=nomi,
            owner=request.user,
            resurs=resurs        
        )
        messages.success(request, 'Resurs muvofaqqiyatli qo`shildi')
        return redirect('addhisobot')

def delhis(request, id):
    davlat = his_ich.objects.get(pk=id)
    davlat.delete()
    messages.success(request, 'Resurs muvofaqqiyatli o`chirildi')
    return redirect('addhisobot')

##########################################################################
def result_his(request):    
    h_filter=hisobot_full.objects.get(pk=4)
    
    oraliq_min=h_filter.oraliq_min
    oraliq_max=h_filter.oraliq_max
    
    h_baza=hisobot_ich.objects.filter(owner=request.user, vaqt__range=[oraliq_min,oraliq_max])
    
    context={
        'h_baza':h_baza,        
    }
    return render(request, '03_foydalanuvchi/03_1_result.html',context)