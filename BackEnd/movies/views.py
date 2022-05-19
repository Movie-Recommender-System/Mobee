from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .models import Movie, Genre
from .serializers import MovieSerializer, MovieListSerializer, GenreSerializer

BASE_URL = 'https://api.themoviedb.org/3'   # tmdb URL
params = {
    'api_key': '0092d2cc473c39e4782f65d37de965bd',
    'language': 'ko-KR',
}

def movie_initial_setting(request):
    # tmdb 장르 받아오기
    path = '/genre/movie/list'
    genres = requests.get(BASE_URL+path, params = params).json()['genres']
    genres_data = []
    for genre in genres:
        if Genre.objects.all().filter(name=genre['name']).exists():
            continue
        genres_data.append({'name' : genre['name']})
    
    serializer = GenreSerializer(data=genres_data, many=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    
    # tmdb 영화 인기 영화 100개 가져오기
    for page in range(1, 6):
        popular_params = {
            'api_key': '0092d2cc473c39e4782f65d37de965bd',
            'region': 'KR',
            'language': 'ko-KR',
            'page': page,
        }
        path = '/movie/popular'
        movies = requests.get(BASE_URL+path, params = popular_params).json()['results']
        for movie in movies:
            if Movie.objects.all().filter(title=movie['title']).exists():
                continue
            movie_data = {
                'title' : movie['title'],
                'poster_path' : f'https://image.tmdb.org/t/p/w500{movie["poster_path"]}',
                'release_date' : movie['release_date'],
            }
            serializer = MovieListSerializer(data=movie_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            
            # 영화와 장르 연결하기
            movie_data = get_object_or_404(Movie, title=movie['title'])
            path = f'/movie/{movie["id"]}'
            genres = requests.get(BASE_URL+path, params = params).json()['genres']
            for genre in genres:
                genre_data = get_object_or_404(Genre, name=genre['name'])
                genre_data.movies.add(movie_data)
    return JsonResponse(['init success'], safe=False)

    # 트레일러 요청
    # path = f'/movie/{movie["id"]}/videos'
    # params = {
    #     'api_key': '0092d2cc473c39e4782f65d37de965bd',
    #     'language': 'ko-KR',
    # }
    # videos = requests.get(BASE_URL+path, params = params).json()['results']
    # if not videos:
    #     params = {
    #     'api_key': '0092d2cc473c39e4782f65d37de965bd',
    #     'language': 'en-US',
    #     }
    #     videos = requests.get(BASE_URL+path, params = params).json()['results']
    # video_key = videos[0]['key']
    # video_path = f'http://www.youtube.com/watch?v={video_key}',

def movie_list(request, kind):
    pass
    

def movie_detail_or_movie_wish_list(request, movie_pk):
    pass


def create_review(request, movie_pk):
    pass


def create_review_update_or_delete(request, movie_pk, review_pk):
    pass