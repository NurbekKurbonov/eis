from django.shortcuts import render

#login_____*********************************************/

def loginP(request):
    return render(request, '01_auth/01_login.html')

def registerP(request):
    return render(request, '01_auth/02_register.html')

def xato404(request):
    return render(request, '01_auth/03_Xato_404.html')

def xato500(request):
    return render(request, '01_auth/04_Xato_500.html')

def resetpas(request):
    return render(request, '01_auth/05_reset.html')

#Asosiy qism_____*********************************************/

def kirish(request):
    return render(request, '00_kirish/00_base.html')