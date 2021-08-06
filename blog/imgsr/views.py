from django.shortcuts import render
from django.http import HttpResponse
# Creae your views here.
def home(request):
    return render(request,'base.html')
