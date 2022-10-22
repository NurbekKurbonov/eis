from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
import json

from django.shortcuts import render, redirect
from kirish.models import sahifa, savolnoma
from datetime import datetime

from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseForbidden

from django.contrib.auth.decorators import user_passes_test
import six
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from .models import davlatlar, viloyatlar, tumanlar, IFTUM, DBIBT,THST, birliklar, resurslar, Valyuta, Tadbir, yaxlitlash

from foydalanuvchi.models import allfaqir, ichres, istres, sotres, hisobot_item, hisobot_ich, hisobot_ist, hisobot_uzat, allfaqir, hisobot_full, his_ich

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


@group_required('admin2')
def icons(request):
    return render(request, 'partials/01_icons.html')
#kirish qismini to'ldirish *********************************

@group_required('admin2')
def kirishP(request):    
    title='Kirish bo`limi'
    
    sah = sahifa.objects.all() 
    paginator = Paginator(sah, 4)    
    page_number=request.GET.get('page')
    page_obj=Paginator.get_page(paginator, page_number)
    
    context = {
        'title':title,
        'sah':sah,
        'page_obj':page_obj
    }
    return render(request, '02_s_ad/01_0_kirishP.html', context)


@group_required('admin2')
def addkir(request):
    titleown='Yangi sahifa qo`shish'
    
   
    context = {
        'titleown':titleown,        
        
    }    
    if request.method == 'GET':
        return render(request, '02_s_ad/01_1_addkirishP.html', context)
    
    if request.method =='POST':
        dt=timezone.now()
        
        title = request.POST['title']
        permalink = request.POST['permalink']
        update_date = dt
        bodytext = request.POST['bodytext']
        icon = request.POST['icon'] 
        
        sahifa.objects.create(owner=request.user, title=title, permalink=permalink, update_date=update_date, bodytext=bodytext, icon=icon)
        messages.success(request, 'Yangi sahifa muvofaqqiyatli qo`shildi! ')
        return redirect('kirishP')

@group_required('admin2')
def editkir(request, id):
    
    titleown='O`zgartirish'
    sah = sahifa.objects.get(pk=id)
    
    context = {
        'sah': sah,
        'values': sah,
        'titleown':titleown
    } 
    
    if request.method == 'GET':        
        return render(request, '02_s_ad/01_2_editkirishP.html', context)
    
    if request.method =='POST':
        dt=timezone.now()
        
        title = request.POST['title']
        permalink = request.POST['permalink']        
        bodytext = request.POST['bodytext']
        icon = request.POST['icon']
        
        sah.title = title
        sah.permalink = permalink      
        sah.bodytext = bodytext
        sah.icon = icon
        
        sah.update_date = dt
        sah.owner=request.user
        
        sah.save()        
        messages.success(request, 'sahifa muvofaqqiyatli yangilandi! ')
        
        return redirect('kirishP')

@group_required('admin2')
def delkir(request, id):
    #perm tekshirish 
    user_permission=list(User.objects.get(pk=request.user.id).get_group_permissions())
    c='s_ad.change_resurslar'
    if not (c in user_permission):
        return redirect('view404')
    #******************************
    
    sah = sahifa.objects.get(pk=id)
    sah.delete()
    messages.success(request, 'Sahifa muvofaqqiyatli o`chirildi')
    return redirect('kirishP')

#Hududlar bo'yicha ma'lumotlarni kiritish*********************

@group_required('admin2')
def davlat(request):
    #perm tekshirish 
    user_permission=list(User.objects.get(pk=request.user.id).get_group_permissions())
    c='s_ad.change_resurslar'
    if not (c in user_permission):
        return redirect('view404')
    #******************************
    
    titleown='Davlatlar'
    dav = davlatlar.objects.all()
    
    context = {
        'dav': dav,
        'titleown':titleown
        }
    
    return render(request, '02_s_ad/02_0_davlat.html', context)

