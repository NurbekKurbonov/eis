from django.contrib import messages

from django.shortcuts import render, redirect
from kirish.models import sahifa
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from .models import davlatlar, viloyatlar, tumanlar, IFTUM, DBIBT,THST, birliklar, resurslar

def icons(request):
    return render(request, 'partials/01_icons.html')
#kirish qismini to'ldirish *********************************
def kirishP(request):
    title='Kirish bo`limi'
    
    sah = sahifa.objects.filter(owner=request.user)    
    paginator = Paginator(sah, 4)    
    page_number=request.GET.get('page')
    page_obj=Paginator.get_page(paginator, page_number)
    
    context = {
        'title':title,
        'sah':sah,
        'page_obj':page_obj
    }
    return render(request, '02_s_ad/01_0_kirishP.html', context)


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
        messages.success(request, 'Yangi sahifa muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('kirishP')

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
        messages.success(request, 'sahifa muvofaqqiyatli yangilandi! Rahmat! Charchamang! :)')
        
        return redirect('kirishP')

def delkir(request, id):
    sah = sahifa.objects.get(pk=id)
    sah.delete()
    messages.success(request, 'Sahifa muvofaqqiyatli o`chirildi')
    return redirect('kirishP')

#Hududlar bo'yicha ma'lumotlarni kiritish*********************

def davlat(request):
    titleown='Davlatlar'
    dav = davlatlar.objects.filter(owner=request.user)
    
    context = {
        'dav': dav,
        'titleown':titleown
        }
    
    return render(request, '02_s_ad/02_0_davlat.html', context)

def adddavlat(request):
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
        messages.success(request, 'Yangi davlat muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('davlat')

def editdavlat(request, id):
       
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

def deldavlat(request, id):
    davlat = davlatlar.objects.get(pk=id)
    davlat.delete()
    messages.success(request, 'Davlat muvofaqqiyatli o`chirildi')
    return redirect('davlat')

#viloyat*********************************
def viloyat(request):
    vil = viloyatlar.objects.all()
    titleown = 'Viloyatlar'
    context = {
        'vil': vil,
        'titleown':titleown
    }
    return render(request, '02_s_ad/03_0_viloyat.html', context)

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
        
        viloyatlar.objects.create(owner=request.user, viloyat_davlati=viloyat_davlati, viloyat_kodi=viloyat_kodi, viloyat_nomi=viloyat_nomi)        
        messages.success(request, 'Yangi viloyat muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('viloyat')
    
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
        vil.viloyat_davlati=viloyat_davlati
        vil.viloyat_nomi=viloyat_nomi
        vil.viloyat_kodi=viloyat_kodi
        
        vil.save()
        messages.success(request, 'Davlat muvofaqqiyatli yangilandi!')
        
        return redirect('viloyat')

def delviloyat(request, id):
    yoqol = viloyatlar.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'Viloyat o`chirildi')
    return redirect('viloyat')

#tuman****************************************************

def tuman(request):
    
    tum = tumanlar.objects.all()
    
    context = {
        'tum': tum,
        'titleown':'Tumanlar'
    }
    return render(request, '02_s_ad/04_0_tuman.html', context)

def addtuman(request):           
    
    vil = viloyatlar.objects.all()
    dav = davlatlar.objects.all()  
    
    context = {    
        'dav': dav,           
        'vil': vil,
        'values': request.POST   ,        
        
        'titleown':'yangi tumanlar qo`shish'             
        
    }
    
    if request.method == 'GET':
        return render(request, '02_s_ad/04_1_addtuman.html', context)
            
    if request.method == 'POST':  
        tuman_davlati = request.POST['tuman_davlati']
        tuman_viloyati = request.POST['tuman_viloyati']
        tuman_kodi = request.POST['tuman_kodi']        
        tuman_nomi = request.POST['tuman_nomi']
        
        tumanlar.objects.create(owner=request.user, tuman_davlati =tuman_davlati, tuman_viloyati = tuman_viloyati, tuman_kodi = tuman_kodi, tuman_nomi = tuman_nomi)
        messages.success(request, 'Yangi tuman muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('tuman')
    
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
        tuman.tuman_davlati=tuman_davlati
        tuman.tuman_viloyati = tuman_viloyati
        tuman.tuman_kodi = tuman_kodi 
        tuman.tuman_nomi = tuman_nomi
        
        
        tuman.save()
        messages.success(request, 'Tuman muvofaqqiyatli yangilandi!')
        
        return redirect('tuman')

def deltuman(request, id):
    yoqol = tumanlar.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'Tuman muvofaqqiyatli o`chirildi')
    return redirect('tuman')

#***_________KODLAR__________**********************************************

def iftums(request):
    iftum = IFTUM.objects.all()
    context = {
        'iftum': iftum,
        'titleown':'IFTUM'
    }
    return render(request, '02_s_ad/05_0_iftum.html', context)

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
        messages.success(request, 'Yangi IFTUM kodi muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('iftums')

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

def deliftums(request, id):
    yoqol = IFTUM.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'IFTUM kodi muvofaqqiyatli o`chirildi')
    return redirect('iftums')

#DBIBT******************************************************************

def dbibt(request):
    dbibts=DBIBT.objects.all()
    
    context={
        'val':dbibts,
        'titleown':'DBIBT kodi'
    }
    return render(request, '02_s_ad/06_0_dbibt.html', context)

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
        messages.success(request, 'Yangi DBIBT kodi muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('dbibt')

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

def deldbibt(request, id):
    yoqol = DBIBT.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'DBIBT kodi muvofaqqiyatli o`chirildi')
    return redirect('dbibt')

#TASHKIL-HUQUQIY SHAKLLARI TASNIFI. ******************************************************************

def thst(request):
    ths=THST.objects.all()
    
    context={
        'val':ths,
        'titleown':'THSHT kodi'
    }
    return render(request, '02_s_ad/07_0_thsht.html', context)

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
        messages.success(request, 'Yangi THSHT kodi muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('thst')

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

def delthst(request, id):
    yoqol = THST.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'THSHT kodi muvofaqqiyatli o`chirildi')
    return redirect('thst')

#Birliklar ******************************************************************

def birlik(request):
    values = birliklar.objects.all()
    context = {
        'values': values,
        'titleown': 'Birliklar kiritish'
    }
    return render(request, '02_s_ad/08_0_birlik.html', context)

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
        messages.success(request, 'Yangi birlik muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('birlik')

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

def delbirlik(request, id):
    yoqol = birliklar.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'Birlik muvofaqqiyatli o`chirildi')
    return redirect('birlik')

#Resurs ******************************************************************
def resurs(request):
    values = resurslar.objects.all()
    context = {
        'values': values,
        'titleown': 'Resurslar'
    }
    return render(request, '02_s_ad/09_0_resurs.html', context)

def addresurs(request):
    birlik=birliklar.objects.all()
    context = {             
        'birlik':birlik,
        'values': request.POST,
        
        'titleown': 'Resurs qo`shish'
    }
    if request.method == 'GET':
        return render(request, '02_s_ad/09_1_addresurs 2.html', context)
            
    if request.method == 'POST':           
        
        nomi = request.POST['nomi']
        birlik = request.POST['birlik'] 

        resurslar.objects.create(owner=request.user,nomi=nomi, birlik=birlik)
        messages.success(request, 'Yangi resurs muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('resurs') 

def editresurs(request, id):     
    r = resurslar.objects.get(pk=id)
    birlik=birliklar.objects.all()
    
    context = {          
        'birlik': birlik,
        'r': r,        
        'values': r,
        'titleown': 'Resursni yangilash'
    } 
    
    if request.method == 'GET':  
        return render(request, '02_s_ad/09_2_editresurs.html', context)
    
    if request.method == 'POST':  
        nomi = request.POST['nomi']
        birlik = request.POST['nomi'] 
        
        r.nomi =nomi 
        r.birlik =birlik 
        
        r.owner=request.user
        
        r.save()
        messages.success(request, 'Kattalik muvofaqqiyatli yangilandi!')
        
        return redirect('kattalik')
    
def delresurs(request, id):
    yoqol = resurslar.objects.get(pk=id)
    yoqol.delete()
    messages.success(request, 'Resurs muvofaqqiyatli o`chirildi')
    return redirect('resurs')

#************______Foydalanuvchilar bo'yicha ma'lumotlar________________*********

def usersozlama(request):
    
    return render(request, '02_s_ad/10_1_sozlamalar.html')

#Valyuta bo'yicha ma'lumotlarni kiritish*********************

def valyuta(request):
    titleown='Davlatlar'
    dav = davlatlar.objects.filter(owner=request.user)
    
    context = {
        'dav': dav,
        'titleown':titleown
        }
    
    return render(request, '02_s_ad/11_0_valyuta.html', context)

def addvalyuta(request):
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
        messages.success(request, 'Yangi davlat muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('davlat')

def editvalyuta(request, id):
       
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

def delvalyuta(request, id):
    davlat = davlatlar.objects.get(pk=id)
    davlat.delete()
    messages.success(request, 'Davlat muvofaqqiyatli o`chirildi')
    return redirect('davlat')