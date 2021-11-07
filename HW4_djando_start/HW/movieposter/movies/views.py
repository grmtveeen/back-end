from django.shortcuts import render
from django.http.response import JsonResponse

movies = [{'name': 'Довод', 'description': 'Хорошее кино!', 'main_actor': 'футболист', 'year': 2021, 'date': '18:46'},
          {'name': 'Гнев человеческий', 'description': 'Хорошее кино!', 'main_actor': 'Джейсон Стэтхем', 'year': 2021,
           'date': '15:35'},
          {'name': 'Интерстеллар', 'description': 'Наука', 'main_actor': 'забыл', 'year': 2014, 'date': '12:20'}]


def movie(request, movie_id):
    return JsonResponse({'movie_id:': movie_id})


def movies_list(request):
    movies = ['Movie1', 'Movie2', 'Movie3', 'Movie4']
    return render(request, 'movies/movies.html', context={'movies': movies})
