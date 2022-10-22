from calendar import month
import re
from django.shortcuts import render, redirect
import random

from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
#modelsdan chaqirish******************
from s_ad.models import resurslar, Valyuta, Tadbir, birliklar,yaxlitlash
from .models import ichres, istres, sotres, hisobot_item, hisobot_ich, hisobot_ist, hisobot_uzat, allfaqir, hisobot_full, his_ich, TexnikTadbir,VVP
from .models import plan_umumiy, plan_uzat, plan_ist, plan_ich, TTT_reja, TTT_umumiy_reja
from kirish.models import savolnoma
import six
from django.core.exceptions import PermissionDenied
from dateutil.relativedelta import relativedelta
from django.http import HttpResponseRedirect, JsonResponse

def group_required(group, login_url=None, raise_exception=False):
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups = (group, )
        else:
            groups = group

        if user.groups.filter(name__in=groups).exists():
            return True
        if raise_exception:
            raise PermissionDenied
        return False
    return user_passes_test(check_perms, login_url='/login')

def application_req( login_url=None, raise_exception=False):
    def check_perms(user):        
        allf=allfaqir.objects.get(owner=user)        
        if allf.nomi!="":
            return True
        if raise_exception:
            raise PermissionDenied
        return False
    return user_passes_test(check_perms, login_url='/savolnoma')

#____***_____Bosh sahifa_____***_____________________
@group_required('Faqirlar')
@application_req()
def home(request):    
    hammasi = allfaqir.objects.filter(owner=request.user)    
    vaqt=timezone.now()
    
    h_item=hisobot_item.objects.filter(owner=request.user)
    ich=hisobot_ich.objects.filter(owner=request.user)
    ist=hisobot_ist.objects.filter(owner=request.user)
    sot=hisobot_uzat.objects.filter(owner=request.user)
    
    sanalar=[]
    obj_ich={}
    obj_ist={}
    obj_uzat={}
    for v in h_item:
        sana = v.vaqt.strftime("01/%m/%Y")
        sanalar.append(sana)
        x=0
        
        for i in ich.filter(vaqt=v.vaqt):
            x+=i.qiymat_pul
        obj_ich[sana]=x
        x=0
        for i in ist.filter(vaqt=v.vaqt):
            x+=i.qiymat_pul
        obj_ist[sana]=x
        x=0
        
        for i in sot.filter(vaqt=v.vaqt):
            x+=i.qiymat_pul
        obj_uzat[sana]=x
       
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
        'value':request.user
    }
    return render(request, '03_foydalanuvchi/00_0_home.html', context)

#____***_____ASosiy_settings_____***_____________________
@group_required('Faqirlar')
@application_req()
def asosiyset(request):
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
@group_required('Faqirlar')
@application_req()
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
    
    #hammasi = allfaqir.objects.all()
    
    context={
        'titleown':titleown,
        'resurs':resurs,
        'ich':ich,
        'active1': 'active',
        'pageid':'1',
        'mich':mich,
        'uzat':uzat
    }
    
    return render(request, '03_foydalanuvchi/01_setting.html', context)

#iste'mol qilish bo'limi***********************
@group_required('Faqirlar')
@application_req()
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
            
    hammasi = allfaqir.objects.all()
    context={
        'titleown':titleown,
        'resurs':resurs,
        'ich':ich,
        'active2': 'active',
        'pageid':'2',
        'mich':mich,
        'uzat':uzat,
    }
    
    return render(request, '03_foydalanuvchi/01_setting.html', context)
#Sotish********************************************************************************
@group_required('Faqirlar')
@application_req()
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
   
    #hammasi = allfaqir.objects.get(pk=1)
    context={
        'titleown':titleown,
        'resurs':resurs,
        'ich':ich,
        'active3': 'active',
        'pageid':'3',
        'mich':mich,
        'uzat':uzat
    }
    
    return render(request, '03_foydalanuvchi/01_setting.html', context)
