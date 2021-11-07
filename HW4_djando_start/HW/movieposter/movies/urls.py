from django.urls import path
from .views import movies_list, movie


urlpatterns = {
    path('', movies_list, name='movies_list'),
    path('movie/<int:movie_id>/', movie, name='movie'),
}