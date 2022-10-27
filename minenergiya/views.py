import re
from time import strptime
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

from foydalanuvchi.models import allfaqir, TexnikTadbir, ichres, istres, sotres
from s_ad.models import IFTUM, THST, DBIBT, resurslar, Valyuta
from django.core.exceptions import PermissionDenied
from .models import filtr_faqir, guruh, ensamfiltr, tur, klassifikator, his_res
from django.http import HttpResponseRedirect, JsonResponse
import operator

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
    esf=ensamfiltr.objects.filter(owner=request.user)

    context={
        'esf':esf,

    }     
    return render(request, '04_minenergiya/ensamkor/0_ensamkor.html', context)

@group_required('whitebone')	
def addbyshablon(request, bolim):    
    context={
        'bolim':bolim,
    }    
    if request.method == 'GET':
        return render(request, '04_minenergiya/ensamkor/1_0_addhisobot.html', context)
    if request.method == 'POST':
        nomi=request.POST['nomi']

        for i in ensamfiltr.objects.filter(owner=request.user):
            if nomi==i.nomi:
                messages.error(request, "Sizda "+str(nomi)+" nomli hisobot mavjud!")
                url='addbyshablon/'+str(bolim)
                next = request.POST.get('next', '/minenergiya/'+url)            
                return HttpResponseRedirect(next)

        E_ID = bolim+"_"+timezone.now().strftime("%Y%m%d%H%M%S")        
        ensamfiltr.objects.create(
            owner=request.user, E_ID=E_ID, nomi=nomi, vaqt=timezone.now(),
        )
        url='addensamkor/'+str(E_ID)
        next = request.POST.get('next', '/minenergiya/'+url)            
        return HttpResponseRedirect(next)

@group_required('whitebone')	
def addensamkor(request, E_ID):

    his_tur=tur.objects.filter(owner=request.user, E_ID=E_ID)

    iftum=IFTUM.objects.all()
    dbibt=DBIBT.objects.all()
    thst=THST.objects.all()
    fqr=allfaqir.objects.all()

    faqir_show=filtr_faqir.objects.filter(owner=request.user, E_ID=E_ID)  
    turi=tur.objects.filter(owner=request.user, E_ID=E_ID) 
    kl=klassifikator.objects.filter(owner=request.user, E_ID=E_ID)    
    gr=guruh.objects.filter(owner=request.user, E_ID=E_ID)  
    
    esf=ensamfiltr.objects.get(owner=request.user, E_ID=E_ID)

    list_klss=[]
    for k in kl:
        lk=k.klass.split(", ")
        lk.remove('')
        list_klss=lk

    #***Resurslarni ko'rsatish
    resurs_list=resurslar.objects.all   
    #**************************************************************************************************
    
    context={
        'E_ID':E_ID,
        'iftum':iftum,
        'dbibt': dbibt,
        'thst':thst,
        'faqir_show':faqir_show,
        'fqr':fqr,
        'resurs_list':resurs_list,
        'his_res':his_res.objects.filter(owner=request.user, E_ID=E_ID),
        'valyuta':Valyuta.objects.all(),
        'his_tur':his_tur,
        'turi':turi,
        'kl':kl,
        'list_klass':list_klss,
        'gr':gr,
        'esf':esf,
    }

    if request.method == 'GET':
        return render(request, '04_minenergiya/ensamkor/1_addhisobot.html', context)
    if request.method == 'POST':
        oraliq=request.POST['oraliq']
        olchov=request.POST.getlist('olchov')
        
        if not oraliq:
            messages.error(request, 'Hisobot oralig`ini kiriting?! ')           
            url='addensamkor/'+str(E_ID)
            next = request.POST.get('next', '/minenergiya/'+url)            
            return HttpResponseRedirect(next)

        oraliq=oraliq.split(" <<>> ")
        dan=datetime.datetime.strptime(oraliq[0],"%Y-%m-%d")
        if len(oraliq)==1:
            gacha=dan
        else:
            gacha=datetime.datetime.strptime(oraliq[1],"%Y-%m-%d")
        
        esf=ensamfiltr.objects.get(owner=request.user, E_ID=E_ID)
        esf.shakl=request.POST.getlist('shakl')
        esf.dan=dan
        esf.gacha=gacha
        esf.olchov=olchov
        
        for i in filtr_faqir.objects.filter(owner=request.user, E_ID=E_ID):
            esf.filtr_faqir.add(i.id)
        for i in guruh.objects.filter(owner=request.user, E_ID=E_ID):
            esf.guruh.add(i.id)
        for i in klassifikator.objects.filter(owner=request.user, E_ID=E_ID):
            esf.klassifikator.add(i.id)    
        for i in tur.objects.filter(owner=request.user, E_ID=E_ID):
                    esf.tur.add(i.id)
        for i in his_res.objects.filter(owner=request.user, E_ID=E_ID):
                    esf.his_res.add(i.id)

        esf.save()
        messages.success(request, 'Hisobot muvafaqqiyatli biriktirildi! ')  
        return redirect('ensamkor')

