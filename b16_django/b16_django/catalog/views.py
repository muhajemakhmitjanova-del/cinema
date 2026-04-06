from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.core.paginator import Paginator
from .models import Category, Genre, Movie
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy


from .forms import (
    CategoryForm,
    GenreForm,
    MovieForm,
    CustomUserRegistrationForm,
    CustomLoginForm,
)

# Главная страница
def main_page(request):
    categories = Category.objects.all()
    genres = Genre.objects.all()
    
    query = request.GET.get('q')
    movies = Movie.objects.all()

    if query:
        movies = movies.filter(name__icontains=query)

    page_number = request.GET.get('page', 1)
    paginator = Paginator(movies, 3)
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'movies': page_obj,
        'genres': genres,
        'query': query,
    }
    return render(request, 'index.html', context)

class MovieDetailView(TemplateView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = "movie"

# Детальная страница фильма
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})


# Страница категории (С ПАГИНАЦИЕЙ)
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    movies = Movie.objects.filter(category=category)

    qwery = request.GET.get('q')
    if qwery:
        movies = movies.filter(name__icontains=qwery)

    page_number = request.GET.get('page', 1)
    paginator = Paginator(movies, 3)
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'movies': page_obj,
        'qwery': qwery,
    }

    return render(request, 'category_detail.html', context)


# def add_movie(request):
#     if request.method == "POST":
#         form = MovieForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("main_page")
#     else:
#         form = MovieForm()

#     return render(request, "add_movie.html", {"form": form})


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main_page")
    else:
        form = CategoryForm()

    return render(request, "add_category.html", {"form": form})


def add_genre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main_page")
    else:
        form = GenreForm()

    return render(request, "add_genre.html", {"form": form})


def register(request):
    if request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password != password2:
            return render(request, "register.html", {"error": "Пароли не совпадают"})
    return render(request, "register.html")


def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get("password")
    return render(request, "login.html")


def change_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    categories = Category.objects.all()
    genres = Genre.objects.all()

    if request.method == "POST":
        movie.name = request.POST.get("name")
        movie.description = request.POST.get("description")
        movie.country = request.POST.get("country")
        movie.directed_by = request.POST.get("directed_by")
        movie.age_rating = request.POST.get("age_rating")
        movie.raiting = request.POST.get("raiting") or movie.raiting
        movie.category_id = request.POST.get("category")

        image = request.FILES.get("image")
        trailir_video = request.FILES.get("trailir_video")
        if image:
            movie.image = image
        if trailir_video:
            movie.trailir_video = trailir_video

        movie.save()
        movie.genre.set(request.POST.getlist("genres"))

        return redirect("movie_detail", pk=movie.pk)

    return render(request, "change_movie.html", {
        "categories": categories,
        "genres": genres,
        "movie": movie,
        "movie_genre_ids": set(movie.genre.values_list("id", flat=True)),
        "is_edit": True,
    })

# def delete_movie(request, pk):
#         movie = get_object_or_404(Movie, pk=pk)
#         movie.delete()
#         return redirect("main_page")

def ch(request):
    return redirect("main_page")

class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['genres'] = Genre.objects.all()
        context['movies'] = Movie.objects.all()
        return context

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'add_movie.html'
    form_class = MovieForm
    success_url = reverse_lazy('main_page')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['categories'] = Category.objects.all()
        return context

class CreateMovie(CreateView):
    template_name = 'add_movie.html'
    form_class = MovieForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['categories'] = Category.objects.all()
        return context

class DeleteMovieView(DeleteView):
    model = Movie
    template_name = 'catalog/movie_confirm_delete.html'
    success_url = '/'