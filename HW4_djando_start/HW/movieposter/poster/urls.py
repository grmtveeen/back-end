from django.urls import path
from .views import posters_list, poster_description, create_poster, delete_poster


urlpatterns = {
    path('', posters_list, name='posters_list'),                                    #render and list
    path('create/', create_poster, name='create_poster'),                           #create
    path('delete/', delete_poster, name='delete_poster'),                           #delete
    path('<int:post_id>/', poster_description, name='poster_description'),          #description
}