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
    
    tilID=0
    for i in tillar:
        if i.nomi==til:
            tilID=i.id

    jumlalar=jumla.objects.all()
    tarjima=Tarjima.objects.filter(til=tilID)
    tarjimon=Tarjimon.objects.all()
    
    st={}
    for i in jumlalar:    
        st[i]=False
        if tarjimon.filter(nomi=i.id).exists():
            tarjimalari=tarjimon.get(nomi=i.id)
            for k in tarjimalari.tarjimasi.all():
                if k.til.id==tilID:
                    st[i]=tarjima.get(pk=k.id)         
                   
                
    context={
        'tillar':tillar,
        'til':til,
        'jumlalar':jumlalar,
        'tarjima':tarjima,      
        'st'  :st,
    }

    return render(request, 'tarjimon/Tillar/tarjima.html',context)