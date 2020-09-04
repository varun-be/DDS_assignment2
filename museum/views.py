from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellow world, you are in the online ships museum")