@group_required('Faqirlar')
@application_req()
def add(request):
    
    sahnom = request.POST['sahifanomi'] 
    
    resurs=resurslar.objects.all()  
    res_id = request.POST['nom'] 
 
    if sahnom=='1':  
        if ichres.objects.filter(owner=request.user, resurs=resurslar(res_id)).first():
            messages.error(request, "Hurmatli foydalanuvchi ushbu resurs allaqachon qo'shilgan!")
            return redirect('mich')  
            
        ichres.objects.create(owner=request.user, resurs=resurslar(res_id))        
        
        messages.success(request, 'Siz yangi ishlab chiqarish resurs/mahsulotni muvafaqqiyatli qo`shdingiz! ')
        return redirect('mich')
    
    if sahnom=='2':
        if istres.objects.filter(owner=request.user, resurs=resurslar(res_id)).first():
            messages.error(request, "Hurmatli foydalanuvchi ushbu resurs allaqachon qo'shilgan!")
            return redirect('ist')  
          
        istres.objects.create(owner=request.user, resurs=resurslar(res_id))
        
        messages.success(request, 'Siz iste`mol resurs/mahsulotni muvafaqqiyatli qo`shdingiz! ')
        return redirect('ist')
    
    if sahnom=='3':
        if sotres.objects.filter(owner=request.user, resurs=resurslar(res_id)).first():
            messages.error(request, "Hurmatli foydalanuvchi ushbu resurs allaqachon qo'shilgan!")
            return redirect('sot')
          
        sotres.objects.create(owner=request.user, resurs=resurslar(res_id))
        
        messages.success(request, 'Siz sotish bo`limi chiqarish resurs/mahsulotni muvafaqqiyatli qo`shdingiz! ')
        return redirect('sot')
    
#*****************************Ma'lumotlarni kiritish*********************
#*****************************Reja**************************************
@group_required('Faqirlar')
@application_req()
def reja(request):
    titleown = 'Shartnomaviy miqdorlar'
    his = plan_umumiy.objects.filter(owner=request.user)
    ist = istres.objects.filter(owner=request.user)    

    context={
        'titleown':titleown,
        'values':ist,
        'his':his
    }
    return render(request, '03_foydalanuvchi/reja/0_reja.html', context)

@group_required('Faqirlar')
@application_req()
def addreja(request):
    ich = ichres.objects.filter(owner=request.user)
    ist = istres.objects.filter(owner=request.user)
    sot = sotres.objects.filter(owner=request.user)
    
    vaqt=timezone.now()
    sana = vaqt.strftime("%d-%m-%Y")
    yil = vaqt.strftime("%Y")
    
    m =vaqt.strftime("%m")
    oylar = ['YANVAR', 'FEVRAL', 'MART', 'APREL', 'MAY', 'IYUN', 'IYUL', 'AVGUST','SENTYABR', 'OKTYABR', 'NOYABR', 'DEKABR']
        
    title = str(oylar[int(m)])+'-'+yil
    titleown = title+' OYI UCHUN UCHUN SHARTNOMAVIY MIQDORLAR'    
    
    boshi=int(yil)-12
    oxiri=int(yil)+10

    yil=[]
    for i in range(boshi, oxiri):
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
        return render(request, '03_foydalanuvchi/reja/1_addreja.html', context)
    
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
        if plan_umumiy.objects.filter(owner=request.user, title = title).first():
            messages.error(request, 'Sizda allaqachon uchbu davr uchun rejalashtirilgan shartnomaviy qiymatlar mavjud!')            
            return redirect('reja')
          
        for v in ich:                        
            qiymat=request.POST[(str(v.resurs.id)+'.1')]
            qiymat_pul=request.POST[str(v.resurs.id)+'.pul1']
            plan_ich.objects.create(owner=request.user, 
                                    title=title,
                                    vaqt=vaqt,
                                    resurs=ichres(v.id),
                                    qiymat=qiymat,
                                    qiymat_pul=qiymat_pul)
        for v in ist:                        
            qiymat=request.POST[str(v.resurs.id)+'.2']
            qiymat_pul=request.POST[str(v.resurs.id)+'.pul2']
            plan_ist.objects.create(owner=request.user, 
                                    title=title,
                                    vaqt=vaqt,
                                    resurs=istres(v.id),
                                    qiymat=qiymat,
                                    qiymat_pul=qiymat_pul)
        for v in sot:                        
            qiymat=request.POST[str(v.resurs.id)+'.3']
            qiymat_pul=request.POST[str(v.resurs.id)+'.pul3']
            plan_uzat.objects.create(owner=request.user, 
                                    title=title,
                                    vaqt=vaqt,
                                    resurs=sotres(v.id),
                                    qiymat=qiymat,
                                    qiymat_pul=qiymat_pul)
        
        plan_umumiy.objects.create(owner=request.user, 
                                    title=title,
                                    vaqt=vaqt,
                                    )   
        
        for h in plan_umumiy.objects.filter(owner=request.user, title=title):
            h_id=h.id
        his=plan_umumiy.objects.get(pk=h_id)
            
        for i in plan_ich.objects.filter(owner=request.user, title=title):
            his.ich.add(i.id) 
        for i in plan_ist.objects.filter(owner=request.user, title=title):
            his.ist.add(i.id)    
        for i in plan_uzat.objects.filter(owner=request.user, title=title):
            his.uzat.add(i.id) 
            
        messages.success(request, 'Bazaga muvafaqqiyatli qo`shildi!')
        return redirect('reja')

