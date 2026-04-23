from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster_path = models.CharField(max_length=500)
    release_date = models.DateField()
    is_popular = models.BooleanField(default=False)

class Series(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster_path = models.CharField(max_length=500)
    release_date = models.DateField()

    def __str__(self):
        return self.title

class TVChannel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    poster_path = models.CharField(max_length=500)
    stream_url = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.title