@group_required('admin2')
def adddavlat(request):
    #perm tekshirish 
    user_permission=list(User.objects.get(pk=request.user.id).get_group_permissions())
    c='s_ad.change_resurslar'
    if not (c in user_permission):
        return redirect('view404')
    #******************************
    
    titleown='Davlatlar'
    context = {
        'titleown':titleown
    }
    if request.method == 'GET':
        return render(request, '02_s_ad/02_1_adddavlat.html', context)
            
    if request.method == 'POST':        
        davlat_kodi = request.POST['davlat_kodi']
        davlat_nomi = request.POST['davlat_nomi']        
        
        davlatlar.objects.create(owner=request.user, davlat_kodi=davlat_kodi, davlat_nomi=davlat_nomi )        
        messages.success(request, 'Yangi davlat muvofaqqiyatli qo`shildi! ')
        return redirect('davlat')
    

@group_required('admin2')
def editdavlat(request, id):
    #perm tekshirish 
    user_permission=list(User.objects.get(pk=request.user.id).get_group_permissions())
    c='s_ad.change_resurslar'
    if not (c in user_permission):
        return redirect('view404')
    #******************************
       
    davlat = davlatlar.objects.get(pk=id)
    
    context = {
        'davlat': davlat,
        'values': davlat,
    } 
    
    if request.method == 'GET':  
        return render(request, '02_s_ad/02_2_editdavlat.html', context)
    
    if request.method == 'POST':  
        davlat_kodi = request.POST['davlat_kodi']
        davlat_nomi = request.POST['davlat_nomi'] 
        
        davlat.owner=request.user
        davlat.davlat_kodi=davlat_kodi
        davlat.davlat_nomi=davlat_nomi
        
        davlat.save()
        messages.success(request, 'Davlat muvofaqqiyatli yangilandi!')
        
        return redirect('davlat')

@group_required('admin2')
def deldavlat(request, id):
    davlat = davlatlar.objects.get(pk=id)
    davlat.delete()
    messages.success(request, 'Davlat muvofaqqiyatli o`chirildi')
    return redirect('davlat')

#viloyat*********************************

@group_required('admin2')
def viloyat(request):
    vil = viloyatlar.objects.all()
    titleown = 'Viloyatlar'
    context = {
        'vil': vil,
        'titleown':titleown
    }
    return render(request, '02_s_ad/03_0_viloyat.html', context)

@group_required('admin2')
def addviloyat(request):
    davlat = davlatlar.objects.all()
    
    context = {          
        'davlat': davlat,  
        'values': request.POST,
        'titleown':'viloyat qo`shish'
    }
    
    if request.method == 'GET':
        return render(request, '02_s_ad/03_1_addviloyat.html', context)
            
    if request.method == 'POST':        
        viloyat_davlati = request.POST['viloyat_davlati']
        viloyat_kodi = request.POST['viloyat_kodi']
        viloyat_nomi = request.POST['viloyat_nomi']           
        
        viloyatlar.objects.create(owner=request.user, viloyat_davlati=davlatlar(viloyat_davlati), viloyat_kodi=viloyat_kodi, viloyat_nomi=viloyat_nomi)        
        messages.success(request, 'Yangi viloyat muvofaqqiyatli qo`shildi! ')
        return redirect('viloyat')
   
@group_required('admin2')
def editviloyat(request, id):
    davlat = davlatlar.objects.all()   
    vil = viloyatlar.objects.get(pk=id)
    
    context = {
        'davlat': davlat, 
        'vil': vil,
        'values': vil,
        'titleown':'viloyatni o`zgartirish'
    } 
    
    if request.method == 'GET':  
        return render(request, '02_s_ad/03_2_editviloyat.html', context)
    
    if request.method == 'POST':  
        viloyat_davlati = request.POST['viloyat_davlati']
        viloyat_kodi = request.POST['viloyat_kodi']
        viloyat_nomi = request.POST['viloyat_nomi'] 
        
        vil.owner=request.user
        vil.viloyat_davlati=davlatlar(viloyat_davlati)
        vil.viloyat_nomi=viloyat_nomi
        vil.viloyat_kodi=viloyat_kodi
        
        vil.save()
        messages.success(request, 'Davlat muvofaqqiyatli yangilandi!')
        
        return redirect('viloyat')

@group_required('admin2')
def delviloyat(request, id):
    yoqol = viloyatlar.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'Viloyat o`chirildi')
    return redirect('viloyat')

