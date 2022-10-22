from django.shortcuts import render
from quiz.models import Exam

# Create your views here.

def home(request):
    exam = Exam.objects.all()
    return render(request,"index.html",{"exam":exam})
