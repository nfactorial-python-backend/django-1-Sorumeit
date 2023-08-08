from django.shortcuts import render
from django.http import HttpResponse
def home(request):
	return HttpResponse('<h1>Hello, nfactorial school!</h1>')
 
def sum(request , first : int , second : int ):
	return HttpResponse('<h1> {{ first + second }} </h1>')
