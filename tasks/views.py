from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("WelCome!!")

def contact(request):
    return HttpResponse("This Is Contact!!")

def support(request):
    return HttpResponse("This Is Support Page")