from django.db import models

# Create your models here.
class album(models.Model):
    artist=models.CharField(max_length=250)
    albume_title=models.CharField(max_length=250)
    genor=models.CharField(max_length=250)
    albume_logo=models.CharField(max_length=1000)
    def __str__(self):
        return self.albume_title+'_'+self.artist

class song(models.Model):
    albums=models.ForeignKey(album,on_delete=models.CASCADE)
    fileType=models.CharField(max_length=250)
    song_title=models.CharField(max_length=200)
