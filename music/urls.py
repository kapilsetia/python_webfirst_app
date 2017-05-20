from django.conf.urls import url
from . import views

app_name='music'

urlpatterns = [
    #/music/
    #url(r'^$', views.index, name='index'),
    # for generic view.
    url(r'^$', views.IndexView.as_view(), name='index'),

    #music/33/
   # url(r'^(?P<album_id>[0-9]+)/$', views.details, name='detail'),
    #for generic view
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),
    #music/33/favorite/
    #url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'album/add/$',views.addAlbum.as_view(),name='album-add')

]

