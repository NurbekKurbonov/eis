from django.shortcuts import render

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

from .models import Til, Tarjima, jumla, Tarjimon
from .til_formulas import tilID
from django.core.files.storage import FileSystemStorage

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

@group_required('Tarjimon')
def bosh_sahifa(request):
    tillar=Til.objects.filter(tarjimonlar=request.user)
    context={
        'tillar':tillar,
    }
    return render(request, 'tarjimon/bosh_sahifa/00_bosh_sahifa_tarjimon.html',context)

@group_required('Tarjimon')
def tarjima(request, til):    
    tillar=Til.objects.filter(tarjimonlar=request.user)   
    jumlalar=jumla.objects.all()
    tarjima=Tarjima.objects.filter(til=tilID(tillar, til))
    tarjimon=Tarjimon.objects.all()
    
    st={}
    for i in jumlalar:    
        st[i]=False
        if tarjimon.filter(nomi=i.id).exists():
            tarjimalari=tarjimon.get(nomi=i.id)
            for k in tarjimalari.tarjimasi.all():
                if k.til.id==tilID(tillar, til):
                    st[i]=tarjima.get(pk=k.id)         
                   
                
    context={
        'tillar':tillar,
        'til':til,
        'jumlalar':jumlalar,
        'tarjima':tarjima,      
        'st'  :st,
    }

    return render(request, 'tarjimon/Tillar/tarjima.html',context)

@group_required('Tarjimon')
def tarjimon(request,id, til):    
    tillar=Til.objects.filter(tarjimonlar=request.user)
    
    if id==0:
        jumlalar=jumla.objects.create(nomi='',owner=request.user)
    else:
        jumlalar=jumla.objects.get(pk=id)
    
    tarjima=Tarjima.objects.filter(til=tilID(tillar, til))
    
    if not Tarjimon.objects.filter(nomi=jumlalar.id).exists():
        Tarjimon.objects.create(nomi=jumlalar)

    tarjimon=Tarjimon.objects.get(nomi=jumlalar.id)
    
    tarjimasi=''
    for i in tarjimon.tarjimasi.all():
        if i.til.id==tilID(tillar, til):
                    tarjimasi=tarjima.get(pk=i.id)
    if tarjimasi=='':
            tarjimasi=Tarjima.objects.create(
                nomi='', til=Til(pk=tilID(tillar, til)),
                owner=request.user
            )

    if request.method=="GET":
        context={
            'tillar':tillar,
            'til':til,
            'jumlalar':jumlalar,
            'tarjimasi':tarjimasi,
        }
        return render(request, 'tarjimon/Tillar/01_tarjima.html',context)
    if request.method=="POST":
        jumlalar.nomi=request.POST['jumla']
        jumlalar.save()
        tarjima=request.POST['tarjimasi']

        tarjimasi.nomi=tarjima
        tarjimasi.save()
        tarjimon.tarjimasi.add(tarjimasi.id)
        tarjimon.save()

        messages.success(request, 'Amaliyot muvofaqqiyatli bajarildi')
        url='tarjima/'+str(til)
        next = request.POST.get('next', '/tarjimon/'+url)            
        return HttpResponseRedirect(next)


def deltarjima(request,id):
    tarjimon=Tarjimon.objects.get(pk=id)
    tarjimon.nomi.delete()
    for i in tarjimon.tarjimasi.all():
        i.delete()
        
    tarjimon.delete()
    messages.success(request, 'Amaliyot muvofaqqiyatli bajarildi')                
    return redirect('tarjimon_s_ad')

def addtil(request):
    titleown='Til qo`shish'
    tarjimonlar=User.objects.all()
    
    if request.method=="GET":
        context = {            
            'tarjimonlar':tarjimonlar,
            }        
        return render(request, '02_s_ad/tarjimon/02_addtil.html', context)
    
    if request.method=="POST":
        nomi=request.POST['til']     
        
        til=Til.objects.create(
            nomi=nomi
        ) 
        
        if request.FILES.get('bay', False):                      
            by = request.FILES['bay']
            til.bayroq=by
            til.save()
        
        tarjimonlari=request.POST.getlist('tarjimonlari')        
        for i in tarjimonlari:
            til.tarjimonlar.add(User.objects.get(pk=int(i)))
        
        messages.success(request, str(til.nomi)+' muvofaqqiyatli qo`shildi')
        return redirect('tarjimon_s_ad')

def edittil(request,id):
    
    tillar=Til.objects.get(pk=id)
    tarjimonlar=User.objects.all()
    
    if request.method=="GET":
        context = {            
            'tillar':tillar,
            'id':id,
            'tarjimonlar':tarjimonlar,
            }        
        return render(request, '02_s_ad/tarjimon/03_edittil.html', context)
    
    if request.method=="POST":
        nomi=request.POST['til']

        tarjimonlari=request.POST.getlist('tarjimonlari')        
        for i in User.objects.all():
            tillar.tarjimonlar.remove(i)

        for i in tarjimonlari:
            tillar.tarjimonlar.add(User.objects.get(pk=int(i)))
        
        messages.success(request, str(tillar.nomi)+' muvofaqqiyatli qo`shildi')
        return redirect('tarjimon_s_ad')

def deltil(request, id):
    til=tillar=Til.objects.get(pk=id)
    til.delete()

    messages.success(request, str(til.nomi)+' muvofaqqiyatli o`chirildi')
    return redirect('tarjimon_s_ad')

def tr(uz, til):
    for i in jumla.objects.all():
        if i.nomi == uz:
            tarjima=Tarjimon.objects.get(pk=i.id)

    for i in tarjima.tarjimasi.all():
        if i.til.nomi==til:
            tarjima = i.nomi
    
    return tarjima
