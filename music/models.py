from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=200)
    album_logo = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('music:details',kwargs={'pk':self.pk})

    def __str__(self):
        return self.artist + "  :  " +self.album_title+" ; "


class Songs(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100)
    song_title = models.CharField(max_length=300)
    ## boolean variable is used to mark if we select a particular song is our fav.
    is_favourate = models.BooleanField(default=False)
    def __str__(self):
        return self.song_title