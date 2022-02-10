from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages

from django.views import View
import json
from django.contrib.auth.models import User
from django.contrib import auth
from validate_email import validate_email
from django.core.mail import EmailMessage

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site

from django.urls import reverse
from .utils import account_activation_token

from .models import sahifa, savolnoma
from foydalanuvchi.models import allfaqir

from s_ad.models import IFTUM, THST, DBIBT, davlatlar, viloyatlar, tumanlar
from .forms import ContactForm
import foydalanuvchi
from foydalanuvchi.models import allfaqir

from django.contrib.auth.models import Group
from .forms import captchaform

from django.core.files.storage import FileSystemStorage

#from foydalanuvchi.views import

#registratsya**************************************************
class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        last=email[-9:]        
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email xato'}, status=400)
        
        #if last !='@umail.uz':
        #    return JsonResponse({'email_error': 'umail.uz bo`lishi lozim'}, status=401)
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Uzur, ushbu email foydalanilgan, parolni unutgan bo`lsangiz, tiklash bo`limiga o`ting'}, status=409)
        return JsonResponse({'email_valid': True})
    
class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'foydalanuvchi nomi faqat harf-raqamli belgilarni o`z ichiga olishi kerak'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Kechirasiz, ushbu nom foydalanilgan, boshqa nom tanlang  '}, status=409)
        return JsonResponse({'username_valid': True})    

class StirValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        stir = data['stir']
        
        if len(stir)!=9:
            return JsonResponse({'stir_error': 'STIR raqami noto`g`ri'}, status=400)
        
        boshi=int(stir[:1])        
        if boshi>3:
            if boshi<7:
                return JsonResponse({'stir_error': 'Sistema hozircha faqat yuridik shaxslarni qabul qiladi'}, status=401)
            return JsonResponse({'stir_error': 'STIR yuridik shaxsga tegishli emas'}, status=400)            
        
        return JsonResponse({'stir_valid': True})    

class passwordValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        password = data['password']
        
        if len(password)<8:
            return JsonResponse({'password_error': 'parol 8 ta belgidan ko`p bo`lishi kerak. masalan:pArol12#'}, status=400)
        
        if str(password).isalnum():
            return JsonResponse({'password_error': 'Kamida belgi qatnashishi kerak'}, status=400)                    
        
        lst=list(str(password))
        if any(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in lst) is False:
            return JsonResponse({'password_error': 'Kamida bitta harf katta bo`lishi kerak'}, status=409)
        
        return JsonResponse({'password_valid': True})    
    
class registerP(View):
    def get(self, request):       
        
        return render(request, '01_auth/02_register.html')
    
    def post(self, request):
        stir=request.POST['stir']
        
        username=request.POST['username']
        email=request.POST['email']        
        password = request.POST['password']
        context = {
            'fieldValues': request.POST,
            'captchaform': captchaform
        }
        
        if str(password).isalnum():
            messages.error(request, 'Parolga kamida bitta belgi qatnashishi lozim')
            return render(request, '01_auth/02_register.html', context)
        
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if not User.objects.filter(password=password).exists():
                    user=User.objects.create_user(username=username, email=email)
                    user.set_password(password)
                    faqir = Group.objects.get(name='Faqirlar') 
                    faqir.user_set.add(user)
                    
                    user.is_active = False                    
                    user.save()         
                               
                    #korxona tayyorlash:
                    allfaqir.objects.create(owner=user, inn=stir, savol1=False, savol2=False)
                    
                    #************************************************                   
                        
                    current_site = get_current_site(request)
                    email_body = {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                        }
                    link = reverse('activate', kwargs={
                               'uidb64': email_body['uid'], 'token': email_body['token']})
                    
                    email_subject = 'Sistemaga kirish uchun faol qilish'
                    activate_url = 'http://'+current_site.domain+link                   
                    
                    email=EmailMessage(
                                email_subject,
                                'Hurmatli '+user.username+'!\n\n Iltimos quyidagi havola orqali akkauntingizni faollashtiring:\n\n'+
                                    'Уважаемый ' + user.username + '!\n\n Пожалуйста, активируйте свой аккаунт по следующей ссылке: \n'+
                                    'Dear ' + user.username + '!\n\n Please activate your account using the following link: 👇🏻👇🏻👇🏻\n\n\n'+activate_url,
                                'noreply.nurbek.kurbonov@nur.uz',                                
                                [email],
                            )
                    email.send(fail_silently=False)
                    
                    messages.success(request, 'Foydalanuvchi muvafaqqiyatli sistemaga qo`shildi! Iltimos, pochtangiz orqali faollashtiring')
                    return redirect('loginP')
        return render(request, '01_auth/02_register.html', {'captchaform': captchaform})

