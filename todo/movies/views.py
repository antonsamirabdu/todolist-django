from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movies
from .forms import MovieForm


# Create your views here.
def index(request):
    return HttpResponse('movies')


def movies_list(request):
    all_movies = Movies.objects.all()
    my_context = {'movies_list': all_movies}
    return render(request, 'movies/movies_list.html', context=my_context)


def movies_details(request, pk):
    movie_index = Movies.objects.get(pk=pk)
    my_context = {'movie': movie_index}
    print(my_context)
    return render(request, 'movies/movies_details.html', context=my_context)


def movies_delete(request, pk):
    movie_index = Movies.objects.get(pk=pk).delete()
    my_context = {'movie': movie_index}
    print(my_context)
    return redirect('movies:movies-list')


def movies_update(request, pk):
    movie = Movies.objects.get(pk=pk)
    movie_form = MovieForm(instance=movie)
    if request.method == 'POST':
        movie_form = MovieForm(data=request.POST, instance=movie)
        if movie_form.is_valid():
            print('yes is valid')
            movie_form.save()
            return redirect('movies:movies-details', pk=movie.id)
    return render(request, 'movies/movies_update.html', context={'form': movie_form, 'movie': movie})


def movies_create(request):
    movie_form = MovieForm()
    if request.method == 'POST':
        movie_form = MovieForm(data=request.POST, files=request.FILES)
        if movie_form.is_valid():
            print('yes is valid')
            movie_form.save()
            return redirect('movies:movies-list')
    return render(request, 'movies/movies_create.html', context={'form':movie_form})

