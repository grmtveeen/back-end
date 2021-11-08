from django.shortcuts import render
from django.http.response import JsonResponse, Http404
from .models import Poster
from actors.models import Actor
from genres.models import Genre
from movies.models import Movie
from cinemas.models import Cinema
import json


def poster_description(request, post_id, date):
    if request.method == 'GET':
        try:
            Movie.objects.get(id=post_id)
        except Movie.DoesNotExist:
            raise Http404
        return render(request, 'poster/poster_description.html',
                      context={'posters': Poster.objects.filter(id=post_id)})
    return JsonResponse({'ER': 'You can use only GET for that'}, status=405)


def posters_list(request):
    if request.method == 'GET':
        return render(request, 'poster/posters.html', context={'posters': Poster.objects.all(),
                                                               'movies': Movie.objects.all(),
                                                               'actors': Actor.objects.all(),
                                                               'genre': Genre.objects.all()})
    return JsonResponse({'ER': 'You can use only GET for that'}, status=405)


def create_poster(request):
    if request.method == 'POST':
        request_decode = json.loads(request.body.decode('utf-8'))
        if 'actor_name' in request_decode:
            try:
                Actor.objects.get(name=request_decode['actor_name'])
            except Actor.DoesNotExist:
                Actor.objects.create(name=request_decode['actor_name'], born=request_decode['born'],
                                     description=request_decode['description_actor'])
        if 'date' in request_decode:
            try:
                Poster.objects.get(date=request_decode['date'])
            except Poster.DoesNotExist:
                Poster.objects.create(date=request_decode['date'])
        if 'genre' in request_decode:
            try:
                Genre.objects.get(genre=request_decode['genre'])
            except Genre.DoesNotExist:
                Genre.objects.create(genre=request_decode['genre'])
        if 'title' in request_decode:
            Movie.objects.create(title=request_decode['title'],
                                 main_actor_id=Actor.objects.get(name=request_decode['actor_name']).id,
                                 genre_id=Genre.objects.get(genre=request_decode['genre']).id,
                                 year=request_decode['year'], link=request_decode['link'], img=request_decode['img'],
                                 description=request_decode['description_movie'],
                                 poster_id=Poster.objects.get(date=request_decode['date']).id)
        if 'actor_name' not in request_decode and 'date' not in request_decode and 'genre' not in request_decode and \
                'title' not in request_decode:
            return JsonResponse({'ER': 'JSON request does not match the format!'}, status=400)
        return JsonResponse({'OK': 'created!'}, status=200)
    return JsonResponse({'ER': 'You have to use only POST for that'}, status=405)


def delete_poster(request, movie_id):
    if request.method == 'GET':
        try:
            p = Movie.objects.get(id=movie_id)
        except Genre.DoesNotExist:
            return JsonResponse({'ER': 'Movie DoesNotExist'}, status=412)
        p.delete()
        return JsonResponse({'OK': 'Movie deleted!'}, status=200)
    return JsonResponse({'ER': 'You have to use only GET for that'}, status=405)
