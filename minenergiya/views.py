import re
from django.shortcuts import render, redirect

from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone

import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
import six

from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta
from foydalanuvchi.models import allfaqir, TexnikTadbir, his_ich, ichres, istres, sotres
from s_ad.models import IFTUM, THST, DBIBT, resurslar, Valyuta
from django.core.exceptions import PermissionDenied
from .models import filtr_faqir, guruh, ensamfiltr, tur, klassifikator

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

@group_required('whitebone')	
def home(request):

    context={
        
    }
    return render(request, '04_minenergiya/tahlil/01_0_korxonalar.html', context)

@group_required('whitebone')	
def korxonalar(request):
    fqir=allfaqir.objects.all()


    context={
        'titleown': 'Foydalanuvchilar ro`yxati',
        'fqir':fqir
    }
    return render(request, '04_minenergiya/tahlil/01_0_korxonalar.html', context)

#************Baxrom aka jadvallari********************************
#************I jadval********************************
@group_required('whitebone')	
def I_jadval(request):

    fqir=allfaqir.objects.all()


    context={
        'titleown': 'I jadval',
        
    }
    return render(request, '04_minenergiya/Baxrom/01_0_jadval.html', context)
@group_required('whitebone')	
def I_add(request):

    fqir=allfaqir.objects.all()


    context={
        'titleown': 'I jadval tayyorlash',
        
    }

    return render(request, '04_minenergiya/Baxrom/01_1_add.html', context)
@group_required('whitebone')	
def I_result(request):

    fqir=allfaqir.objects.all()


    context={
        'titleown': 'I jadval tayyorlash',
        
    }

    return render(request, '04_minenergiya/I_jadval copy/2_I_result.html', context)

#*****************II jadval***********************************
@group_required('whitebone')	
def II_result(request):
    fqir=allfaqir.objects.all()

    sana = (timezone.now()-relativedelta(month=int(timezone.now().strftime('%m'))-1))
    
    oylar = ['YANVAR', 'FEVRAL', 'MART', 'APREL', 'MAY', 'IYUN', 'IYUL', 'AVGUST','SENTYABR', 'OKTYABR', 'NOYABR', 'DEKABR']
    oy = oylar[int(sana.strftime("%m"))-1]    
    yil = sana.strftime("%Y")

    context={
        'titleown': 'III jadval tayyorlash',
        't_umumiy':t_umumiy,
        'faqir':fqir,
        'yil':yil,
        'oy':oy,
    }

    return render(request, '04_minenergiya/II_jadval/2_II_result.html', context)

#*****************III jadval***********************************
@group_required('whitebone')	
def III_result(request):
    fqir=allfaqir.objects.all()
    ttt=TexnikTadbir.objects.all()

    context={
        'titleown': 'III jadval tayyorlash',
        't_umumiy':t_umumiy,
    }

    return render(request, '04_minenergiya/III_jadval/2_III_result.html', context)
#*****************Tashkiliy texnik tadbirlar**********************************************
@group_required('whitebone')	
def t_umumiy(request):
    fqir=allfaqir.objects.all()
    ttt=TexnikTadbir.objects.all()

    t_1=[]
    for i in ttt:
        t_1.append(i)
    
    t_umumiy={}
    for i in t_1:
        t_umumiy[i]=allfaqir.objects.get(owner=i.owner)

    context={
        'titleown': 'I jadval tayyorlash',
        't_umumiy':t_umumiy,        
        't_1':t_1
    }

    return render(request, '04_minenergiya/Tadbir/0_Tadbir.html', context)
@group_required('whitebone')	
def tejash(request):
    fqir=allfaqir.objects.all()
    ttt=TexnikTadbir.objects.all()

    t_1=[]
    for i in ttt:
        t_1.append(i)
    
    t_umumiy={}
    for i in t_1:
        t_umumiy[i]=allfaqir.objects.get(owner=i.owner)

    context={
        'titleown': 'I jadval tayyorlash',
        't_umumiy':t_umumiy,        
        't_1':t_1
    }

    return render(request, '04_minenergiya/Tadbir/0_Tadbir.html', context)

#********************Yoqilg'i sarfi*************************
@group_required('whitebone')	
def ensamkor(request):
    
    context={

    }    
    return render(request, '04_minenergiya/ensamkor/0_ensamkor.html', context)