#tuman****************************************************

@group_required('admin2')
def tuman(request):
    
    tum = tumanlar.objects.all()
    
    context = {
        'tum': tum,
        'titleown':'Tumanlar'
    }
    return render(request, '02_s_ad/04_0_tuman.html', context)

@group_required('admin2')
def addtuman(request):           
    dav = davlatlar.objects.all()
    vil = viloyatlar.objects.all() #.filter(viloyat_davlati=dav)
    
    if request.is_ajax():
        dav = request.GET.get('dav')
        vil = viloyatlar.objects.all().filter(viloyat_davlati=dav)               
        
        #return JsonResponse(vil, safe=False)
    
    context = {    
        'dav': dav,           
        'vil': vil,
        'values': request.POST   ,        
        
        'titleown':'yangi tumanlar qo`shish'             
        
    }
    
    if request.method == 'GET':
        return render(request, '02_s_ad/04_1_addtuman.html', context)
            
    if request.method == 'POST':  
        tuman_viloyati = request.POST['tuman_viloyati']
        tuman_kodi = request.POST['tuman_kodi']        
        tuman_nomi = request.POST['tuman_nomi']
        
        tumanlar.objects.create(owner=request.user, tuman_viloyati = viloyatlar(tuman_viloyati), tuman_kodi = tuman_kodi, tuman_nomi = tuman_nomi)
        messages.success(request, 'Yangi tuman muvofaqqiyatli qo`shildi! ')
        return redirect('tuman')
    
   
@group_required('admin2')
def edittuman(request, id):   
    vil = viloyatlar.objects.all()
    dav = davlatlar.objects.all()       
    tuman = tumanlar.objects.get(pk=id)
    context = {        
        'dav': dav,
        'vil': vil,
        'tuman': tuman,
        'values': tuman
    } 
    
    if request.method == 'GET':  
        return render(request, '02_s_ad/04_2_edittuman.html', context)
    
    if request.method == 'POST':  
        tuman_davlati = request.POST['viloyat_davlati']
        tuman_viloyati = request.POST['tuman_viloyati']
        tuman_kodi = request.POST['tuman_kodi']        
        tuman_nomi = request.POST['tuman_nomi']
        
        tuman.owner=request.user
        tuman.tuman_viloyati = viloyatlar(tuman_viloyati)
        tuman.tuman_kodi = tuman_kodi 
        tuman.tuman_nomi = tuman_nomi
        
        
        tuman.save()
        messages.success(request, 'Tuman muvofaqqiyatli yangilandi!')
        
        return redirect('tuman')

@group_required('admin2')
def deltuman(request, id):
    yoqol = tumanlar.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'Tuman muvofaqqiyatli o`chirildi')
    return redirect('tuman')

#***_________KODLAR__________**********************************************

@group_required('admin2')
def iftums(request):
    iftum = IFTUM.objects.all()
    context = {
        'iftum': iftum,
        'titleown':'IFTUM'
    }
    return render(request, '02_s_ad/05_0_iftum.html', context)

@group_required('admin2')
def addiftums(request):    
    bolimlist = ["A", "B", "C", "D","E", "F","G", "H","I", "J","K", "L","M", "N","O", "P",]    
    context = {    
        'values': request.POST,
        'bolimlist': bolimlist,
        'titleown':'IFTUM kodini qo`shish'               
    }
    
    if request.method == 'GET':
        return render(request, '02_s_ad/05_1_addiftum.html', context)
            
    if request.method == 'POST':  
        bolim = request.POST['bolim']
        bob = request.POST['bob']
        guruh = request.POST['guruh']
        sinf = request.POST['sinf']
        tartib = request.POST['tartib']
        nomi = request.POST['nomi']
        
        IFTUM.objects.create(owner=request.user, bolim= bolim, bob= bob, guruh= guruh, sinf= sinf, tartib= tartib, nomi=nomi)
        messages.success(request, 'Yangi IFTUM kodi muvofaqqiyatli qo`shildi! ')
        return redirect('iftums')