@group_required('Faqirlar')
@application_req()
def checkreja(request, id):
    ich = ichres.objects.filter(owner=request.user)
    ist = istres.objects.filter(owner=request.user)
    sot = sotres.objects.filter(owner=request.user)
    
    h_item=plan_umumiy.objects.get(pk=id)
    
    h_ich=plan_ich.objects.filter(owner=request.user, title=h_item.title)
    h_ist=plan_ist.objects.filter(owner=request.user, title=h_item.title)
    h_uzat=plan_uzat.objects.filter(owner=request.user, title=h_item.title)
    
    titleown=h_item.title+' oyi uchun ma`lumotlarni tekshirish'
    
    vaqt=timezone.now()
    oy = vaqt.strftime("%m")
    yil = vaqt.strftime("%Y")

    ruxsat="disabled"
    if int(h_item.vaqt.strftime("%m"))==int(oy) and int(h_item.vaqt.strftime("%Y"))==int(yil):
        ruxsat="" 

    context ={
        'h_item':h_item,
        'h_ich':h_ich,
        'h_ist':h_ist,
        'h_uzat':h_uzat,
        'titleown':titleown,
        'val':h_item,
        'disabled': ruxsat
    }
    
    if request.method=="GET":
        return render(request, '03_foydalanuvchi/reja/2_checkreja.html', context)
    if request.method=="POST":
        
        for v in h_ich:                      
            
            qiymat=request.POST[(str(v.resurs.id)+'.1')]
            qiymat_pul=request.POST[str(v.resurs.id)+'.pul1']

            v.qiymat=qiymat
            v.qiymat_pul=qiymat_pul

            v.save()
        
        for v in h_ist: 
            qiymat=request.POST[str(v.resurs.id)+'.2']
            qiymat_pul=request.POST[str(v.resurs.id)+'.pul2']
            
            v.qiymat=qiymat
            v.qiymat_pul=qiymat_pul

            v.save()

        for v in h_uzat:                  
            qiymat=request.POST[str(v.resurs.id)+'.3']
            qiymat_pul=request.POST[str(v.resurs.id)+'.pul3']
            
            v.qiymat=qiymat
            v.qiymat_pul=qiymat_pul

            v.save()
        messages.success(request, 'Shartnomaviy miqdorlardan '+h_item.title+' muvofaqqiyatli yangilandi!')            
        
        return redirect('reja')

#****************************Davriy ma'lumotlar**************************
@group_required('Faqirlar')
@application_req()
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

@group_required('Faqirlar')
@application_req()
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
    for i in range(2010,2023):
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
            messages.error(request, 'Siz allaqachon uchbu davr uchun hisobot yuborgansiz, agar xatoliklar yuzasidan murojaatingiz bo`lsa murojaat bo`limidan murojaat qilishingiz mumkin! ')            
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
            
        messages.success(request, 'Hisobot muvafaqqiyatli yuborildi! ')
        return redirect('davr')
