from django.contrib import messages

from django.shortcuts import render, redirect
from kirish.models import sahifa
from datetime import date

def kirishP(request):
    title='Kirish bo`limi'
    context = {
        'title':title
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
        
        title = request.POST['title']
        permalink = request.POST['permalink']
        update_date = "2020-6-12 7:38"
        bodytext = request.POST['bodytext']
        icon = request.POST['icon'] 
        
        sahifa.objects.create(owner=request.user, title=title, permalink=permalink, update_date=update_date, bodytext=bodytext, icon=icon)
        messages.success(request, 'Yangi sahifa muvofaqqiyatli qo`shildi! Rahmat! Charchamang! :)')
        return redirect('kirishP')
    
def icons(request):
    return render(request, 'partials/01_icons.html')