@group_required('admin2')
def editiftums(request, id): 
    bolimlist = ["A", "B", "C", "D","E", "F","G", "H","I", "J","K", "L","M", "N","O", "P",]    
    iftum = IFTUM.objects.get(pk=id)
    context = {  
        'bolimlist':bolimlist,
        'iftum': iftum,        
        'values': iftum,
        'titleown':'IFTUM kodini yangilash'
    } 
    
    if request.method == 'GET':  
        return render(request, '02_s_ad/05_2_editiftum.html', context)
    
    if request.method == 'POST':  
        bolim = request.POST['bolim']
        bob = request.POST['bob']
        guruh = request.POST['guruh']
        sinf = request.POST['sinf']
        tartib = request.POST['tartib']
        nomi = request.POST['nomi']
        
        iftum.bolim = bolim
        iftum.bob = bob
        iftum.guruh = guruh
        iftum.sinf = sinf
        iftum.tartib = tartib
        iftum.nomi =nomi
        
        iftum.owner=request.user
        
        iftum.save()
        messages.success(request, 'IFTUM kodi muvofaqqiyatli yangilandi!')   
             
        return redirect('iftums')

@group_required('admin2')
def deliftums(request, id):
    yoqol = IFTUM.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'IFTUM kodi muvofaqqiyatli o`chirildi')
    return redirect('iftums')

#DBIBT******************************************************************

@group_required('admin2')
def dbibt(request):
    dbibts=DBIBT.objects.all()
    
    context={
        'val':dbibts,
        'titleown':'DBIBT kodi'
    }
    return render(request, '02_s_ad/06_0_dbibt.html', context)

@group_required('admin2')
def adddbibt(request):    
    
    context = { 
        'titleown':'DBIBT kodini qo`shish'               
    }
    
    if request.method == 'GET':
        return render(request, '02_s_ad/06_1_adddbibt.html', context)
            
    if request.method == 'POST':  
        dbibt = request.POST['dbibt']
        ktut = request.POST['ktut']
        nomi = request.POST['nomi']
        
        DBIBT.objects.create(owner=request.user,dbibt=dbibt, ktut=ktut, nomi=nomi)
        messages.success(request, 'Yangi DBIBT kodi muvofaqqiyatli qo`shildi! ')
        return redirect('dbibt')

@group_required('admin2')
def editdbibt(request, id):
    dbibts=DBIBT.objects.get(pk=id)  
    
    context = {          
        'dbibts': dbibts,        
        'values': dbibts,
        'titleown':'DBIBT kodini yangilash'
    } 
    
    if request.method == 'GET':  
        return render(request, '02_s_ad/06_2_editdbibt.html', context)
    
    if request.method == 'POST':  
        
        dbibt = request.POST['dbibt']
        ktut = request.POST['ktut']
        nomi = request.POST['nomi']
        
        dbibts.dbibt = dbibt
        dbibts.ktut = ktut
        dbibts.nomi = nomi
        
        dbibts.owner=request.user
        
        dbibts.save()
        messages.success(request, 'DBIBT kodi muvofaqqiyatli yangilandi!')
        
        return redirect('dbibt')

@group_required('admin2')
def deldbibt(request, id):
    yoqol = DBIBT.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'DBIBT kodi muvofaqqiyatli o`chirildi')
    return redirect('dbibt')

#TASHKIL-HUQUQIY SHAKLLARI TASNIFI. ******************************************************************

@group_required('admin2')
def thst(request):
    ths=THST.objects.all()
    
    context={
        'val':ths,
        'titleown':'THSHT kodi'
    }
    return render(request, '02_s_ad/07_0_thsht.html', context)

@group_required('admin2')
def addthst(request):    
    
    context = { 
        'titleown':'THSHT kodini qo`shish'               
    }
    
    if request.method == 'GET':
        return render(request, '02_s_ad/07_1_addthsht.html', context)
            
    if request.method == 'POST':  
        bolim = request.POST['bolim']
        tur = request.POST['tur']
        nomi = request.POST['nomi']        
        
        THST.objects.create(owner=request.user, bolim = bolim, tur = tur, nomi=nomi)
        messages.success(request, 'Yangi THSHT kodi muvofaqqiyatli qo`shildi! ')
        return redirect('thst')

