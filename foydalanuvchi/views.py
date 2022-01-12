from django.shortcuts import render

# Create your views here.
def sozlama(request):
    return render(request, '03_foydalanuvchi/00_base.html')