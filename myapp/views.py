from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):   
    context = {'name':'ahsan','types':'student'}
    return render(request, 'index.html',context)
def home(request):
    return render(request,'home.html')

def office(request):
    return render(request,'office.html')