#kodlar bo'yicha chiqarish:
@group_required('whitebone')	
def fqr_show(request, E_ID):    
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
                    filtr_faqir.objects.create(owner=request.user, E_ID=E_ID,
                                            fqr=allfaqir.objects.get(pk=i.id))
        if dbibt_fqr=="0":
            for i in fqr.filter(iftum=iftum_fqr, thst=THST(thst_fqr)):
                if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                    pass
                else:
                    filtr_faqir.objects.create(owner=request.user, E_ID=E_ID, 
                                            fqr=allfaqir.objects.get(pk=i.id))
        if thst_fqr=="0":
            for i in fqr.filter(iftum=iftum_fqr, dbibt=DBIBT(dbibt_fqr)):
                if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                    pass
                else:
                    filtr_faqir.objects.create(owner=request.user, E_ID=E_ID, 
                                            fqr=allfaqir.objects.get(pk=i.id))
        
        if iftum_fqr!="0" and dbibt_fqr=="0" and thst_fqr=="0":
            for i in fqr.filter(iftum=iftum_fqr,):
                if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                    pass
                else:
                    filtr_faqir.objects.create(owner=request.user, E_ID=E_ID, 
                                            fqr=allfaqir.objects.get(pk=i.id))
        if iftum_fqr=="0" and dbibt_fqr!="0" and thst_fqr=="0":
            for i in fqr.filter(dbibt=DBIBT(dbibt_fqr)):
                if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                    pass
                else:
                    filtr_faqir.objects.create(owner=request.user, E_ID=E_ID, 
                                            fqr=allfaqir.objects.get(pk=i.id))
        if iftum_fqr=="0" and dbibt_fqr=="0" and thst_fqr!="0":
            for i in fqr.filter(thst=THST(thst_fqr)):
                if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                    pass
                else:
                    filtr_faqir.objects.create(owner=request.user, E_ID=E_ID, 
                                            fqr=allfaqir.objects.get(pk=i.id))
        if iftum_fqr=="0" and dbibt_fqr=="0" and thst_fqr=="0" and len(stirnom)==0:
            messages.warning(request, "Hech bir kod belgilanmadi!")    
        
        for i in fqr.filter(iftum=iftum_fqr, dbibt=DBIBT(dbibt_fqr), thst=THST(thst_fqr)):
            if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i.id)).first():        
                pass
            else:
                filtr_faqir.objects.create(owner=request.user, E_ID=E_ID, 
                                            fqr=allfaqir.objects.get(pk=i.id))
        
        for i in stirnom:            
            if filtr_faqir.objects.filter(owner=request.user, fqr=allfaqir(i)).first():        
                pass
            else:
                filtr_faqir.objects.create(owner=request.user, E_ID=E_ID, 
                                            fqr=allfaqir.objects.get(pk=i))

        messages.success(request, "muvafaqqiyatli biriktirildi!")

        url='addensamkor/'+str(E_ID)
        next = request.POST.get('next', '/minenergiya/'+url)            
        return HttpResponseRedirect(next)
        