@group_required('Faqirlar')
@application_req()
def checkdavr(request, id):
    h_item=hisobot_item.objects.get(pk=id)
    
    h_ich=hisobot_ich.objects.filter(owner=request.user, title=h_item.title)
    h_ist=hisobot_ist.objects.filter(owner=request.user, title=h_item.title)
    h_uzat=hisobot_uzat.objects.filter(owner=request.user, title=h_item.title)
    
    titleown=h_item.title+' oyi uchun ma`lumotlarni tekshirish'
    vaqt=timezone.now()
    oy = vaqt.strftime("%m")
    yil = vaqt.strftime("%Y")

    #ruxsat="disabled"
    #if int(h_item.vaqt.strftime("%m"))==int(oy) and int(h_item.vaqt.strftime("%Y"))==int(yil):
    ruxsat="" 

    context ={
        'h_item':h_item,
        'h_ich':h_ich,
        'h_ist':h_ist,
        'h_uzat':h_uzat,
        'titleown':titleown,
        'val':h_item,
        'ruxsat':ruxsat        
    }
    
    if request.method=="GET":
        return render(request, '03_foydalanuvchi/02_2_checkdavr.html', context)
    if request.method=="POST":
        
        for v in h_ich:                      
            
            qiymat=request.POST[(str(v.resurs.id)+'.1')]
            qiymat_pul=request.POST[str(v.resurs.id)+'.pul1']

            v.qiymat=qiymat
            v.qiymat_pul=qiymat_pul

            v.save()
        
        for v in h_ist: 
            qiymat=request.POST[str(v.resurs.id)+'.2']
            qiymat_pul=request.POST[str(v.resurs.id)+'.pul2']
            
            v.qiymat=qiymat
            v.qiymat_pul=qiymat_pul

            v.save()

        for v in h_uzat:                  
            qiymat=request.POST[str(v.resurs.id)+'.3']
            qiymat_pul=request.POST[str(v.resurs.id)+'.pul3']
            
            v.qiymat=qiymat
            v.qiymat_pul=qiymat_pul

            v.save()
        messages.success(request, 'Davriy hisobotlardan '+h_item.title+' muvofaqqiyatli yangilandi!')            
        
        return redirect('davr')

#********************Tashkiliy tadbirlar kiritish*****************************************
@group_required('Faqirlar')
@application_req()
def tadbir(request):
    titleown = 'Tashkiliy texnik tadbirlar'

    #/////////////////*******************///////////////////////////////
    TTT=TexnikTadbir.objects.filter(owner=request.user)

    #***Resurslarni ko'rsatish
    res=[]
    for r in ichres.objects.filter(owner=request.user):
        res.append(r.resurs)
    for r in istres.objects.filter(owner=request.user):
        res.append(r.resurs)
    for r in sotres.objects.filter(owner=request.user):
        res.append(r.resurs)    
    res=list(set(res))
    T_ID = timezone.now().strftime("%Y%m%d%H%M%S")
    #/////////////****************************/////////////////////////
    t_reja=TTT_umumiy_reja.objects.filter(owner=request.user)

    list_danger=[]
    for i in range(50):
        list_danger.append(i)

    context={
        'res':res,
        'titleown':titleown,        
        'show':'show',
        'ttt':TTT,
        'T_ID':T_ID,
        't_reja':t_reja,
        'list_danger':list_danger,
    }
    return render(request, '03_foydalanuvchi/Tadbir/0_Tadbir.html', context)


@group_required('Faqirlar')
@application_req()
def addttt(request):
    if request.method=="POST":

        T_ID=request.POST['T_ID']
        ttt=TTT_reja.objects.filter(owner=request.user, T_ID=T_ID)

        n=0
        for i in ttt:
            n=n+1
        
        if n>0:
            for t in ttt:
                if t.nomi=="" or t.izoh=="" or t.tejaladi==0 or t.tejaladi_pul==0:
                    messages.warning(request, 'Bo`sh o`rinlarni to`ldirilib saqlanganidan so`ng yangi TTCHT ochish mumkin! ')
                    return redirect('addtexniktadbir/'+str(T_ID))
                
        TTT_reja.objects.create(owner=request.user, guruh=Tadbir.objects.first(), T_ID=T_ID, dan="1996-01-26", gacha="1996-01-26")

        messages.success(request, 'Yangi tashkiliy texnik tadbir oynasi muvofaqqiyatli qo`shildi! ')
        
        return redirect('addtexniktadbir/'+str(T_ID))

