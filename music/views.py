# -*- coding: utf-8 -*-
# from __future__ import unicode_literals


## render is a class which internally calls template loader , its a smart way to reduce the code.
#context is a predefined template which used to hold all required parametters for html template.
#from django.http import Http404
#from django.http import HttpResponse
# from models import Album, Songs
# from django.shortcuts import render,get_object_or_404

#required import for generic views
from models import Album, Songs
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView

## classes code for generic views

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'album_all'



    def get_queryset(self):
        return Album.objects.all()

class DetailsView(generic.DetailView):
    model=Album
    template_name = 'music/details.html'

class addAlbum(CreateView):
    model=Album
    fields = ['artist','album_title','album_logo']

class updateAlbum(UpdateView):
    model = Album

# desgin before implimenting generic design view.
#def index(request):
#    album_all=Album.objects.all()
#     context = {'album_all': album_all}
#     return render(request,'music/index.html',context)
#
#
# def details(request, album_id):
#     # try:
#     #     single_album=Album.objects.get(id=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Id is invalid")
#     # get_object_or_404 is same as above try catch logic
#     single_album=get_object_or_404(Album,pk=album_id)
#     return render(request,'music/details.html',{'album':single_album})
#
# def favorite(request, album_id):
#     single_album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song= single_album.songs_set.get(pk=request.POST['song'])
#     except(KeyError,Songs.DoesNotSelected):
#         return render(request,'music/details.html',{'album':single_album,
#                                                      'error_message': "selected songs does not exists",
#                                                   })
#     else:
#         selected_song.is_favourate = True
#         selected_song.save()
#         return render(request, 'music/details.html', {'album': single_album})

