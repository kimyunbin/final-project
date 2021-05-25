from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:movie_pk>/', views.detail, name='detail'),
    # path('tournament', views.tournament, name='tournament'),
    path('', views.main),
    path('genre_data', views.genre_data),
    path('movie_data2', views.movie_data2),
    path('detail/<int:movie_pk>', views.movie_detail),
    path('tournament', views.tournament),
    path('mypageMovie/<str:username>', views.mypageMovie)
]
