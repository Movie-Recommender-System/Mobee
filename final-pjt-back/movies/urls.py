from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('create/', views.movie_create),
    path('recommendation/', views.recommendation),
    path('list/<str:kind>/', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail_wish_movie),
    path('<int:movie_pk>/reviews/', views.create_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_update_or_delete),
]