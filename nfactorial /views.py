from django.shortcuts import render
from django.http import HttpResponse
def home(request):
	return HttpResponse('<h1>Hello, nfactorial school!</h1>')
 
def sum(request , first : int , second : int ):
	sum1 = first + second
	return HttpResponse( sum1 )

def up( request , text : str ):
	return HttpResponse( text.upper() )

def pal( request , word : str ):
	new = word
	return HttpResponse( word == new.reverse(  ) )
