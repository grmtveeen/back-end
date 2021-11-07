from django.shortcuts import render
from django.http.response import JsonResponse


def actor(request, actor_id):
    return JsonResponse({'Description of actor with id:': actor_id})


def actors_list(request):
    actors = {'Actor A': 'description A', 'Actor B': 'description B', 'Actor C': 'description C',
              'Actor D': 'description D'}
    return JsonResponse(actors)