@group_required('admin2')
def editthst(request, id):
    ths=THST.objects.get(pk=id)  
    
    context = {          
        'ths': ths,        
        'values': ths,
        'titleown':'THSHT kodini yangilash'
    } 
    
    if request.method == 'GET':  
        return render(request, '02_s_ad/07_2_editthsht.html', context)
    
    if request.method == 'POST':  
        
        bolim = request.POST['bolim']
        tur = request.POST['tur']
        nomi = request.POST['nomi']    
        
        ths.bolim = bolim
        ths.tur = tur
        ths.nomi = nomi
        
        ths.owner=request.user
        
        ths.save()
        messages.success(request, 'THSHT kodi muvofaqqiyatli yangilandi!')
        
        return redirect('thst')

@group_required('admin2')
def delthst(request, id):
    yoqol = THST.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'THSHT kodi muvofaqqiyatli o`chirildi')
    return redirect('thst')

#Birliklar ******************************************************************

@group_required('admin2')
def birlik(request):
    values = birliklar.objects.all()
    context = {
        'values': values,
        'titleown': 'Birliklar kiritish'
    }
    return render(request, '02_s_ad/08_0_birlik.html', context)

@group_required('admin2')

def addbirlik(request):    
    
    context = { 
        'values': request.POST,
        
        'titleown':'Birlik qo`shish'               
    }
    
    if request.method == 'GET':
        return render(request, '02_s_ad/08_1_addbirlik.html', context)
            
    if request.method == 'POST':  
        birlik = request.POST['birlik']
        asos = request.POST['asos']
        farq = request.POST['farq'] 

        birliklar.objects.create(owner=request.user, birlik=birlik, asos=asos, farq=farq)
        messages.success(request, 'Yangi birlik muvofaqqiyatli qo`shildi! ')
        return redirect('birlik')


@group_required('admin2')
def editbirlik(request, id):
    b = birliklar.objects.get(pk=id)
    context = {          
        'b': b,        
        'values': b
    }    
    
    if request.method == 'GET':  
        return render(request, '02_s_ad/08_2_editbirlik.html', context)
    
    if request.method == 'POST':  
        birlik = request.POST['birlik']
        asos = request.POST['asos']
        farq = request.POST['farq'] 
        
        b.birlik =birlik 
        b.asos =asos 
        b.farq =farq
        
        b.owner=request.user
        
        b.save()
        messages.success(request, 'Birlik muvofaqqiyatli yangilandi!')
        
        return redirect('birlik')

@group_required('admin2')
def delbirlik(request, id):
    yoqol = birliklar.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'Birlik muvofaqqiyatli o`chirildi')
    return redirect('birlik')

#Resurs ******************************************************************

@group_required('admin2')
def resurs(request):
    values = resurslar.objects.all()
    context = {        
        'values': values,
        'titleown': 'Resurslar'
    }
    return render(request, '02_s_ad/09_0_resurs.html', context)


@group_required('admin2')
def addresurs(request):
    birlik=birliklar.objects.all()
    yaxlit_all=yaxlitlash.objects.all()

    context = {             
        'birlik':birlik,
        'values': request.POST,
        
        'titleown': 'Resurs qo`shish',
        'yaxlit_all':yaxlit_all,
    }
    if request.method == 'GET':
        return render(request, '02_s_ad/09_1_addresurs 2.html', context)
            
    if request.method == 'POST':           
        
        nomi = request.POST['nomi']
        birlik = request.POST['birlik'] 
        
        tshy = request.POST['tshy']
        tne = request.POST['tne']
        gj = request.POST['gj']
        gkal = request.POST['gkal']
        yaxlit = request.POST['yaxlit']

        resurslar.objects.create(owner=request.user,nomi=nomi, birlik=birliklar(birlik),yaxlit=yaxlitlash(yaxlit),
                                 tshy=tshy,tne=tne,gj=gj, gkal=gkal)
        messages.success(request, 'Yangi resurs muvofaqqiyatli qo`shildi! ')
        return redirect('resurs') 
    