@group_required('whitebone')	
def delfaqirshow(request, id, E_ID):

    d = filtr_faqir.objects.get(pk=id)
    d.delete()
    messages.success(request, 'muvafaqqiyatli o`chirildi')
    
    url='addensamkor/'+str(E_ID)
    next = request.POST.get('next', '/minenergiya/'+url)            
    return HttpResponseRedirect(next)

@group_required('whitebone')	
def ensamkor_result(request, id):
    esf=ensamfiltr.objects.get(pk=id)
    
    delta = relativedelta(esf.gacha, esf.dan)
    
    #OY LAR BO"YICHA
    #******** Mahsulot ishlab chiqarish ****************************
    resurs=esf.his_res.all()     

    farq_oylar=delta.months+delta.years*12
    
    oylar=[]
    keyingi_oy=esf.dan    
    for i in range(int(farq_oylar)+1):        
        keyingi_oy=keyingi_oy+relativedelta(months=1)
        oylar.append(keyingi_oy.strftime("%m-%Y"))
    
    #mich**********************************************************
    
    oy_list = ['YANVAR', 'FEVRAL', 'MART', 'APREL', 'MAY', 'IYUN', 'IYUL', 'AVGUST','SENTYABR', 'OKTYABR', 'NOYABR', 'DEKABR']
    
    mich={}
    
    for f in esf.filtr_faqir.all():
        for oy in oylar:
            lst=[]
            oycha=oy_list[int(oy.split("-")[0])-1]
            yilcha=int(oy.split("-")[1])
            if f.fqr.fakt.all().filter(title=str(oycha)+"-"+str(yilcha)).exists():
                pass
                
                
        mich[f]=lst

    #******** Mahsulot ishlab chiqarish TAMOM **********************

    context={
        'esf':esf,
        'resurs':resurs,
        'keyingi_oy':mich
    }    
    return render(request, '04_minenergiya/ensamkor/2_result.html', context)

#****************FILTR**************************************************
@group_required('whitebone')
def addfiltrres(request, E_ID):
    
    faqir_show=filtr_faqir.objects.filter(owner=request.user)       
    
   
    if request.method=="POST":        
        resurs=request.POST.getlist('resurs_id')
        barcha=request.POST.getlist('barcha')        

        if "1" in barcha:
            for v in faqir_show:
                for r in ichres.objects.filter(owner_id=v.fqr.owner_id):
                    if his_res.objects.filter(owner=request.user, E_ID=E_ID, resurs = r.resurs_id).first():
                        pass                        
                    else:
                        his_res.objects.create(E_ID=E_ID,
                            owner=request.user,
                            resurs=resurslar(pk=r.resurs_id))     

                for r in istres.objects.filter(owner_id=v.fqr.owner_id):
                    if his_res.objects.filter(owner=request.user, E_ID=E_ID, resurs = r.resurs_id).first():
                        pass                        
                    else:
                        his_res.objects.create(
                            owner=request.user,E_ID=E_ID,
                            resurs=resurslar(pk=r.resurs_id))    

                for r in sotres.objects.filter(owner_id=v.fqr.owner_id):
                    if his_res.objects.filter(owner=request.user, E_ID=E_ID, resurs = r.resurs_id).first():
                        pass                        
                    else:
                        his_res.objects.create(
                            owner=request.user,E_ID=E_ID,
                            resurs=resurslar(pk=r.resurs_id))                  
            
            url='addensamkor/'+str(E_ID)
            next = request.POST.get('next', '/minenergiya/'+url)            
            return HttpResponseRedirect(next)
        else:
            for i in resurs:
                if his_res.objects.filter(owner=request.user, E_ID=E_ID,resurs = i).first():
                    messages.error(request, "Hurmatli foydalanuvchi ushbu resurs allaqachon qo'shilgan!")
                    url='addensamkor/'+str(E_ID)
                    next = request.POST.get('next', '/minenergiya/'+url)            
                    return HttpResponseRedirect(next)
                    
                his_res.objects.create(
                    owner=request.user,E_ID=E_ID,
                    resurs=resurslar(pk=i)
                )
                messages.success(request, 'Resurs muvafaqqiyatli qo`shildi')
            
            url='addensamkor/'+str(E_ID)
            next = request.POST.get('next', '/minenergiya/'+url)            
            return HttpResponseRedirect(next)

