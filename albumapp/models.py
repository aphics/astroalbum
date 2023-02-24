from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Catalogue(models.Model):
    messier = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=50)
    ar = models.CharField(max_length=50)
    dec = models.CharField(max_length=50)
    dist = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='album/images')

    def __str__(self):
        return f'M{self.messier}'

    class Meta:
        verbose_name_plural = 'Objetos Messier'

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    swap_status = models.BooleanField(default=False)
