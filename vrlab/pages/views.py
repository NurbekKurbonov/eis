from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
#from django.http import HttpResponseRedirect

from .models import Page, Book, Section, Subject, Test, Savol, Javob
from .forms import ContactForm

def contact(request):
  submitted = False
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid:
      #cd = form.cleaned_data
      #assert False
      return HttpResponseRedirect("/contact?submitted=True")
  else:
    form = ContactForm()
    if 'submitted' in request.GET:
      submitted = True

  return render(request, 'contact.html', {'form':form, 'page_list':Page.objects.all(), 'submitted':submitted})


def index(request):
  
  kitob=Book.objects.all()
  title = {}  
  for i in reversed(kitob):
    title[i.id]=''
    if len(i.nomi)>12:
      title[i.id] = str(i.nomi)[:13]+'...'
    else:
      title[i.id] = str(i.nomi)

  context={
    'kitob':kitob,
    'nomi':title,
  }
  return render(request, 'index.html', context)

def kitob(request, id):  
  book=Book.objects.get(pk=id)
  bob=book.section.all()
  
  context={
    'kitob':book,  
    'bob':bob,
  }

  return render(request, '00_0_home.html', context)

def theme(request, id):
  M=Subject.objects.get(pk=id)
  
  context={
    'M':M,
  }  
  
  return render(request, '00_1_mavzu.html', context)

def test(request):
  
  return render(request, 'test.html')

#===============Virtual lab===========================

def vrlab(request):
  return render(request, 'vrlab.html')

#1-lab
def lab1(request):
  return render(request, 'lab1.html')

def lab1_result(request):
  return render(request, 'lab1_result.html')

#2-lab
def lab2(request):
  return render(request, 'lab2.html')

def lab2_result(request):
  return render(request, 'lab2_result.html')

def lab3(request):
  return render(request, 'lab3.html')