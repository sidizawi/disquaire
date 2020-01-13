from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
	message = "hello, world"
	return HttpResponse(message)
