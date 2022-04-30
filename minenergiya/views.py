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

#modelsdan chaqirish******************
#from s_ad.models import resurslar, Valyuta
#from .models import ichres, istres, sotres, hisobot_item, hisobot_ich, hisobot_ist, hisobot_uzat, allfaqir, hisobot_full, his_ich
#from kirish.models import savolnoma

def home(request):
    context={
        
    }
    return render(request, '04_minenergiya/00_0_home.html', context)

def tahlil(request):
    context={
        
    }
    return render(request, '04_minenergiya/02_0_tahlil.html', context)