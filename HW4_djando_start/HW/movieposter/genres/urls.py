from django.urls import path
from .views import genres_list, genre


urlpatterns = {
    path('', genres_list, name='genres_list'),
    path('genre/<int:genre_id>/', genre, name='genre'),
}