@group_required('whitebone')	
def delfiltrres(request, id, E_ID):
    davlat = his_res.objects.get(pk=id)
    davlat.delete()
    messages.success(request, 'Resurs muvafaqqiyatli o`chirildi')
    
    url='addensamkor/'+str(E_ID)
    next = request.POST.get('next', '/minenergiya/'+url)            
    return HttpResponseRedirect(next)

#*************GURUH******************************
@group_required('whitebone')	
def addguruh(request, E_ID):
    if request.method == 'POST':
        nomi=request.POST['nomi']

        if nomi=="":
            messages.warning(request, 'guruh nomini kiriting!')
            url='addensamkor/'+str(E_ID)
            next = request.POST.get('next', '/minenergiya/'+url)            
            return HttpResponseRedirect(next)
        
        for i in guruh.objects.filter(owner=request.user):
            if i.nomi==nomi:
                messages.warning(request, 'Ushbu nomdagi guruh mavjud!')
                url='addensamkor/'+str(E_ID)
                next = request.POST.get('next', '/minenergiya/'+url)            
                return HttpResponseRedirect(next)
        
        messages.success(request, 'Yangi guruh muvafaqqiyatli tayyorlandi')
        guruh.objects.create(owner=request.user, E_ID=E_ID, nomi=nomi)
        
        url='addensamkor/'+str(E_ID)
        next = request.POST.get('next', '/minenergiya/'+url)            
        return HttpResponseRedirect(next)

@group_required('whitebone')	
def savenameguruh(request, id, E_ID):
    if request.method == 'POST':
        nomi=request.POST['nomi']

        if nomi=="":
            messages.warning(request, 'guruh nomini kiriting!')
            return redirect('addensamkor')
        
        for i in guruh.objects.filter(owner=request.user):
            if i.nomi==nomi:
                messages.warning(request, 'Ushbu nomdagi guruh mavjud!')
                return redirect('addensamkor')

        gr=guruh.objects.get(pk=id)
        gr.nomi=nomi
        gr.save()
        messages.success(request, 'Guruh nomi muvafaqqiyatli o`zgartirildi')
        
        url='addensamkor/'+str(E_ID)
        next = request.POST.get('next', '/minenergiya/'+url)            
        return HttpResponseRedirect(next)

@group_required('whitebone')	
def addfqrtoguruh(request, id1, id2, E_ID):
    gr=guruh.objects.get(pk=id1)
    
    if gr.fqr.filter(owner=request.user, pk = id2).first():
        messages.warning(request, 'ushbu foydalanuvchi allaqachon qo`shilgan')
        return redirect('addensamkor')

    gr.fqr.add(id2)
    gr.save()
    messages.success(request, 'foydalanuvchi guruhga muvafaqqiyatli qo`shildi')
        
    url='addensamkor/'+str(E_ID)
    next = request.POST.get('next', '/minenergiya/'+url)            
    return HttpResponseRedirect(next)

@group_required('whitebone')	
def delfqrtoguruh(request, id1, id2, E_ID):
    gr=guruh.objects.get(pk=id1)
    nom=gr.fqr.all().get(pk=id2)
    gr.fqr.remove(id2)
    messages.success(request, str(nom)+' foydalanuvchi guruhdan movofaqqiyatli o`chirildi')
    
    url='addensamkor/'+str(E_ID)
    next = request.POST.get('next', '/minenergiya/'+url)            
    return HttpResponseRedirect(next)

