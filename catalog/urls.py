from django.urls import path
from . import views

from .views import CreateMovie,add_category,add_genre,login,register,change_movie,DeleteMovieView,MainPageView
from .views import main_page,movie_detail,category_detail

urlpatterns = [
    path('main/', views.MainPageView.as_view(), name='main_page'),
    path('movie/<int:pk>/', movie_detail, name='movie_detail'),
    path('category/<str:slug>/', category_detail, name='category_detail'),
    path('add-movie/', views.CreateMovie.as_view() , name="add_movie"),
    path('add-category/', add_category, name="add_category"),
    path('add-genre/', add_genre, name="add_genre"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('change_movie/<int:pk>/', change_movie, name='change_movie'),
    path('delete_movie/<int:pk>/', views.DeleteMovieView.as_view(), name='delete_movie'),
]