@group_required('admin2')
def editresurs(request, id):     
    r = resurslar.objects.get(pk=id)
    birlik=birliklar.objects.all()
    yaxlit_all=yaxlitlash.objects.all()

    context = {          
        'birlik': birlik,
        'r': r,        
        'values': r,
        'titleown': 'Resursni yangilash',
        'yaxlit_all':yaxlit_all,

    } 
    
    if request.method == 'GET':  
        return render(request, '02_s_ad/09_2_editresurs.html', context)
    
    if request.method == 'POST':  
        nomi = request.POST['nomi']
        birlik = request.POST['birlik'] 
        
        tshy = request.POST['tshy']
        tne = request.POST['tne']
        gj = request.POST['gj']
        gkal = request.POST['gkal']
        yaxlit = request.POST['yaxlit']
        
        r.nomi =nomi 
        r.birlik =birliklar(birlik)
        r.tshy=tshy
        r.tne=tne
        r.gj=gj
        r.gkal=gkal
        r.yaxlit=yaxlitlash(yaxlit)
        r.owner=request.user
        
        r.save()
        messages.success(request, 'Kattalik muvofaqqiyatli yangilandi!')
        
        return redirect('resurs')


@group_required('admin2')   
def delresurs(request, id):
    yoqol = resurslar.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'Resurs muvofaqqiyatli o`chirildi')
    return redirect('resurs')
#************______Foydalanuvchilar bo'yicha ma'lumotlar________________*********

@group_required('admin2')
def usersozlama(request):
    
    return render(request, '02_s_ad/10_1_sozlamalar.html')

#Valyuta bo'yicha ma'lumotlarni kiritish*********************

@group_required('admin2')
def valyuta(request):
    titleown='Valyuta'
    val = Valyuta.objects.filter(owner=request.user)
    
    context = {
        'val': val,
        'titleown':titleown
        }
    
    if request.method == 'GET':
        
        return render(request, '02_s_ad/11_0_valyuta.html', context)
    
    if request.method == 'POST':       
        
        return redirect('valyuta')
@group_required('admin2')
def addvalyuta(request):
    Valyuta.objects.create(owner=request.user, name='', somda=0, qiymati=0, checker=False)
    return redirect('valyuta')

@group_required('admin2')
def editvalyuta(request, id):
       
    val = Valyuta.objects.get(pk=id)    
    val.checker=False           
    val.save()    
    messages.success(request, 'Valyutani o`zgartirishingiz mumkin!')        
    return redirect('valyuta')

@group_required('admin2')
def savevalyuta(request, id):
    val = Valyuta.objects.get(pk=id)
    
    if request.method=="POST": 
        nom='nom'+str(id)
        som='som'+str(id)
        qiy='qiy'+str(id)
        
        val.name = request.POST[nom]
        val.somda = request.POST[som]
        val.qiymati = request.POST[qiy] 
        val.checker=True
        val.save()
        messages.success(request, 'Valyuta muvafaqqiyatli yangilandi!')        
    
    return redirect('valyuta')

@group_required('admin2')
def delvalyuta(request, id):
    davlat = Valyuta.objects.get(pk=id)    
    davlat.delete()
    messages.success(request, 'Valyuta o`chirildi')
    return redirect('valyuta')

@group_required('admin2')
def monitoring_users(request):

    fqir=allfaqir.objects.all()
    
    context={
        'titleown': 'Foydalanuvchilar ro`yxati',
        'fqir':fqir
    }
    return render(request, '02_s_ad/Monitoring/foydalanuvchi.html', context)

@group_required('admin2')
def passport(request,id):

    fqir=allfaqir.objects.all()
    foydalanuvchi = allfaqir.objects.get(pk=id)
    
    savol=savolnoma.objects.get(owner=foydalanuvchi.owner.id)

    savol1=""
    savol2=""
    if savol.savol1==True:
        savol1="checked"
    if savol.savol2==True:
        savol2="checked"
    
    context={
        "id":id,
        "active0": "active",
        "titleown": "Passport",

        'foydalanuvchi':foydalanuvchi,
        'savol':savol,
        'savol1':savol1,
        'savol2':savol2,

    }

    return render(request, '02_s_ad/Monitoring/02_passport.html', context)

