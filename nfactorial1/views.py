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
	if ( operation == "mult" ):
	    first *= second
        return HttpResponse( first )

	if ( operation == "div" ):
		first /= second
        return HttpResponse( first )

	if ( operation == "add" ):
        first += second
        return HttpResponse( first )	
	
    if ( operation == "sub" ):
	    first -= second
        return HttpResponse( first )