@group_required('Faqirlar')
@application_req()
def tttsave(request, T_ID, id):

    if request.method=="POST":
        t_reja=TTT_reja.objects.filter(owner=request.user).get(pk=id)

        t_reja.guruh=Tadbir(request.POST['gr'])
        t_reja.nomi=request.POST['nomi']        
        t_reja.tejaladi=request.POST['tejaladi']
        t_reja.tejaladi_pul=request.POST['tejaladi_pul']
        t_reja.izoh=request.POST['izoh']
        t_reja.aktiv=True
        oraliq=request.POST['oraliq']
        oraliq=oraliq.split(" <<>> ")

        t_reja.dan=oraliq[0]
        if len(oraliq)==1:
            messages.success(request, 'Boshlanish va tugash vaqtlarini to`liq kiriting')    
            url='addtexniktadbir/'+str(T_ID)
            next = request.POST.get('next', '/foydalanuvchi/'+url)            
            return HttpResponseRedirect(next)
        else:
            t_reja.gacha=oraliq[1]
            pass

        t_reja.save()

        messages.success(request, t_reja.nomi+' nomli tashkiliy texnik tadbir muvafaqqiyatli saqlandi')    
        
        url='addtexniktadbir/'+str(T_ID)
        next = request.POST.get('next', '/foydalanuvchi/'+url)            
        return HttpResponseRedirect(next)


@group_required('Faqirlar')
@application_req()
def delttt(request, id, T_ID):    
    ttt = TTT_reja.objects.get(pk=id)
    

    messages.success(request, ttt.nomi+' nomli tashkiliy texnik tadbir muvafaqqiyatli o`chirildi')    
    
    ttt.delete()
    url='addtexniktadbir/'+str(T_ID)
    next = request.POST.get('next', '/foydalanuvchi/'+url)
    
    return HttpResponseRedirect(next)

@group_required('Faqirlar')
@application_req()
def addt_umumiy(request):
    if request.method=="POST":

        T_ID = timezone.now().strftime("%Y%m%d%H%M%S")
        resurs=request.POST['resurs']
        tejaladi=request.POST['tejaladi']
        tejaladi_pul=request.POST['tejaladi_pul']
        oraliq=request.POST['oraliq']
        
        oraliq=oraliq.split(" <<>> ")            
        dan=oraliq[0]
        if len(oraliq)==1:
            messages.success(request, 'Boshlanish va tugash')    
            return redirect('addtexniktadbir')
        else:
            gacha=oraliq[1]

        TTT_umumiy_reja.objects.create(owner=request.user, T_ID=T_ID, dan=dan, gacha=gacha,
                                                resurs=resurslar(resurs), tejaladi=tejaladi, tejaladi_pul=tejaladi_pul)
       

        messages.success(request, 'Yangi tashkiliy texnik tadbirni qo`shish oynasi muvofaqqiyatli ochildi!')    
        return redirect('addtexniktadbir/'+str(T_ID))
        

@group_required('Faqirlar')
@application_req()
def addtexniktadbir(request,id):
    titleown='Texnik tadbirlar qo`shish'
    tadbirlar=Tadbir.objects.all()
    
    t_umumiy=TTT_umumiy_reja.objects.filter(owner=request.user).get(T_ID=id)
    ttt=TTT_reja.objects.filter(owner=request.user, T_ID=id)

    n=0
    for i in ttt:
        n=n+1

    #***Resurslarni ko'rsatish
    res=[]
    for r in ichres.objects.filter(owner=request.user):
        res.append(r.resurs)
    for r in istres.objects.filter(owner=request.user):
        res.append(r.resurs)
    for r in sotres.objects.filter(owner=request.user):
        res.append(r.resurs)    
    res=list(set(res))

    dangacha=str(t_umumiy.dan)+" <<>> "+str(t_umumiy.gacha)
    context = {
        'T_ID':id,
        'titleown':titleown,
        'show':'show',
        'tad':tadbirlar,
        'birlik':birliklar.objects.all(),
        'resurslar':resurslar.objects.all(),
        'ttt':ttt,
        'n':n,
        't_umumiy':t_umumiy,
        'res':res,
        'dangacha':dangacha,
        


    }
    if request.method == 'GET':
        return render(request, '03_foydalanuvchi/Tadbir/1_addtadbir.html', context)
            
    if request.method == 'POST':

        tadbir = request.POST['tadbir']
        izoh = request.POST['izoh']   
        resurs=request.POST['resurs']      
        tejaldi = request.POST['tejaldi'] 
        
        vaqt=timezone.now()-relativedelta(month=int(timezone.now().strftime('%m'))-1)
        sana = vaqt.strftime("%Y-%m-%d")

        TexnikTadbir.objects.create(owner=request.user, sana=sana, 
                                    tadbir=Tadbir(tadbir), izoh=izoh,
                                    resurs=resurslar(resurs), tejaldi=tejaldi)

        messages.success(request, 'Yangi tashkiliy texnik tadbir muvofaqqiyatli qo`shildi! ')
        return redirect('ftadbir')

