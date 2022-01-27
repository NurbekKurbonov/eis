from django.shortcuts import render, redirect


from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
import datetime

#modelsdan chaqirish******************
from s_ad.models import resurslar, Valyuta
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
        
        for h in hisobot_item.objects.filter(owner=request.user, title=title):
            h_id=h.id
        his=hisobot_item.objects.get(pk=h_id)
            
        for i in hisobot_ich.objects.filter(owner=request.user, title=title):
            his.ich.add(i.id) 
        for i in hisobot_ist.objects.filter(owner=request.user, title=title):
            his.ist.add(i.id)    
        for i in hisobot_uzat.objects.filter(owner=request.user, title=title):
            his.uzat.add(i.id) 
            
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
    
    valyuta=Valyuta.objects.all()
    
    vaqt=timezone.now()
    sana = vaqt.strftime("%d-%m-%Y")
    
    m =vaqt.strftime("%m")
    oylar = ['YANVAR', 'FEVRAL', 'MART', 'APREL', 'MAY', 'IYUN', 'IYUL', 'AVGUST','SENTYABR', 'OKTYABR', 'NOYABR', 'DEKABR']
    
    mich=ichres.objects.filter(owner=request.user)
    sot=sotres.objects.filter(owner=request.user)
    
    context={
        'titleown':titleown,        
        'values':ist,
        'his_res':his_res,
        'ich_res':ich_res,
        'oylar':oylar,
        'valyuta':valyuta,
        'mich':mich,
        'sot':sot
    }
    if request.method=="GET":
        return render(request, '03_foydalanuvchi/03_1_addhisobot.html', context)

    if request.method=="POST":
        oraliq=request.POST['oraliq']
        valute=request.POST['valute']
        
        if not oraliq:
            messages.error(request, 'Iltimos oraliqni kiriting?! ')           
            return redirect('addhisobot')
        
        oraliq=oraliq.split(" <<>> ")
            
        oraliq_min=oraliq[0]
        if len(oraliq)==1:
            oraliq_max=oraliq_min
        else:
            oraliq_max=oraliq[1]
        
        his=hisobot_ich.objects.filter(owner=request.user)
        
        if not hisobot_ich.objects.filter(owner=request.user, vaqt__range=[str(oraliq_min), str(oraliq_max)]):
            messages.error(request, "Ushbu oraliqda ma'lumotlar mavjud emas, boshqa oraliq tanlang!")
            return redirect('addhisobot') 
        
        vaqt=timezone.now()
        sana = vaqt.strftime("%d-%m-%Y")
        yil = vaqt.strftime("%Y")
        
        nomi=sana+' hisoboti'
        
        if hisobot_full.objects.filter(nomi = nomi).first():
            messages.error(request, "Siz bugungi so'rov limitini bajargansiz, keyinroq urinib ko'ring!")
            return redirect('hisobot') 
        
        #diagramma va qo'shimcha birliklarni qo'shish
        
        cheks = request.POST.getlist('chart')
        tur = request.POST.getlist('his_tur')
        
        if len(tur)==1 and tur[0]=='':
            messages.success(request, 'Hisobot muvofaqqiyatli tayyorlandi! ')
            return redirect('hisobot')
        
        hisobot_full.objects.create(
           owner=request.user,
           nomi=nomi,
           oraliq_min=oraliq_min,
           oraliq_max=oraliq_max,           
           vaqt=vaqt,
           cheks=cheks,
           valyuta=Valyuta(valute),
           tur=tur
           
        )
        
        for h in hisobot_full.objects.filter(owner=request.user, nomi=nomi):
            h_id=h.id
        his=hisobot_full.objects.get(pk=h_id)
                        
        for i in hisobot_item.objects.filter(owner=request.user, vaqt__range=[str(his.oraliq_min), str(his.oraliq_max)]):
            his.hisobotlar.add(i.id)
        
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