@group_required('whitebone')	
def addtur(request, E_ID):
    if request.method=="POST": 
        turi=request.POST.get('turi') 
        hudud=request.POST.get('hudud') 

        if turi=="Hudud bo`yicha":
           if hudud=="":
            messages.warning(request, 'Hududni tanlang')
            url='addensamkor/'+str(E_ID)
            next = request.POST.get('next', '/minenergiya/'+url)            
            return HttpResponseRedirect(next)
           else:
            pass

        tur.objects.create(
            owner=request.user, E_ID=E_ID,            
            tur=turi+" "+hudud,            
        )
    messages.success(request, 'filtr turi '+str(turi)+' muvafaqqiyatli biriktirildi')        
    url='addensamkor/'+str(E_ID)
    next = request.POST.get('next', '/minenergiya/'+url)            
    return HttpResponseRedirect(next)

@group_required('whitebone')	
def deltur(request, id, E_ID):
    turi = tur.objects.get(pk=id)

    if turi.tur=="Ixtiyoriy guruhlash ":
        for i in guruh.objects.filter(owner=request.user, E_ID=E_ID):
            i.delete()
         
    turi.delete()
    messages.success(request, 'Qayta hisobot turini belgilang')
    url='addensamkor/'+str(E_ID)
    next = request.POST.get('next', '/minenergiya/'+url)            
    return HttpResponseRedirect(next)

@group_required('whitebone')	
def delgr(request, id, E_ID):
    gr = guruh.objects.get(pk=id)    
    gr.delete()
    messages.success(request, str(gr)+' guruhi muvafaqqiyatli o`chirildi')
    
    url='addensamkor/'+str(E_ID)
    next = request.POST.get('next', '/minenergiya/'+url)            
    return HttpResponseRedirect(next)

@group_required('whitebone')	
def addklassifikator(request, E_ID):
    if request.method=="POST": 
        klass=request.POST.getlist('klass') 
        
        if "iftum" in klass:
            if "bob" in klass or "guruh" in klass or "sinf" in klass:
                pass
            else:
                messages.success(request, 'IFTUM parametrini tanlang')
                url='addensamkor/'+str(E_ID)
                next = request.POST.get('next', '/minenergiya/'+url)            
                return HttpResponseRedirect(next)

        kl=""
        for i in klass:
            kl=kl+", "+i

        if len(klass)==1:
            messages.success(request, 'Klassifikatorlarni tanlang')
            url='addensamkor/'+str(E_ID)
            next = request.POST.get('next', '/minenergiya/'+url)            
            return HttpResponseRedirect(next)
        
        klassifikator.objects.create( E_ID=E_ID,
            owner=request.user,            
            klass=kl,            
        )
    
    url='addensamkor/'+str(E_ID)
    next = request.POST.get('next', '/minenergiya/'+url)            
    return HttpResponseRedirect(next)

@group_required('whitebone')	
def delklassifikator(request, id, E_ID):
    turi = klassifikator.objects.get(pk=id)
    turi.delete()
    messages.success(request, 'Klassifikatorni belgilang')

    url='addensamkor/'+str(E_ID)
    next = request.POST.get('next', '/minenergiya/'+url)            
    return HttpResponseRedirect(next)

@group_required('whitebone')	
def delensamfilter(request, id, E_ID):
    esf=ensamfiltr.objects.get(pk=id)
    for i in filtr_faqir.objects.filter(owner=request.user, E_ID=E_ID):
        i.delete()
    for i in guruh.objects.filter(owner=request.user, E_ID=E_ID):
        i.delete()
    for i in klassifikator.objects.filter(owner=request.user, E_ID=E_ID):
        i.delete()
    for i in tur.objects.filter(owner=request.user, E_ID=E_ID):
        i.delete()
    for i in his_res.objects.filter(owner=request.user, E_ID=E_ID):
        i.delete()
    
    
    esf.delete()

    messages.success(request, 'Hisobot muvofaqqiyatli o`chirildi')           
    return redirect('ensamkor')