@group_required('whitebone')	
def addensamkor(request):

    his_tur=tur.objects.filter(owner=request.user)

    iftum=IFTUM.objects.all()
    dbibt=DBIBT.objects.all()
    thst=THST.objects.all()
    fqr=allfaqir.objects.all()
    rsrs=resurslar.objects.filter(owner=request.user)
    filtr=filtr_faqir.objects.filter(owner=request.user)
    faqir_show=filtr_faqir.objects.filter(owner=request.user)  
    turi=tur.objects.filter(owner=request.user) 
    kl=klassifikator.objects.filter(owner=request.user)    
    
    list_klss=[]
    for k in kl:
        lk=k.klass.split(", ")
        lk.remove('')
        list_klss=lk

    #***Resurslarni ko'rsatish
    resurs_list=[]
    for i in faqir_show:            
        for r in ichres.objects.filter(owner=i.fqr.owner):
            resurs_list.append(r.resurs)
        for r in istres.objects.filter(owner=i.fqr.owner):
            resurs_list.append(r.resurs)
        for r in sotres.objects.filter(owner=i.fqr.owner):
            resurs_list.append(r.resurs)
        
    resurs_list=list(set(resurs_list))       
    #**************************************************************************************************    
    
    
    context={
        'iftum':iftum,
        'dbibt': dbibt,
        'thst':thst,
        'faqir_show':faqir_show,
        'fqr':fqr,
        'rsrs': rsrs,
        'resurs_list':resurs_list,
        'his_res':his_ich.objects.filter(owner=request.user),
        'valyuta':Valyuta.objects.all(),
        'his_tur':his_tur,
        'turi':turi,
        'kl':kl,
        'list_klass':list_klss,
    }

    if request.method == 'GET':
        return render(request, '04_minenergiya/ensamkor/1_addhisobot.html', context)
    if request.method == 'POST':
        oraliq=request.POST['oraliq']        
        
        olchov=request.POST.getlist('olchov')

        if not oraliq:
            messages.error(request, 'Iltimos oraliqni kiriting?! ')           
            return redirect('addensamkor')
        oraliq=oraliq.split(" <<>> ")
        dan=oraliq[0]
        if len(oraliq)==1:
            gacha=dan
        else:
            gacha=oraliq[1]

        vaqt=timezone.now()
        
        
        ensamfiltr.objects.create(
                                    owner=request.user, 
                                    nomi="hisobotcha", 
                                vaqt=vaqt, 
                                dan=dan, gacha=gacha)
        messages.success(request, 'Hisobot muvafaqqiyatli tayyorlandi! ')
        return redirect('ensamkor')
#kodlar bo'yicha chiqarish:
@group_required('whitebone')	
def fqr_show(request):    
    fqr=allfaqir.objects.all()
    
    if request.method == 'POST':
        
        iftum_fqr = request.POST['iftum_fqr']        
        dbibt_fqr = request.POST['dbibt_fqr']
        thst_fqr = request.POST['thst_fqr']
        stirnom=request.POST.getlist('stirnom')
        
        if iftum_fqr=="0":
            for i in fqr.filter(dbibt=DBIBT(dbibt_fqr), thst=THST(thst_fqr)):
                if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                    pass
                else:
                    filtr_faqir.objects.create(owner=request.user, 
                                            fqr=allfaqir.objects.get(pk=i.id))
        if dbibt_fqr=="0":
            for i in fqr.filter(iftum=iftum_fqr, thst=THST(thst_fqr)):
                if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                    pass
                else:
                    filtr_faqir.objects.create(owner=request.user, 
                                            fqr=allfaqir.objects.get(pk=i.id))
        if thst_fqr=="0":
            for i in fqr.filter(iftum=iftum_fqr, dbibt=DBIBT(dbibt_fqr)):
                if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                    pass
                else:
                    filtr_faqir.objects.create(owner=request.user, 
                                            fqr=allfaqir.objects.get(pk=i.id))
        
        if iftum_fqr!="0" and dbibt_fqr=="0" and thst_fqr=="0":
            for i in fqr.filter(iftum=iftum_fqr,):
                if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                    pass
                else:
                    filtr_faqir.objects.create(owner=request.user, 
                                            fqr=allfaqir.objects.get(pk=i.id))
        if iftum_fqr=="0" and dbibt_fqr!="0" and thst_fqr=="0":
            for i in fqr.filter(dbibt=DBIBT(dbibt_fqr)):
                if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                    pass
                else:
                    filtr_faqir.objects.create(owner=request.user, 
                                            fqr=allfaqir.objects.get(pk=i.id))
        if iftum_fqr=="0" and dbibt_fqr=="0" and thst_fqr!="0":
            for i in fqr.filter(thst=THST(thst_fqr)):
                if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                    pass
                else:
                    filtr_faqir.objects.create(owner=request.user, 
                                            fqr=allfaqir.objects.get(pk=i.id))
        if iftum_fqr=="0" and dbibt_fqr=="0" and thst_fqr=="0" and len(stirnom)==0:
            messages.warning(request, "Hech bir kod belgilanmadi!")    
        
        for i in fqr.filter(iftum=iftum_fqr, dbibt=DBIBT(dbibt_fqr), thst=THST(thst_fqr)):
            if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                pass
            else:
                filtr_faqir.objects.create(owner=request.user, 
                                            fqr=allfaqir.objects.get(pk=i.id))
        
        for i in stirnom:            
            if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i)).first():        
                pass
            else:
                filtr_faqir.objects.create(owner=request.user, 
                                            fqr=allfaqir.objects.get(pk=i))

        messages.success(request, "Muvofaqqiyatli biriktirildi!")

        return redirect('addensamkor')