@group_required('Faqirlar')
@application_req()
def t_umumiysave(request, T_ID, id):
    if request.method == 'POST':
        t_reja=TTT_umumiy_reja.objects.filter(owner=request.user).get(pk=id)
        t_reja.resurs=resurslar(request.POST['resurs'])         
        t_reja.tejaladi=request.POST['tejaladi']
        t_reja.tejaladi_pul=request.POST['tejaladi_pul']
        oraliq=request.POST['oraliq']
        oraliq=oraliq.split(" <<>> ")
        t_reja.dan=oraliq[0]
        t_reja.save()

        reja_s=0
        for i in TTT_reja.objects.filter(owner=request.user, T_ID=T_ID):
            reja_s=reja_s+float(i.tejaladi)
        reja_pul=0
        for i in TTT_reja.objects.filter(owner=request.user, T_ID=T_ID):
            reja_pul=reja_pul+float(i.tejaladi_pul)

        xat=''
        if reja_s!=float(t_reja.tejaladi) or reja_pul!=float(t_reja.tejaladi_pul):
            if reja_s>float(t_reja.tejaladi) or reja_pul>float(t_reja.tejaladi_pul):
                xat='TTCHT lar miqdori umumiy rejadan ortiq!'
            if reja_s<float(t_reja.tejaladi) or reja_pul<float(t_reja.tejaladi_pul):
                xat='Rejalashririlgan umumiy miqdorni bajarish uchun TTCHT lar yetarli emas!'    
            
            messages.error(request, xat) 
            url='addtexniktadbir/'+str(T_ID)
            next = request.POST.get('next', '/foydalanuvchi/'+url)            
            return HttpResponseRedirect(next)
        
        if len(oraliq)==1:
            messages.success(request, 'Boshlanish va tugash vaqtlarini to`liq kiriting')    
            url='addtexniktadbir/'+str(T_ID)
            next = request.POST.get('next', '/foydalanuvchi/'+url)            
            return HttpResponseRedirect(next)
        else:
            t_reja.gacha=oraliq[1]
            pass

        for i in TTT_reja.objects.filter(owner=request.user, T_ID=T_ID):
            t_reja.TTT_rejalar.add(i.id)

        t_reja.save()

        messages.success(request, 'Yangi tashkiliy texnik tadbir muvafaqqiyatli tayyorlandi')    
            
        return redirect('ftadbir')


#texniktadbirni ummuman o'chirish
@group_required('Faqirlar')
@application_req()
def deltexniktadbir(request, id):
    
    t_umumiy=TTT_umumiy_reja.objects.get(pk=id)

    for v in t_umumiy.TTT_rejalar.all():
        v.delete()
    
    t_umumiy.delete()

    messages.success(request, 'Tashkiliy texnik tadbir muvafaqqiyatli o`chirildi')    
    return redirect('ftadbir')

@group_required('Faqirlar')
@application_req()
def fakttadbir(request, id):
    t_reja=TTT_umumiy_reja.objects.get(pk=id)
    qoldi=(t_reja.gacha-(timezone.now().date())).days
    rejalar=t_reja.TTT_rejalar.all()
    
    bajarildi=[]
    for i in range(100):
        bajarildi.append(i)
    
    vaqt=timezone.now()
    list_danger=[]
    for i in range(50):
        list_danger.append(i)

    
    context={
        't_reja':t_reja,
        'qoldi':qoldi,
        'rejalar':rejalar,
        'vaqt':vaqt,
        'list_danger':list_danger,
        'bajarildi':bajarildi,
    }

    if request.method == 'GET':
        return render(request, '03_foydalanuvchi/Tadbir/3_fakttadbir.html', context)

    if request.method == 'POST':
        pass

    #messages.success(request, 'Tashkiliy texnik tadbir muvafaqqiyatli o`chirildi')    

