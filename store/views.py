from django.http import HttpResponse
from django.shortcuts import render

from .models import ALBUMS
# Create your views here.

def index(request):
	message = "hello, world"
	return HttpResponse(message)

def listing(request):
	albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
	message = """Les albums : \n<ul>{}</ul>""".format("\n".join(albums))
	return HttpResponse(message)

def detail(request, album_id):
	id = int(album_id)
	album = ALBUMS[id]
	artists = " ".join([artists['name'] for artist in album['artists']])
	messatge = "Le nom de l'album est {}. IL a été écrit par {}".format(album['name', artists])
	return HttpResponse(message)
