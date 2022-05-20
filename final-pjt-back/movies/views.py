from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .models import Movie, Genre, Review
from .serializers.movie import MovieCreateSerializer, MovieSerializer, MovieListSerializer, GenreSerializer
from django.db.models import Count, Avg


BASE_URL = 'https://api.themoviedb.org/3'   # tmdb URL
User = get_user_model()

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


# 찜한 영화 순
@api_view(['GET'])
def movie_list(request, kind):
    def wish():         # 찜 많이 한 순으로 정렬
        movies = Movie.objects.annotate(wished_count=Count('wished_users')).order_by('-wished_count')
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    def person():       # 개인화 알고리즘 (리뷰 남긴 영화의 장르를 분석해 가장 좋아하는 장르로 이루어진 영화 보여주기)
        genres = {}
        watch_movies = []
        for genre in Genre.objects.all():
            genres[genre.name] = 0
        user = request.user
        for review in Review.objects.filter(user=user):
            watch_movies.append(review.movie.pk)
            for movie_genre in review.movie.genres.all():
                genres[movie_genre.name] += review.score - 3        # 장르에 점수 -2 -1 0 1 2

        result_data = []
        movies = Movie.objects.annotate(wished_count=Count('wished_users'))

        serializer = MovieListSerializer(movies, many=True)
        data = serializer.data
        scores = [[0, i] for i in range(movies.count())]        # 추천도
        for idx, movie in enumerate(movies):
            score = 0
            if movie.pk in watch_movies:
                score = -10         # 봤던 영화는 보여주지 않는다.
                continue
            for genre in movie.genres.all():
                score += genres[genre.name]
            scores[idx][0] = score
        scores.sort(reverse=True)

        cnt = 0
        for v, idx in scores:
            if cnt == 10:           # 10개 이하로 출력
                break
            if v < 0:               # 추천도가 0보다 작아지면 종료
                break
            cnt += 1
            result_data.append(data[idx])
        return Response(result_data)

    if kind == 'wish':
        return wish()
    if kind == 'person':
        return person()




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