from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):   
    return render(request, 'index.html')
def home(request):
    return HttpResponse('this is home section')

def office(request):
    return HttpResponse('This page is dedicated to official matterials')