@group_required('admin2')
def hisobot(request, id):

    foydalanuvchi = allfaqir.objects.get(pk=id)
    
    his = hisobot_item.objects.filter(owner=foydalanuvchi.owner.id)
    ist = istres.objects.filter(owner=foydalanuvchi.owner.id)


    context={
        "id":id,
        "active1": "active",
        "titleown": "Hisobot",

        'values':ist,
        'his':his
    }

    return render(request, '02_s_ad/Monitoring/03_hisobot.html', context)

@group_required('admin2')
def hisobot_check_monitoring(request, id, own_id):
    
    h_item=hisobot_item.objects.get(pk=id)
    
    h_ich=hisobot_ich.objects.filter(owner=h_item.owner.id, title=h_item.title)
    h_ist=hisobot_ist.objects.filter(owner=h_item.owner.id, title=h_item.title)
    h_uzat=hisobot_uzat.objects.filter(owner=h_item.owner.id, title=h_item.title)
    
    titleown=h_item.title+' oyi uchun ma`lumotlarni tekshirish'
    
    context ={
        "id":own_id,
        "del_id":id,

        "active1": "active",
        "titleown": "Hisobot",
        
        'h_item':h_item,
        'h_ich':h_ich,
        'h_ist':h_ist,
        'h_uzat':h_uzat,
        'titleown':titleown,
        'val':h_item        
    }


    return render(request, '02_s_ad/Monitoring/Hisobot/01_hisobot_check_monitoring.html', context)

@group_required('admin2')
def delhisobot(request, id, own_id):
    h_item=hisobot_item.objects.get(pk=id)
    
    h_ich=hisobot_ich.objects.filter(owner=h_item.owner.id, title=h_item.title)
    h_ist=hisobot_ist.objects.filter(owner=h_item.owner.id, title=h_item.title)
    h_uzat=hisobot_uzat.objects.filter(owner=h_item.owner.id, title=h_item.title)

    h_item.delete()
    for v in h_ich:
        v.delete()
    for v in h_ist:
        v.delete()
    for v in h_uzat:
        v.delete()
    
    messages.success(request, 'Davriy hisobot muvofaqqiyatli o`chirildi')
    
    url='hisobot_monitoring/'+str(own_id)
    next = request.POST.get('next', '/s_ad/'+url)
    
    return HttpResponseRedirect(next)


@group_required('admin2')
def tayyorlangan_hisobot(request, id):      
    fqir=allfaqir.objects.get(pk=id)

    his = hisobot_full.objects.filter(owner=fqir.owner_id)
    ist = istres.objects.filter(owner=fqir.owner_id)  

    context ={
    "id":id,
    "titleown": "Tayyorlangan hisobotlar",
    "active2": "active", 

    'values':ist,
    'his':his,   
    
    }


    return render(request, '02_s_ad/Monitoring/04_tayyorlangan_hisobotlar.html', context)


@group_required('admin2')
def tayyorlangan_result(request, id, tur, birl, own_id):      
    fqir=allfaqir.objects.get(pk=id)

    his = hisobot_full.objects.filter(owner=fqir.owner_id)
    ist = istres.objects.filter(owner=fqir.owner_id)  

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
                                koef2=j.qiymat
                            if birl == 'valut':
                                koef2=1000*j.qiymat*his.valyuta.qiymati/his.valyuta.somda
                            q=j.qiymat_pul*koef2/1000000
                        
                        obj[r].append(float('{0:.2f}'.format(float(q))))
                        
            else:
                obj[r].append(0)
        
    context={        
        "id":own_id,
        "titleown": "Tayyorlangan hisobotlar",
        "active2": "active", 
        'titleown':his.nomi,
       'his':his,
       'obj':obj,
       'sana':sana,
       'res_id':res_id,
       'birl':birl,
       'tur1':tur,
       
       'activecha1':active1,
       'activecha2':active2,
       'activecha3':active3,
    }   

    return render(request, '02_s_ad/Monitoring/Hisobot/02_tayyorlangan_hisobot_result.html', context)

@group_required('admin2')
def deltayyorlangan_hisobot(request, id, own_id):  

    his = hisobot_full.objects.get(pk=id)
    
    his.delete()
    
    messages.success(request, 'Muvofaqqiyatli o`chirildi')
    
    url='tayyorlangan_hisobot/'+str(own_id)
    next = request.POST.get('next', '/s_ad/'+url)

    return HttpResponseRedirect(next)

