from django.db import models

# Create your models here.


class album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=550)
    genre = models.CharField(max_length=150)
    album_logo = models.CharField(max_length=1250)

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title