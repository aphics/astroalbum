from django.db import models
from django.contrib.auth.models import User
from albumapp.models import Album


# Create your models here.

class SwapOperations(models.Model):
    emissor_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='emissor_user')
    emissor_album = models.ForeignKey(Album, on_delete=models.DO_NOTHING, related_name='emissor_album')
    receptor_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='receptor_user')
    receptor_album = models.ForeignKey(Album, on_delete=models.DO_NOTHING, related_name='receptor_album')