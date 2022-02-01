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
    
    h_item=hisobot_item.objects.filter(owner=request.user)
    ich=hisobot_ich.objects.filter(owner=request.user)
    ist=hisobot_uzat.objects.filter(owner=request.user)
    sot=hisobot_uzat.objects.filter(owner=request.user)
    
    sanalar=[]
    obj_ich={}
    obj_ist={}
    obj_uzat={}
    for v in h_item:
        sana = v.vaqt.strftime("%m-%Y")
        sanalar.append(sana)
        x=0
        obj_ich[sana]=[]
        obj_ist[sana]=[]
        obj_uzat[sana]=[]
        
        for i in ich.filter(vaqt=v.vaqt):
            x+=i.qiymat_pul
        obj_ich[sana].append(x)
        x=0
        for i in ist.filter(vaqt=v.vaqt):
            x+=i.qiymat_pul
        obj_ist[sana].append(x)
        x=0
        
        for i in sot.filter(vaqt=v.vaqt):
            x+=i.qiymat_pul
        obj_uzat[sana].append(x)
       
    titleown="Bosh menyu"
    
    context ={
        'hammasi':hammasi,
        'h_item':h_item,
        'ich':ich,
        'ist':ist,
        'sot':sot,
        'sanalar':sanalar,
        
        'titleown':titleown,        
        'obj_ich':obj_ich,
        'obj_ist':obj_uzat,
        'obj_uzat':obj_uzat,
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
    res_id = request.POST['nom'] 
 
    if sahnom=='1':  
        if ichres.objects.filter(owner=request.user, resurs=resurslar(res_id)).first():
            messages.error(request, "Hurmatli foydalanuvchi ushbu resurs allaqachon qo'shilgan!")
            return redirect('mich')  
            
        ichres.objects.create(owner=request.user, resurs=resurslar(res_id))        
        
        messages.success(request, 'Siz yangi ishlab chiqarish resurs/mahsulotni muvafaqqiyatli qo`shdingiz! Rahmat! Charchamang! :)')
        return redirect('mich')
    
    if sahnom=='2':
        if istres.objects.filter(owner=request.user, resurs=resurslar(res_id)).first():
            messages.error(request, "Hurmatli foydalanuvchi ushbu resurs allaqachon qo'shilgan!")
            return redirect('ist')  
          
        istres.objects.create(owner=request.user, resurs=resurslar(res_id))
        
        messages.success(request, 'Siz iste`mol resurs/mahsulotni muvafaqqiyatli qo`shdingiz! Rahmat! Charchamang! :)')
        return redirect('ist')
    
    if sahnom=='3':
        if sotres.objects.filter(owner=request.user, resurs=resurslar(res_id)).first():
            messages.error(request, "Hurmatli foydalanuvchi ushbu resurs allaqachon qo'shilgan!")
            return redirect('sot')  
          
        sotres.objects.create(owner=request.user, resurs=resurslar(res_id))
        
        messages.success(request, 'Siz sotish bo`limi chiqarish resurs/mahsulotni muvafaqqiyatli qo`shdingiz! Rahmat! Charchamang! :)')
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
    
    yil=[]
    for i in range(2010,2021):
        yil.append(i)
        
    context={
            'titleown':titleown,        
            'ich':ich,
            'ist':ist,
            'sot':sot,
            'sana':sana,
            'oylar':oylar,
            'yil':yil
        }
    
    if request.method=="GET":
        return render(request, '03_foydalanuvchi/02_1_adddavr.html', context)
    
    if request.method=="POST":
        #************tarix***************
        tarix=request.POST.get('c1')
        
        yil_post=request.POST['yil']
        oy_post=request.POST['oy']
        if tarix=="True":
            for i in range(len(oylar)):
                if oy_post==oylar[i]:
                    k=i+1                
            vaqt=datetime.datetime(int(yil_post), int(k), 15)
            title=oy_post+'-'+yil_post
        #*******************************************
        if hisobot_item.objects.filter(owner=request.user, title = title).first():
            messages.error(request, 'Siz allaqachon uchbu davr uchun hisobot yuborgansiz, agar xatoliklar yuzasidan murojaatingiz bo`lsa murojaat bo`limidan murojaat qilishingiz mumkin! Rahmat! Charchamang! :)')            
            return redirect('davr')
          
        for v in ich:                        
            qiymat=request.POST[(str(v.resurs.id)+'.1')]
            qiymat_pul=request.POST[str(v.resurs.id)+'.pul1']
            hisobot_ich.objects.create(owner=request.user, 
                                    title=title,
                                    vaqt=vaqt,
                                    resurs=ichres(v.id),
                                    qiymat=qiymat,
                                    qiymat_pul=qiymat_pul)
        for v in ist:                        
            qiymat=request.POST[str(v.resurs.id)+'.2']
            qiymat_pul=request.POST[str(v.resurs.id)+'.pul2']
            hisobot_ist.objects.create(owner=request.user, 
                                    title=title,
                                    vaqt=vaqt,
                                    resurs=istres(v.id),
                                    qiymat=qiymat,
                                    qiymat_pul=qiymat_pul)
        for v in sot:                        
            qiymat=request.POST[str(v.resurs.id)+'.3']
            qiymat_pul=request.POST[str(v.resurs.id)+'.pul3']
            hisobot_uzat.objects.create(owner=request.user, 
                                    title=title,
                                    vaqt=vaqt,
                                    resurs=sotres(v.id),
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
            
        messages.success(request, 'Hisobot muvafaqqiyatli yuborildi! Rahmat! Charchamang! :)')
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
    #***Resurslarni ko'rsatish
    res_for_add_show=[]
    for r in ichres.objects.filter(owner=request.user):
        res_for_add_show.append(r.resurs.id)
    for r in istres.objects.filter(owner=request.user):
        res_for_add_show.append(r.resurs.id)
    for r in sotres.objects.filter(owner=request.user):
        res_for_add_show.append(r.resurs.id)
    
    res_for_add_show=list(set(res_for_add_show))
    res_show={}
    for i in res_for_add_show:
        res_show[i]=resurslar.objects.get(pk=i).nomi+' ( '+resurslar.objects.get(pk=i).birlik+' )'
    #**************************************************************************************************
    
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
        'oylar':oylar,
        'valyuta':valyuta,
        'mich':mich,
        'sot':sot,
        'res_show':res_show
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
        
        nomi='Hisobot: '+sana
        
        if hisobot_full.objects.filter(owner=request.user, nomi = nomi).first():
            messages.error(request, "Siz bugungi so'rov limitini bajargansiz, keyinroq urinib ko'ring!")
            return redirect('hisobot') 
        
        #diagramma va qo'shimcha birliklarni qo'shish
        
        cheks = request.POST.getlist('chart')
        tur = request.POST.getlist('his_tur')
        
        if len(tur)==1 and tur[0]=='':
            messages.success(request, 'Hisobot muvafaqqiyatli tayyorlandi! ')
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
        
        #hisobot shakllantirish uchun resurslarni qo'shish:
        for i in his_res:
            his.resurs.add(i.resurs.id)
        
        #oraliqqa ko'ra davriy hisobotlar qo'shish:             
        for v in hisobot_item.objects.filter(owner=request.user, vaqt__range=[str(his.oraliq_min), str(his.oraliq_max)]):            
            his.h_item.add(v.id)
            for r in v.ich.all():                
                for i in his_res:
                    if r.resurs.resurs.id==i.resurs.id:
                        his.ich.add(r.id)
            for r in v.ist.all():                
                for i in his_res:
                    if r.resurs.resurs.id==i.resurs.id:
                        his.ist.add(r.id)
            for r in v.uzat.all():                
                for i in his_res:
                    if r.resurs.resurs.id==i.resurs.id:
                        his.sot.add(r.id)
        
        messages.success(request, 'Hisobot muvafaqqiyatli tayyorlandi! ')
        return redirect('hisobot')
        
def addichresforhis(request):
    if request.method=="POST":        
        resurs=request.POST['resurs_id']
        
        if his_ich.objects.filter(owner=request.user, resurs = resurs).first():
            messages.error(request, "Hurmatli foydalanuvchi ushbu resurs allaqachon qo'shilgan!")
            return redirect('addhisobot')
        #resurs id ni aniqlash        
        his_ich.objects.create(
            owner=request.user,
            resurs=resurslar(pk=resurs)
        )
        messages.success(request, 'Resurs muvafaqqiyatli qo`shildi')
        return redirect('addhisobot')

def delhis(request, id):
    davlat = his_ich.objects.get(pk=id)
    davlat.delete()
    messages.success(request, 'Resurs muvafaqqiyatli o`chirildi')
    return redirect('addhisobot')

##########################################################################

def result_his(request, id, tur, birl):   
     
    his=hisobot_full.objects.get(pk=id) 
       
    valyuta=his.valyuta
    
    active1=''
    active2=''
    active3=''
    
    if tur=="A":
        active1='active'
        res=his.ich.all()
    
    if tur=="B":
        active2='active'
        res=his.ist.all()
        
    if tur=="C":
        active3='active'
        res=his.sot.all()
        
    
    
    # Nomli Birliklarda
    sana=[]
    resurs=[]
    res_id=[]
    for i in res:
        s = i.vaqt.strftime("%Y-%m")
        sana.append(s) 
               
        res_id.append(i.resurs.resurs.id)
        
        r=i.resurs.resurs.nomi
        resurs.append(r)
    
    sana=set(sana)
    sana=sorted(sana)
    resurs=set(resurs)
    res_id=set(res_id)
    
    obj={}
    for i in res_id: 
        if birl=="nomli":
            b=' ('+resurslar.objects.get(pk=i).birlik+' )'               
        if birl=="tshy":
            b=' ( tshy )'
        if birl=="tne":
            b=' ( tne )'
        if birl=="gj":
            b=' ( GJ )'
        if birl=="gkal":
            b=' ( GKal )'
        if birl=="som":
            b=' ( mln.so`m )'
        if birl=="valut":
            b=' ( ming.'+his.valyuta.name+' )'
        r=resurslar.objects.get(pk=i).nomi+b
        obj[r]=[]
        
        lst=[]
        for j in res.filter(resurs__resurs__id=i):
            s = j.vaqt.strftime("%Y-%m")
            lst.append(s)            
        
        for k in sana:
            if k in lst:
                for j in res.filter(resurs__resurs__id=i):
                    s = j.vaqt.strftime("%Y-%m")            
                    if k==s:
                        if birl=='nomli' or birl=='tshy' or birl=='tne' or birl=='gj' or birl=='gkal':
                            def birlik(i):
                                switcher={
                                    'nomli':1,
                                    'tshy':j.resurs.resurs.tshy,
                                    'tne':j.resurs.resurs.tne,
                                    'gj':j.resurs.resurs.gj,
                                    'gkal':j.resurs.resurs.gkal,                                    
                                }
                                return switcher.get(i, "xato")    
                            
                            koef1=birlik(birl)           
                            q=j.qiymat*koef1
                        if birl=='som' or birl=='valut':
                            if birl == 'som':
                                koef2=1
                            if birl == 'valut':
                                koef2=1000*his.valyuta.qiymati/his.valyuta.somda
                            q=j.qiymat_pul*koef2
                        
                        obj[r].append(q)
                        
            else:
                obj[r].append(0)
        
    context={
        'titleown':his.nomi,
       'his':his,
       'obj':obj,
       'sana':sana,
       'res_id':res_id,
       'birl':birl,
       'tur1':tur,
       
       'active1':active1,
       'active2':active2,
       'active3':active3,
    }   
    return render(request, '03_foydalanuvchi/03_1_result.html', context)
    