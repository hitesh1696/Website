#from django.http import HttpResponce
from django.shortcuts import  render, get_object_or_404
from .models import album

def index(request):
    all_albums = album.objects.all()

    return render(request, 'Music/index.html', {'all_albums': all_albums})

def detail(request,album_id):
    album = get_object_or_404(album, pk=album_id)
    return render(request, 'Music/details.html', {'album': album})