from django.shortcuts import render
from django.http.response import JsonResponse


def genre(request, genre_id):
    return JsonResponse({'Genre with id:': genre_id})


def genres_list(request):
    genres = ['genres1', 'genres2', 'genres3', 'genres4']
    return JsonResponse(genres, safe=False)
