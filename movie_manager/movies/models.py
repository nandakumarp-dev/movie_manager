from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movies/')
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title