@group_required('Faqirlar')
@application_req()
def faktsave(request, id1, id2):  
    if request.method == 'POST':
        
        t_reja=TTT_reja.objects.get(pk=id1)

        t_reja.tejaldi=request.POST['tejaldi']
        t_reja.tejaldi_pul=request.POST['tejaldi_pul']
        t_reja.nega=request.POST['nega']
        
        bajarilishi=float(request.POST['bajarilishi'])
        if bajarilishi==0 or t_reja.bajarilishi==bajarilishi:
            bajarilishi=int(float(t_reja.tejaldi)*100/t_reja.tejaladi)
        
        t_reja.bajarilishi=bajarilishi

        if t_reja.bajarilishi>=100:
            t_reja.tugadi_sanasi=timezone.now().date()
        
        t_reja.save()

        t_umumiy=TTT_umumiy_reja.objects.get(owner=request.user, T_ID=t_reja.T_ID)
        
        f_jami=0;
        for i in t_umumiy.TTT_rejalar.all():
            f_jami+=i.tejaldi
        t_umumiy.tejaldi=f_jami

        f_jami_pul=0;
        for i in t_umumiy.TTT_rejalar.all():
            f_jami_pul+=i.tejaldi_pul
        t_umumiy.tejaldi_pul=f_jami_pul

        t_umumiy.bajarilishi=int(float(t_umumiy.tejaldi)*100/float(t_umumiy.tejaladi))
        if t_umumiy.bajarilishi>=100:
            t_umumiy.tugash_sanasi=timezone.now().date()
        
        t_umumiy.save()

        messages.success(request, t_reja.nomi+' muvafaqqiyatli saqlandi')    
        url='fakttadbir/'+str(id2)
        next = request.POST.get('next', '/foydalanuvchi/'+url)            
        return HttpResponseRedirect(next) 

@group_required('Faqirlar')
@application_req()
def faktedit(request, id1, id2):  
       
    t_reja=TTT_reja.objects.get(pk=id1)

    t_reja.bajarilishi=0
    t_reja.save()

    messages.warning(request, t_reja.nomi+' nomli tadbir qayta tahrir uchun yuborildi')    
    url='fakttadbir/'+str(id2)
    next = request.POST.get('next', '/foydalanuvchi/'+url)            
    return HttpResponseRedirect(next) 
        
@group_required('Faqirlar')
@application_req()
def vvp(request):
    titleown = 'Ishlab chiqarilgan mahsulot miqdori'
    
    context={
        'titleown':titleown,        
        'show':'show',    
        'vvp':VVP.objects.filter(owner=request.user)
    }
    return render(request, '03_foydalanuvchi/VVP/0_VVP.html', context)

@group_required('Faqirlar')
@application_req()
def addvvp(request):
    titleown = 'Ishlab chiqarilgan mahsulot miqdori'
   
    context = {
        'titleown':titleown,
        'show':'show',
        'birlik':birliklar.objects.all(),
        'valyuta':Valyuta.objects.all(),
    }

    if request.method == 'GET':
        return render(request, '03_foydalanuvchi/VVP/1_addVVP.html', context)
            
    if request.method == 'POST':

        nomi = request.POST['nomi']
        VP = request.POST['VVP']        
        birlik = request.POST['birlik']
        pul = request.POST['pul']        
        pul_birlik = request.POST['pul_birlik']      
        
        vaqt=timezone.now()-relativedelta(month=int(timezone.now().strftime('%m'))-1)
        sana = vaqt.strftime("%Y-%m-%d")

        VVP.objects.create(owner=request.user, sana=sana, 
                                    nomi=nomi, VVP=VP,
                                    birlik=birliklar(birlik), pul=pul, pul_birlik=Valyuta(pul_birlik))

        messages.success(request, 'Yangi ishlab chiqarilgan mahsulot miqdori muvofaqqiyatli qo`shildi! ')
        return redirect('vvp')

