from django.http import HttpResponseRedirect

from django.shortcuts import render,redirect
from musicmanagement.models import Music

def list_music(request):
    music = Music.objects.all()
    return render(request, 'list_music.html',{'music': music})

from musicmanagement.forms import MusicForm

def create_music(request):
    form = MusicForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_music')
    return render(request, 'music_form.html',{'form':form})


def update_music(request, id):
    music = Music.objects.get(id=id)
    form = MusicForm(request.POST or None, instance=music)

    if form.is_valid():
        form.save()
        return redirect('list_music')

    return render(request, 'music_form.html', {'form': form, 'music': music})


def delete_music(request, id):
    music = Music.objects.get(id=id)

    if request.method == 'POST':
        music.delete()
        return redirect('list_music')

    return render(request, 'music_delete_confirm.html', {'music': music})

def search_basic(request):
    if 'q' in request.GET:
        q = request.GET['q']
        message = 'You searched for: %r' % request.GET['q']
        music = Music.objects.filter(continents__icontains=q)

    else:
        message = 'You submitted an empty form.'
    return render(request, 'list_music.html', {'message': message, 'music': music})



