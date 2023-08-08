from django.shortcuts import render

from django.http import HttpResponse
def home(request):
	return HttpResponse('<h1>Главная</h1>')
 
def sum(request , first : int , second : int ):
	first += second
	return HttpResponse( first )

def up(request , text : str):
	return HttpResponse( text.upper() )

def pal(request , word : str ):
	return HttpResponse( word == word[::-1] )

def calc( request , first : int , operation : str , second : int ):
	if ( operation == "add" ):
        return HttpResponse( first + second )	
    if ( operation == "sub" ):
	    return HttpResponse( first - second )
	if ( operation == "mult" ):
	    return HttpResponse( first * second )
	if ( operation == "div" ):
        return HttpResponse( first / second )