@group_required('whitebone')	
def delfaqirshow(request, id):

    d = filtr_faqir.objects.get(pk=id)
    d.delete()
    messages.success(request, 'Muvofaqqiyatli o`chirildi')
    return redirect('addensamkor')

@group_required('whitebone')	
def ensamkor_result(request):
    

    context={
        

    }    
    return render(request, '04_minenergiya/ensamkor/2_result.html', context)

#****************FILTR**************************************************
@group_required('whitebone')
def addfiltrres(request):
    
    faqir_show=filtr_faqir.objects.filter(owner=request.user)       
    
   
    if request.method=="POST":        
        resurs=request.POST.getlist('resurs_id')
        barcha=request.POST.getlist('barcha')

        if "1" in barcha:
            for v in faqir_show:
                for r in ichres.objects.filter(owner_id=v.fqr.owner_id):
                    if his_ich.objects.filter(owner=request.user, resurs = r.resurs_id).first():
                        pass                        
                    else:
                        his_ich.objects.create(
                            owner=request.user,
                            resurs=resurslar(pk=r.resurs_id))     

                for r in istres.objects.filter(owner_id=v.fqr.owner_id):
                    if his_ich.objects.filter(owner=request.user, resurs = r.resurs_id).first():
                        pass                        
                    else:
                        his_ich.objects.create(
                            owner=request.user,
                            resurs=resurslar(pk=r.resurs_id))    

                for r in sotres.objects.filter(owner_id=v.fqr.owner_id):
                    if his_ich.objects.filter(owner=request.user, resurs = r.resurs_id).first():
                        pass                        
                    else:
                        his_ich.objects.create(
                            owner=request.user,
                            resurs=resurslar(pk=r.resurs_id))                  
            
            return redirect('addensamkor')
        else:
            for i in resurs:
                if his_ich.objects.filter(owner=request.user, resurs = i).first():
                    messages.error(request, "Hurmatli foydalanuvchi ushbu resurs allaqachon qo'shilgan!")
                    return redirect('addhisobot')
                    
                his_ich.objects.create(
                    owner=request.user,
                    resurs=resurslar(pk=i)
                )
                messages.success(request, 'Resurs muvafaqqiyatli qo`shildi')
            return redirect('addensamkor')

@group_required('whitebone')	
def delfiltrres(request, id):
    davlat = his_ich.objects.get(pk=id)
    davlat.delete()
    messages.success(request, 'Resurs muvafaqqiyatli o`chirildi')
    return redirect('addensamkor')

#*************GURUH******************************
@group_required('whitebone')	
def addguruh(request):
    n=1
    for i in guruh.objects.filter(owner=request.user):
        n=n+1
    
    guruh.objects.create(owner=request.user, nomi=str(n)+"-guruh")
    
    return redirect('addensamkor')

@group_required('whitebone')	
def addtur(request):
    if request.method=="POST": 
        turi=request.POST.get('turi') 
        hudud=request.POST.get('hudud') 

        if turi=="Hudud bo`yicha":
           if hudud=="":
            messages.success(request, 'Hududni tanlang')
            return redirect('addensamkor')
           else:
            pass

        tur.objects.create(
            owner=request.user,            
            tur=turi+" "+hudud,            
        )
    
    return redirect('addensamkor')

@group_required('whitebone')	
def deltur(request, id):
    turi = tur.objects.get(pk=id)
    turi.delete()
    messages.success(request, 'Qayta hisobot turini belgilang')
    return redirect('addensamkor')

@group_required('whitebone')	
def addklassifikator(request):
    if request.method=="POST": 
        klass=request.POST.getlist('klass') 
        
        if "iftum" in klass:
            if "bob" in klass or "guruh" in klass or "sinf" in klass:
                pass
            else:
                messages.success(request, 'IFTUM parametrini tanlang')
                return redirect('addensamkor')

        kl=""
        for i in klass:
            kl=kl+", "+i

        if len(klass)==1:
            messages.success(request, 'Klassifikatorlarni tanlang')
            return redirect('addensamkor')
        klassifikator.objects.create(
            owner=request.user,            
            klass=kl,            
        )
    
    return redirect('addensamkor')

@group_required('whitebone')	
def delklassifikator(request, id):
    turi = klassifikator.objects.get(pk=id)
    turi.delete()
    messages.success(request, 'Klassifikatorni belgilang')
    return redirect('addensamkor')