from django.contrib import admin
from django.urls import path, include
from movies.views import MovieList, MovieDetail, SeriesList, SeriesDetail, SearchView, TVChannelList

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/movies/', MovieList.as_view()),
    path('api/movies/<int:pk>/', MovieDetail.as_view()),
    path('api/series/', SeriesList.as_view()),
    path('api/series/<int:pk>/', SeriesDetail.as_view()),
    path('api/channels/', TVChannelList.as_view()),
    path('api/search/', SearchView.as_view()),
    path('api/auth/', include('users.urls')),
]