#***************Tashkiliy tadbirlar*************************
@group_required('admin2')
def Tadbirlar(request):
    titleown='Texnik tadbirlar'
    tadbir=Tadbir.objects.all()
    context = {
        'titleown':titleown,
        'tadbir':tadbir
    }

    return render(request, '02_s_ad/Tadbirlar/0_tadbirlar.html',context)

@group_required('admin2')
def addtadbir(request):
    titleown='Texnik tadbirlar qo`shish'
    context = {
        'titleown':titleown
    }
    if request.method == 'GET':
        return render(request, '02_s_ad/Tadbirlar/1_addtadbir.html', context)
            
    if request.method == 'POST':        
        tadbir_kodi = request.POST['tadbir_kodi']
        tadbir_nomi = request.POST['tadbir_nomi']        
        
        Tadbir.objects.create(owner=request.user, kodi=tadbir_kodi, nomi=tadbir_nomi )        
        messages.success(request, 'Yangi tashkiliy texnik tadbir muvofaqqiyatli qo`shildi! ')
        return redirect('Tadbirlar')

@group_required('admin2')
def edittadbir(request, id):
    
    titleown='O`zgartirish'
    tadbir = Tadbir.objects.get(pk=id)
    
    context = {
        'tadbir': tadbir,
        'titleown':titleown
    } 
    
    if request.method == 'GET':        
        return render(request, '02_s_ad/Tadbirlar/2_edittadbir.html', context)
    
    if request.method =='POST':
        tadbir_kodi = request.POST['tadbir_kodi']
        tadbir_nomi = request.POST['tadbir_nomi']  
        
        tadbir.kodi=tadbir_kodi
        tadbir.nomi=tadbir_nomi
        tadbir.owner=request.user
        
        tadbir.save()        
        messages.success(request, 'Texnik tadbir muvofaqqiyatli yangilandi! ')
        
        return redirect('Tadbirlar')

@group_required('admin2')
def deltadbir(request, id):          
    tadbir = Tadbir.objects.get(pk=id)
    tadbir.delete()
    messages.success(request, 'Texnik tadbir muvofaqqiyatli o`chirildi')
    return redirect('Tadbirlar')

#yaxlitlash bo'yicha ma'lumotlarni kiritish*********************

@group_required('admin2')
def yaxlitlashV(request):
    titleown='Yaxlitlash birliklari'
    val = yaxlitlash.objects.all()
    
    context = {
        'val': val,
        'titleown':titleown
        }
    
    if request.method == 'GET':
        
        return render(request, '02_s_ad/12_0_yaxlitlash.html', context)
    
    if request.method == 'POST':       
        
        return redirect('yaxlitlashV')

@group_required('admin2')
def addyaxlitlash(request):
    yaxlitlash.objects.create(owner=request.user, nomi='', qiymati=0, checker=False)
    return redirect('yaxlitlashV')

@group_required('admin2')
def edityaxlitlash(request, id):
       
    val = yaxlitlash.objects.get(pk=id)    
    val.checker=False           
    val.save()    
    messages.success(request, 'Yaxlitlanuvchi qiymatni o`zgartirishingiz mumkin!')        
    return redirect('yaxlitlashV')

@group_required('admin2')
def saveyaxlitlash(request, id):
    val = yaxlitlash.objects.get(pk=id)
    
    if request.method=="POST": 
        nomi='nomi'+str(id)
        qiymati='qiymati'+str(id)
        
        val.nomi = request.POST[nomi]
        val.qiymati = request.POST[qiymati] 
        val.checker=True
        val.save()
        messages.success(request, 'Yaxlitlanuvchi qiymat muvafaqqiyatli saqlandi!')        
    
    return redirect('yaxlitlashV')

@group_required('admin2')
def delyaxlitlash(request, id):
    val = yaxlitlash.objects.get(pk=id)    
    val.delete()
    messages.success(request, 'Yaxlitlanuvchi qiymat muvafaqqiyatli o`chirildi')
    return redirect('yaxlitlashV')