from django.urls import path, include
from .views import actors_list, actor


urlpatterns = {
    path('', actors_list, name='actors'),
    path('actor/<int:actor_id>/', actor, name='actor'),
}