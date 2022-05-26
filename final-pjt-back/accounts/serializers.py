from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Genre, Movie, Review
from articles.models import Article, Comment


class ProfileSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'poster_key')

    class ReviewSerializer(serializers.ModelSerializer):
        class MovieSerializer(serializers.ModelSerializer):

            class Meta:
                model = Movie
                fields = ('pk', 'title',) 

        movie = MovieSerializer()
        like_count = serializers.IntegerField(source='like_users.count', read_only=True)

        class Meta:
            model = Review
            fields = ('pk', 'movie', 'content', 'score', 'like_count')

    class ArticleSerializer(serializers.ModelSerializer):
        like_count = serializers.IntegerField(source='like_users.count', read_only=True)

        class Meta:
            model = Article
            fields = ('pk', 'title', 'content', 'like_count')

    class CommentSerializer(serializers.ModelSerializer):

        class ArticleSerializer(serializers.ModelSerializer):

            class Meta:
                model = Article
                fields = ('pk', 'title', )
        article = ArticleSerializer()
        class Meta:
            model = Comment
            fields = ('pk', 'article', 'content')

    wish_movie_list = MovieSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    articles = ArticleSerializer(many=True)
    comments = CommentSerializer(many=True)
    preferred_genres = serializers.SerializerMethodField('preferred')

    def preferred(self, user):
        genres = {}
        for genre in Genre.objects.all():
            genres[genre.name] = 0

        for review in Review.objects.filter(user=user):
            for movie_genre in review.movie.genres.all():
                genres[movie_genre.name] += review.score - 3

        for wish_movie in user.wish_movie_list.all():       # 찜한 영화의 장르는 별 4개와 같게!
            for movie_genre in wish_movie.genres.all():
                genres[movie_genre.name] += 1
        
        data = {'genres': [], 'scores' : [], 'best_genres' : []}
        genres = list(genres.items())
        for i in range(len(genres)):
            data['genres'].append(genres[i][0])
            data['scores'].append(genres[i][1])

        genres.sort(key=lambda x: x[1], reverse=True)

        for idx, genre in enumerate(genres):    
            if idx == 5:
                break
            if genre[1] > 0:
                data['best_genres'].append(genre[0])   # # 선호 장르 최대 5개(없으면 선호도가 0이면 X)     
                
        return data

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'wish_movie_list', 'reviews', 
        'preferred_genres', 'articles', 'comments')


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'is_staff')