class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                messages.success(request, 'Assalomu aleykum '+user.username+'! Sizning sahifangiz allaqachon faollashtirilgan, marhamat sistemaga kirishingiz mumkin')
                return redirect('loginP')

            if user.is_active:                
                return redirect('loginP')
            
            user.is_active = True
            user.save()
            
            messages.success(request, 'Assalomu aleykum!'+user.username+' sahifangiz muvafaqqiyatli faollashtirildi')
            return redirect('loginP')

        except Exception as ex:
            pass
        messages.success(request, 'Xatolik, Ushbu noto`g`ri token bilan kirdingiz')
        return redirect('loginP')
    
#login_____*********************************************/

class loginP(View):
    def get(self, request):
        return render(request, '01_auth/01_login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        if username and password:
            user = auth.authenticate(username=username, password=password)
            
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Assalomu alaykum '+user.username+' EIS sistemasiga xush kelibsiz!')                    
                    return redirect('home')
                messages.error(request, 'Foydalanuvchi faollashtirilmagan! iltimos emailingizni tekshiring va faollashtiring')
            messages.error(request, 'Login yoki parol xato, iltimos qayta urinib ko`ring!')
            return render(request, '01_auth/01_login.html')
        
        messages.error(request, 'Iltimos so`ralgan ma`lumotlarni to`ldiring')
        return render(request, '01_auth/01_login.html')

class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'Siz sistemadan chiqdingiz! Salomat bo`ling')
        return redirect('loginP')
    
#**************************************************************   
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
        
        iftum=IFTUM.objects.all()
        thst=THST.objects.all()
        dbibt=DBIBT.objects.all()
        dav=davlatlar.objects.all()
        vil=viloyatlar.objects.all()
        tum=tumanlar.objects.all() 
        
        context={
            'iftum':iftum,
            'thst':thst,
            'dbibt':dbibt,
            'dav': dav,
            'vil':vil,
            'tum':tum,
        }
        return render(request, '01_auth/06_savolnoma.html', context)
    
    if request.method=="POST":        
        nomi=request.POST['nomi']        
        
        ism=request.POST['ism']
        fam=request.POST['fam']
        tel=request.POST['tel']
        iftum=request.POST['iftum']
        dbibt=request.POST['dbibt']
        thst=request.POST['thst']
        mobil=request.POST['mobil']
        dav=request.POST['dav']
        vil=request.POST['vil']
        
        emb=request.FILES['emblem']   
        print(emb.name,' ', emb.size)
        tuman=request.POST['tuman']
        manzil=request.POST['manzil']
        
        savol1=request.POST['savol1']
        savol2=request.POST['savol2']
        
        allf=allfaqir.objects.get(owner=request.user)
        allf.nomi=nomi
        allf.iftum=IFTUM(iftum)
        
        allf.dbibt=DBIBT(dbibt) 
        allf.thst=THST(thst)
        
        allf.mobil=mobil
        allf.tel=tel
        
        allf.dav=davlatlar(dav)
        allf.vil=viloyatlar(vil)
        allf.tum=tumanlar(tuman)
        
        allf.manzil=manzil
        allf.emblem=emb   
        
        fs = FileSystemStorage().save(emb)
          
        allf.save()
           
        savolnoma.objects.create(
            owner=request.user,
            
            savol1=savol1,
            savol2=savol2
        )
        messages.success(request, 'EIS sistemasiga xush kelibsiz! :)')
        return redirect('home')
    
def view404(request):
    return render(request, '404.html')


