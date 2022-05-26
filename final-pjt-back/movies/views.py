import requests

from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from .serializers.review import ReviewSerializer
from .serializers.movie import MovieCreateSerializer, MovieSerializer, MovieListSerializer, GenreSerializer
from .models import Movie, Genre, Review

User = get_user_model()

BASE_URL = 'https://api.themoviedb.org/3'   # tmdb URL
params = {
    'api_key': '0092d2cc473c39e4782f65d37de965bd',
    'language': 'ko-KR',
}

@api_view(['POST'])
@permission_classes([IsAdminUser])      # 관리자만 가능!!
def movie_create(request, kind, pages):
    # 영화 DB 초기 설정(genres와 popular_movies tmdb에서 받아오기)
    add_data = {'genres':[], 'movies':[]}
    # tmdb 장르 받아오기
    path = '/genre/movie/list'
    genres = requests.get(BASE_URL+path, params = params).json()['genres']
    genres_data = []
    for genre in genres:
        # 중복 장르는 제외!
        if Genre.objects.all().filter(pk=genre['id']).exists():
            continue
        genres_data.append({
            'pk' : genre['id'],
            'name' : genre['name']
        })
        add_data['genres'].append({'id' : genre['id'], 'name' : genre['name']})

    serializer = GenreSerializer(data=genres_data, many=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()       # 장르 저장

    # tmdb 영화 인기 영화 5 page 받아오기(한국 번역 트레일러 없는 영화 제외)

    for page in range(1, pages + 1):
        movies_params = {
            'api_key': '0092d2cc473c39e4782f65d37de965bd',
            'region': 'KR',
            'language': 'ko-KR',
            'page': page,
        }
        path = f'/movie/{kind}'
        movies = requests.get(BASE_URL+path, params = movies_params).json()['results']
        for movie in movies:
            # 영화가 등록되어 있지 않는 경우만!
            if Movie.objects.all().filter(pk=movie['id']).exists():
                continue

            if not movie["poster_path"] or not movie["backdrop_path"]:    # 포스터나 배경이미지가 없는 경우 제외    
                continue

            # 영화 트레일러 요청
            path = f'/movie/{movie["id"]}/videos'
            videos = requests.get(BASE_URL+path, params = params).json()['results']

            if not videos:      # 트레일러 없는 경우 제외
                continue
            video_key = videos[0]['key']    # 비디오 하나만 뽑는다.

            # 상영 시간 요청
            path = f'/movie/{movie["id"]}'
            runtime = requests.get(BASE_URL+path, params = params).json()['runtime']

            # 영화 감독 이름
            path = f'/movie/{movie["id"]}/credits'
            directors = requests.get(BASE_URL+path, params = params).json()['crew']
            if not directors:   # 영화 감독 없으면 제외
                continue
            director_name = directors[0]['name']

            movie_data = {
                'pk' : movie['id'],
                'title' : movie['title'],
                'overview' : movie['overview'],
                'runtime' : runtime,
                'release_date' : movie['release_date'],
                'director_name' : director_name,
                'poster_key' : movie["poster_path"],
                'backdrop_key' : movie['backdrop_path'],
                'video_key' : video_key
            }
            add_data['movies'].append(movie['title'])
            serializer = MovieCreateSerializer(data=movie_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()       # 영화 저장
            
            movie_data = get_object_or_404(Movie, pk=movie["id"])
            # 영화와 장르 연결하기
            for genre_id in movie['genre_ids']:
                genre_data = get_object_or_404(Genre, pk=genre_id)
                genre_data.movies.add(movie_data)       # 영화와 장르 연결
    return Response(add_data)   # 추가된 장르와 영화 정보 출력


@api_view(['GET'])
def movie_list(request, kind):
    # 찜 많은 순으로 정렬
    def wish():         
        movies = Movie.objects.annotate(wished_count=Count('wished_users')).order_by('-wished_count')
        serializer = MovieListSerializer(movies, many=True)

        return Response(serializer.data)
    # 최근 영화 순으로 정렬
    def recent():
        movies = Movie.objects.annotate(wished_count=Count('wished_users')).order_by('-release_date')
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    # 장르만 조회
    def genre():
        genre = get_object_or_404(Genre, name=kind)
        movies = genre.movies.annotate(wished_count=Count('wished_users')).order_by('-wished_count')
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    if kind == 'wish':
        return wish()
    elif kind == 'recent':
        return recent()
    else:
        return genre()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommendation(request):
    # 개인화 알고리즘 (리뷰 남긴 영화의 장르를 분석해 가장 좋아하는 장르로 이루어진 영화 보여주기)
    genres_score = {}       # 내가 남긴 리뷰를 바탕으로 선호 장르 조사
    watch_movies = []       # 내가 본 영화 등록(나중에 그 영화는 제외하기 위해)
    for genre in Genre.objects.all():
        genres_score[genre.name] = 0
    user = request.user
    for review in Review.objects.filter(user=user):
        watch_movies.append(review.movie.pk)
        for movie_genre in review.movie.genres.all():
            genres_score[movie_genre.name] += review.score - 3        # 장르에 점수 -2 -1 0 1 2
    
    for wish_movie in user.wish_movie_list.all():       # 찜한 영화의 장르는 별 4개와 같게!
        watch_movies.append(wish_movie.pk)
        for movie_genre in wish_movie.genres.all():
            genres_score[movie_genre.name] += 1
    result_data = []
    movies = Movie.objects.annotate(wished_count=Count('wished_users'))
    
    serializer = MovieListSerializer(movies, many=True)
    data = serializer.data
    scores = [[0, i] for i in range(movies.count())]        # 영화에 매길 추천도
    for idx, movie in enumerate(movies):
        score = 0
        if movie.pk in watch_movies:
            score = -10         # 봤던 영화는 보여주지 않는다.
            continue
        for genre in movie.genres.all():
            score += genres_score[genre.name]
        scores[idx][0] = score
    scores.sort(reverse=True)

    cnt = 0
    for v, idx in scores:
        if cnt == 10:           # 10개 이하로 출력
            break
        if v <= 0:               # 추천도가 0 이하면 종료
            break
        cnt += 1
        result_data.append(data[idx])
    return Response(result_data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])    # 영화 조회는 아무나, 찜 누르기는 인증된 유저만
def movie_detail_wish_movie(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)       # 영화가 있어야 한다.
    def detail():
        serializer = MovieSerializer(movie)
        data = serializer.data
        if movie.wished_users.filter(pk=user.pk).exists():
            data['is_wished'] = True
        else:
            data['is_wished'] = False
        if movie.reviews.filter(user=user.pk).exists():
            data['is_reviewed'] = True
        else:
            data['is_reviewed'] = False
        idx = 0
        for review in movie.reviews.all():
            if review.like_users.filter(pk=user.pk).exists():
                data['reviews'][idx]['is_liked'] = True
            else:
                data['reviews'][idx]['is_liked'] = False
            idx += 1
        return Response(data)
    def wish():
        if movie.wished_users.filter(pk=user.pk).exists():      # wish movie에 등록되어있다면
            movie.wished_users.remove(user)                     # 제거
        else:
            movie.wished_users.add(user)                        # 아니면 추가

    if request.method == 'GET':
        return detail()
    else:
        wish()
        return detail()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    serializer = ReviewSerializer(data=request.data)

    if movie.reviews.filter(user=user).exists():
        return Response(["이 영화에 남긴 리뷰가 존재합니다."], status=status.HTTP_403_FORBIDDEN)     # 이미 영화에 남긴 리뷰가 있으면 작성 X

    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)

        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_update_or_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)
        else:
            return Response(["작성한 사용자만 수정 권한이 있습니다."], status=status.HTTP_403_FORBIDDEN)

    def delete_review():
        if request.user == review.user or request.user.is_staff == 1:   # 작성한 사용자나 관리지만 제거
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        else:
            return Response(["관리자나 작성한 사용자만 삭제할 권한이 있습니다."], status=status.HTTP_403_FORBIDDEN)
    
    if not movie.reviews.filter(pk=review.pk).exists():
        return Response(["사용자가 이 영화에 작성한 리뷰가 없습니다."], status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()


@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])    # 댓글 좋아요 누르기는 인증된 유저만
def like_review(request, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)       # 리뷰가 있어야 한다.

    if review.like_users.filter(pk=user.pk).exists():
        review.like_users.remove(user)
    else:
        review.like_users.add(user)

    serializer = ReviewSerializer(review)
    return Response(serializer.data)


@api_view(['GET'])
def genres(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)