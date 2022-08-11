from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from .models import Moive


def show_all_movie(request):
    movies = Moive.objects.annotate(new_field_bool=Value(True))
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))
    return render(request, 'movie_app/all_movies.html', {

        'movies': movies,
        "agg": agg,

    })


def show_one_movie(request, id_movie: int):
    movie = Moive.objects.get(id=id_movie)
    return render(request, 'movie_app/one_movie.html', {

        'movie': movie

    })
