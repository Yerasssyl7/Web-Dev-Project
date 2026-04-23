from django.contrib import admin
from .models import Movie, Series, TVChannel

admin.site.register(Movie)
admin.site.register(Series)
admin.site.register(TVChannel)