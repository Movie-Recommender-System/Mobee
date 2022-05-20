from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('create/<str:kind>/', views.movie_create),
    path('kind/<str:kind>/', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail_or_wish_movie),
    path('<int:movie_pk>/reviews/', views.create_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.create_review_update_or_delete),
]