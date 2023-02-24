from django.contrib import admin

from .models import Catalogue, Album

# Register your models here.

admin.site.register(Catalogue)

admin.site.register(Album)