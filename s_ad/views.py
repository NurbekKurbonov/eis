from django.contrib import messages

from django.shortcuts import render, redirect
from kirish.models import sahifa
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import davlatlar


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
    sah = sahifa.objects.get(pk=id)
    
    context = {
        'sah': sah,
        'values': sah
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
    dav = davlatlar.objects.filter(owner=request.user)
    
    context = {
        'dav': dav
        }
    
    return render(request, '02_s_ad/02_0_davlat.html', context)

def adddavlat(request):
    
    if request.method == 'GET':
        return render(request, '02_s_ad/02_1_adddavlat.html')
            
    if request.method == 'POST':        
        davlat_kodi = request.POST['davlat_kodi']
        davlat_nomi = request.POST['davlat_nomi']        
        
        davlatlar.objects.create(owner=request.user, davlat_kodi=davlat_kodi, davlat_nomi=davlat_nomi )        
        messages.success(request, 'Yangi davlat muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('davlat')