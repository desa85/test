from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>Hello world</11>")
# Create your views here.
