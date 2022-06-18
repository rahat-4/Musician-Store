from ctypes import alignment
from django.contrib import admin
from musician_info.models import Musician, Album

# Register your models here.
admin.site.register(Musician)
admin.site.register(Album)
