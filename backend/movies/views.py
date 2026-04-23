from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Series
from .serializers import MovieSerializer, SeriesSerializer

class MovieList(generics.ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        is_popular = self.request.query_params.get('is_popular')
        if is_popular == 'true':
            queryset = queryset.filter(is_popular=True)
        return queryset

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeriesList(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

class SeriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        movies = Movie.objects.filter(title__icontains=query)
        series = Series.objects.filter(title__icontains=query)
        movie_data = MovieSerializer(movies, many=True).data
        series_data = SeriesSerializer(series, many=True).data
        return Response(list(movie_data) + list(series_data))