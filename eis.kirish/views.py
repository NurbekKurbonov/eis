from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import sahifa, savolnoma
from .forms import ContactForm
import foydalanuvchi

from django.http import JsonResponse


#login_____*********************************************/

def loginP(request):
    return render(request, '01_auth/01_login.html')

#Regisration **********************************************************
class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'foydalanuvchi nomi faqat harflardan tashkil topishi lozim'}, status=400)        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Foydalanilgan, boshqa tanlang'}, status=409)
        return JsonResponse({'username_valid': True})
    
class registerP(request):
    def get(self, request):
        
        return render(request, '01_auth/02_register.html')
    
# END Regisration *****************************************************

def xato500(request):
    return render(request, '01_auth/04_Xato_500.html')

def resetpas(request):
    return render(request, '01_auth/05_reset.html')

#Asosiy qism_____*********************************************/

def kirish(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(sahifa, permalink=pagename)  
    
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list':sahifa.objects.all(),        
    }
        
    return render(request, '00_kirish/01_index.html', context)

def index(request):
    typem="danger"
    context = {
        'typem':typem
    }
    return render(request, '00_kirish/01_index.html', context)

#Contanct form ***************************************************/

def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form=ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form':form,
        'page_list':sahifa.objects.all(),
        'submitted':submitted
    }
    return render(request, '00_kirish/02_contact.html' )

#QUIZ***************************************************************
def savol(request):
    if request.method=="GET":
        return render(request, '01_auth/06_savolnoma.html' )
    
    if request.method=="POST":
        savol1=request.POST['savol1']
        savol2=request.POST['savol2']
        
        savolnoma.objects.create(
            owner=request.user,
            savol1=savol1,
            savol2=savol2
        )
        messages.success(request, 'EIS sistemasiga xush kelibsiz! :)')
        return redirect('home')