def result_his(request,id,qiy_bir,tur_hisob):   
     
    his=hisobot_full.objects.get(pk=id)
    hisobotlar=his.hisobotlar.all()
    valyuta=his.valyuta 
    if tur_hisob=='mich':
        pass
    if qiy_bir=='nomli' or qiy_bir=='tshy' or qiy_bir=='tne' or qiy_bir=='gj' or qiy_bir=='gkal':
        
        res=[]
        resb=[]
        for v in hisobotlar:
            if tur_hisob=='A':
                resurs=v.ich.all()
            if tur_hisob=='B':
                resurs=v.ist.all()
            if tur_hisob=='C':
                resurs=v.uzat.all()
                
            for i in resurs:
                qb=i.nom+' ( '+i.birlik+' )'
                res.append(i.nom)
                resb.append(qb)
        res=set(res)
        resb=list(set(resb))
        
        #for linegraph
        obj = {}
        count=0    
        for i in res:
            key=resb[count]
            
            obj[key]=[]
            
            count+=1
            for v in hisobotlar:        
                lst=[]
                if tur_hisob=='A':
                    resurs=v.ich.all()
                if tur_hisob=='B':
                    resurs=v.ist.all()
                if tur_hisob=='C':
                    resurs=v.uzat.all()
                
                for k in resurs:
                    lst.append(k.nom)            
                if i in lst:   
                    for j in resurs:                            
                        if i in j.nom:
                            if i==j.nom:
                                koef=1
                                if qiy_bir=='tne':                                    
                                    for blik in resurslar.objects.all():
                                        if j.nom==blik.nomi:
                                            koef=blik.tne
                                if qiy_bir=='gj':
                                    for blik in resurslar.objects.all():
                                        if j.nom==blik.nomi:
                                            koef=blik.tne                                
                                if qiy_bir=='gkal':                                    
                                    for blik in resurslar.objects.all():
                                        if j.nom==blik.nomi:
                                            koef=blik.tne
                                obj[key].append(j.qiymat/koef)
                else:
                    obj[i].append(0)
                
        #table
        obj_table = {}    
        
        for v in hisobotlar:        
            lst=[]
            if tur_hisob=='A':
                resurs=v.ich.all()
            if tur_hisob=='B':
                resurs=v.ist.all()
            if tur_hisob=='C':
                resurs=v.uzat.all()            
                    
            sana = v.vaqt.strftime("%d-%m-%Y")
            obj_table[sana]=[]
            for i in res:
                for k in resurs:
                    lst.append(k.nom)            
                if i in lst:   
                    for j in resurs:                            
                        if i in j.nom:
                            if i==j.nom:
                                    obj_table[sana].append(j.qiymat/koef)                               
                else:
                    obj_table[sana].append(0)                  
        
    # mlm so'mda qiymatni chiqarish
           
            
    titleown=his.nomi +' // '+his.oraliq_min+' dan '+his.oraliq_max+' gacha'
    
    if qiy_bir=='som' or qiy_bir=='dollar':
        
        if qiy_bir=='som':
            koef=1
        if qiy_bir=="dollar":
            koef=valyuta.somda/(valyuta.qiymati*1000)
            
        res=[]        
        for v in hisobotlar:
            if tur_hisob=='A':
                resurs=v.ich.all()
            if tur_hisob=='B':
                resurs=v.ist.all()
            if tur_hisob=='C':
                resurs=v.uzat.all()
            for i in resurs:                
                res.append(i.nom)                
        res=set(res)       
        
        #for linegraph
        obj = {}
        count=0    
        for i in res:                     
            obj[i]=[]
            
            for v in hisobotlar:        
                lst=[]
                if tur_hisob=='A':
                    resurs=v.ich.all()
                if tur_hisob=='B':
                    resurs=v.ist.all()
                if tur_hisob=='C':
                    resurs=v.uzat.all()                               
                for k in resurs:
                    lst.append(k.nom)
                if i in lst:   
                    for j in resurs:                            
                        if i in j.nom:
                            if i==j.nom:
                                    obj[i].append(j.qiymat_pul/koef)
                else:
                    obj[i].append(0)
                
        #table
        obj_table = {}    
        
        for v in hisobotlar:        
            lst=[]
            if tur_hisob=='A':
                resurs=v.ich.all()
            if tur_hisob=='B':
                resurs=v.ist.all()
            if tur_hisob=='C':
                resurs=v.uzat.all()
                                  
            sana = v.vaqt.strftime("%d-%m-%Y")
            obj_table[sana]=[]
            for i in res:
                for k in resurs:
                    lst.append(k.nom)            
                if i in lst:   
                    for j in resurs:                            
                        if i in j.nom:
                            if i==j.nom:
                                    obj_table[sana].append(j.qiymat_pul/koef)                               
                else:
                    obj_table[sana].append(0)
    if tur_hisob=='A':
        active1='active'
        active2=''
        active3=''
    if tur_hisob=='B':
        active1=''
        active2='active'
        active3=''
    if tur_hisob=='C':
        active1=''
        active2=''
        active3='active'
   
    valyut_nom=valyuta.name     
    context={
        'his':his,
        'res':res,
        'hisobotlar':hisobotlar ,
        'obj':obj,
        'titleown':titleown,
        'obj_table': obj_table,
        'qiy_bir':qiy_bir,
        'valyuta':valyuta,
        'valyut_nom':valyut_nom,
        'tur_hisob':tur_hisob,
        'active1':active1,
        'active2':active2,
        'active3':active3,
    }
    return render(request, '03_foydalanuvchi/03_1_result.html', context)
    