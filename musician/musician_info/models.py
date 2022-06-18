from django.db import models
from django.urls import reverse
# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name+" "+self.last_name

    def get_absolute_url(self):
        return reverse('musician_info:musician_detail', kwargs={'pk': self.pk})


class Album(models.Model):
    artist = models.ForeignKey(
        Musician, on_delete=models.CASCADE, related_name='album_list')
    album_name = models.CharField(max_length=50)
    release_date = models.DateField()
    choice = (
        (1, "Worst"),
        (2, "Bad"),
        (3, "Good"),
        (4, "Very Good"),
        (5, "Excellent")
    )
    rating = models.IntegerField(choices=choice)

    def __str__(self):
        return self.album_name+', Rating: '+str(self.rating)

    def get_absolute_url(self):
        return reverse('musician_info:musician_detail', kwargs={'pk': self.artist.id})
