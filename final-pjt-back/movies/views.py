from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .models import Movie, Genre, Review
from .serializers.movie import MovieCreateSerializer, MovieSerializer, MovieListSerializer, GenreSerializer
from django.db.models import Count, Avg

BASE_URL = 'https://api.themoviedb.org/3'   # tmdb URL

@api_view(['POST'])
def movie_create(request, kind):
    params = {
        'api_key': '0092d2cc473c39e4782f65d37de965bd',
        'language': 'ko-KR',
    }
    # tmdb 장르 받아오기
    if kind == 'init':
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
                # 트레일러 요청
                path = f'/movie/{movie["id"]}/videos'
                videos = requests.get(BASE_URL+path, params = params).json()['results']
                if not videos:
                    continue
                video_key = videos[0]['key']
                movie_data = {
                    'id' : movie['id'],
                    'title' : movie['title'],
                    'overview' : movie['overview'],
                    'release_date' : movie['release_date'],
                    'poster_path' : f'https://image.tmdb.org/t/p/w500{movie["poster_path"]}',
                    'video_path' : f'http://www.youtube.com/watch?v={video_key}'
                }
                serializer = MovieCreateSerializer(data=movie_data)
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


# 찜한 영화 순, 평점 순
@api_view(['GET'])
def movie_list(request, kind):
    def wish():
        movies = Movie.objects.annotate(wished_count=Count('wished_users')).order_by('-wished_count')
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    if kind == 'wish':
        return wish()

# 유저 평점 기반 추천
def user_recommendation(request, user_pk):
    pass


@api_view(['GET', 'POST'])
def movie_detail_or_wish_movie(request, movie_pk):
    user = request.user
    print(user)
    movie = get_object_or_404(Movie, pk=movie_pk)

    def movie_detail():
        serializer = MovieSerializer(movie)
        data = serializer.data
        if movie.wished_users.filter(pk=user.pk).exists():
            data['is_wished'] = True
        else:
            data['is_wished'] = False
        return Response(data)

    if request.method == 'GET':
        return movie_detail()
    
    elif request.method == 'PUT':
        if movie.wished_users.filter(pk=user.pk).exists():
            movie.wished_users.remove(user)    
        else:
            movie.wished_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)



def create_review(request, movie_pk):
    pass


def create_review_update_or_delete(request, movie_pk, review_pk):
    pass