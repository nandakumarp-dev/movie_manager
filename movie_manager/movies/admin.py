from django.contrib import admin

# Register your models here.


# movies/admin.py

from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date']