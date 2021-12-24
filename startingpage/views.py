from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib import messages

def index(request):
    return render(request, 'startingpage/index.html')