#***********************Hisobotlar tayyorlash*********************************************
@group_required('Faqirlar')    
@application_req()
def hisobot(request):
    titleown = 'Davriy hisobotlar'
    
    his = hisobot_full.objects.filter(owner=request.user)
    ist = istres.objects.filter(owner=request.user)    
    
    context={
        'titleown':titleown,        
        'values':ist,
        'his':his,
        'show1':'show'
    }
    
    return render(request, '03_foydalanuvchi/03_0_hisobot.html', context)

@group_required('Faqirlar')
@application_req()
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
        res_show[i]=resurslar.objects.get(pk=i).nomi+' ( '+str(resurslar.objects.get(pk=i).birlik)+' )'
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
        
        tur = request.POST.getlist('his_tur')
        
        if not tur:
            messages.error(request, 'Hisobot turlaridan birini tanlang! ')
            return redirect('addhisobot')
        
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
        
        if not hisobot_item.objects.filter(owner=request.user, vaqt__range=[str(oraliq_min), str(oraliq_max)]):
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

@group_required('Faqirlar')
@application_req()
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

@group_required('Faqirlar')
@application_req()
def delhis(request, id):
    davlat = his_ich.objects.get(pk=id)
    davlat.delete()
    messages.success(request, 'Resurs muvafaqqiyatli o`chirildi')
    return redirect('addhisobot')

##########################################################################

@group_required('Faqirlar')
@application_req()
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
            b=' (mln.'+str(resurslar.objects.get(pk=i).birlik)+' )'               
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
                                koef2=j.qiymat
                            if birl == 'valut':
                                koef2=1000*j.qiymat*his.valyuta.qiymati/his.valyuta.somda
                            q=j.qiymat_pul*koef2/(1000000)
                        
                        obj[r].append(float('{0:.2f}'.format(float(q))))
                        
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
    
#_________________________________*************Prognozlash*********************__________________________________________________________________
def prognoz(request):
    
    context={
        't':"text"
    }
    return render(request, '03_foydalanuvchi/04_prognoz.html', context)

def addprognoz(request):
    context={
        't':"text"
    }
    return render(request, '03_foydalanuvchi/04_1_addprognoz.html', context)

def resultprognoz(request):
    context={
        't':"text"
    }
    return render(request, '03_foydalanuvchi/04_2_result.html', context)

#_________________________________*************Me'yorlash*********************__________________________________________________________________
def norm(request):
    
    context={
        't':"text"
    }
    return render(request, '03_foydalanuvchi/05_norm.html', context)

def addnorm(request):
    context={
        't':"text"
    }
    return render(request, '03_foydalanuvchi/05_1_addnorm.html', context)

def resultnorm(request):
    context={
        't':"text"
    }
    return render(request, '03_foydalanuvchi/05_2_resnorm.html', context)

#_________________________________*************Energobalans*********************__________________________________________________________________
def balans(request):
    context={
        't':"text"
    }
    return render(request, '03_foydalanuvchi/06_balans.html', context)

def addbalans(request):
    context={
        't':"text"
    }
    return render(request, '03_foydalanuvchi/06_1_addbalans.html', context)

def resultbalans(request):
    context={
        't':"text"
    }
    return render(request, '03_foydalanuvchi/06_2_result.html', context)


#_________________________________*************ENERGO SAMARADORLIK*********************__________________________________________________________________

def ensam(request):
    vvp=VVP.objects.filter(owner=request.user)

    list_vvp={}
    for i in vvp:
        list_vvp[i.sana]=i.VVP/(i.VVP+random.randint(1,9)*10**(len(str(i.VVP))-3))

    context={
        "titleown": "Energiya sig'imliligi",
        'list_vvp':list_vvp
    }
    return render(request, '03_foydalanuvchi/samaradorlik/0_sam.html', context)

def changesam(request):
    context={
        "titleown": "Energiya samaradorlik"
    }
    return render(request, '03_foydalanuvchi/samaradorlik/1_addsam.html', context)

#*******************************SIFAT*****************************************************
def hisoblagichlar(request):
    context={
        't':"text"
    }
    return render(request, '03_foydalanuvchi/nosim/0_hisoblagichlar.html', context)